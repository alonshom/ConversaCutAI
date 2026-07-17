import os
import json
from pathlib import Path

from pydub import AudioSegment

from silero_vad import (
    load_silero_vad,
    read_audio,
    get_speech_timestamps
)

from utils.rutas import ruta_base



BASE_DIR = Path(
    ruta_base()
)


CONFIG_FILE = BASE_DIR / "config.json"



def cargar_config():

    with open(
        CONFIG_FILE,
        "r",
        encoding="utf-8"
    ) as archivo:

        return json.load(archivo)



def procesar_audio(
        ruta_audio,
        sensibilidad=0.25,
        actualizar_estado=None
):

    try:

        config = cargar_config()


        output_folder = (
            BASE_DIR /
            config["output_folder"]
        )


        if actualizar_estado:

            actualizar_estado(
                "🤖 Cargando modelo IA..."
            )


        model = load_silero_vad()



        if actualizar_estado:

            actualizar_estado(
                "🔎 Detectando voces..."
            )



        audio = read_audio(
            ruta_audio
        )



        vad = config["vad"]



        segmentos = get_speech_timestamps(
            audio,
            model,
            return_seconds=True,
            threshold=sensibilidad,
            min_speech_duration_ms=
                vad["min_speech_duration_ms"],
            min_silence_duration_ms=
                vad["min_silence_duration_ms"],
            speech_pad_ms=
                vad["speech_pad_ms"]
        )



        if not segmentos:

            return None



        if actualizar_estado:

            actualizar_estado(
                f"🗣️ {len(segmentos)} segmentos encontrados"
            )



        audio_original = AudioSegment.from_file(
            ruta_audio
        )



        resultado = AudioSegment.empty()


        audio_config = config["audio"]



        for seg in segmentos:


            inicio = seg["start"] * 1000

            fin = seg["end"] * 1000


            inicio -= audio_config["start_padding_ms"]

            inicio = max(
                0,
                inicio
            )


            fin += audio_config["end_padding_ms"]



            resultado += audio_original[
                inicio:fin
            ]



        output_folder.mkdir(
            exist_ok=True
        )



        nombre = (
            "recortado_"
            +
            os.path.basename(
                ruta_audio
            )
        )



        salida = (
            output_folder /
            nombre
        )



        resultado.export(
            salida,
            format="wav"
        )



        return {

            "ruta":
                str(
                    salida.resolve()
                ),

            "nombre":
                nombre,

            "duracion_original":
                round(
                    len(audio_original)/1000,
                    2
                ),

            "duracion_final":
                round(
                    len(resultado)/1000,
                    2
                )
        }



    except Exception as e:

        print(
            "Error procesando audio:",
            e
        )

        return None