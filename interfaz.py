import customtkinter as ctk
from tkinter import filedialog
from PIL import Image
import threading
import os
import time

from core.procesador import procesar_audio
from utils.rutas import obtener_ruta


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


archivo_actual = None
procesando = False


app = ctk.CTk()

app.geometry("650x700")
app.title("ConversaCutAI - Detector inteligente de voz")


# ===============================
# LOGO
# ===============================

ruta_logo = obtener_ruta(
    "assets",
    "logo.png"
)


if os.path.exists(ruta_logo):

    imagen = Image.open(
        ruta_logo
    )

    logo = ctk.CTkImage(
        light_image=imagen,
        dark_image=imagen,
        size=(120,120)
    )

    logo_label = ctk.CTkLabel(
        app,
        text="",
        image=logo
    )

    logo_label.pack(
        pady=10
    )


# ===============================
# TITULO
# ===============================

titulo = ctk.CTkLabel(
    app,
    text="🎙️ ConversaCutAI\nDetector inteligente de voz",
    font=("Arial",26,"bold")
)

titulo.pack(
    pady=10
)


# ===============================
# SELECCION AUDIO
# ===============================

def seleccionar_audio():

    global archivo_actual

    archivo_actual = filedialog.askopenfilename(
        filetypes=[
            (
                "Archivos de audio",
                "*.wav *.mp3 *.m4a"
            )
        ]
    )

    if archivo_actual:

        archivo_label.configure(
            text=os.path.basename(
                archivo_actual
            )
        )

        estado.configure(
            text="✅ Audio cargado"
        )


boton_archivo = ctk.CTkButton(
    app,
    text="📂 Seleccionar audio",
    command=seleccionar_audio
)

boton_archivo.pack(
    pady=10
)


archivo_label = ctk.CTkLabel(
    app,
    text="Ningún archivo seleccionado"
)

archivo_label.pack(
    pady=5
)


# ===============================
# PROCESAR AUDIO
# ===============================

def iniciar():

    hilo = threading.Thread(
        target=ejecutar
    )

    hilo.start()


boton_procesar = ctk.CTkButton(
    app,
    text="▶ Procesar audio",
    command=iniciar
)

boton_procesar.pack(
    pady=15
)


# ===============================
# SENSIBILIDAD
# ===============================

sens_label = ctk.CTkLabel(
    app,
    text="Sensibilidad: 0.25"
)

sens_label.pack(
    pady=5
)


def cambiar_sensibilidad(valor):

    sens_label.configure(
        text=f"Sensibilidad: {valor:.2f}"
    )


barra_sens = ctk.CTkSlider(
    app,
    from_=0.10,
    to=0.80,
    number_of_steps=70,
    command=cambiar_sensibilidad
)

barra_sens.set(
    0.25
)

barra_sens.pack(
    pady=5
)


ayuda = ctk.CTkLabel(
    app,
    text=
    "Menor = detecta voces más bajas\n"
    "Mayor = detecta solo voces claras"
)

ayuda.pack(
    pady=10
)


# ===============================
# ESTADO
# ===============================

estado = ctk.CTkLabel(
    app,
    text="Esperando archivo",
    font=("Arial",16)
)

estado.pack(
    pady=10
)


progreso = ctk.CTkProgressBar(
    app,
    width=400
)

progreso.set(
    0
)

progreso.pack(
    pady=5
)


resultado = ctk.CTkLabel(
    app,
    text=""
)

resultado.pack(
    pady=10
)


# ===============================
# BOTONES RESULTADO
# ===============================

boton_abrir = ctk.CTkButton(
    app,
    text="🎧 Abrir audio recortado",
    state="disabled"
)

boton_abrir.pack(
    pady=5
)


boton_carpeta = ctk.CTkButton(
    app,
    text="📁 Abrir carpeta output",
    state="disabled"
)

boton_carpeta.pack(
    pady=5
)


# ===============================
# FUNCIONES AUXILIARES
# ===============================

def abrir_audio(ruta):

    ruta = os.path.abspath(
        ruta
    )

    if os.path.exists(ruta):

        os.startfile(
            ruta
        )


def abrir_carpeta():

    carpeta = obtener_ruta(
        "output"
    )

    if os.path.exists(carpeta):

        os.startfile(
            carpeta
        )


def actualizar_estado(texto):

    estado.configure(
        text=texto
    )

    app.update_idletasks()



def animar_carga():

    while procesando:

        progreso.step(
            0.05
        )

        time.sleep(
            0.1
        )


# ===============================
# PROCESAMIENTO
# ===============================

def ejecutar():

    global procesando


    if not archivo_actual:

        estado.configure(
            text="❌ Selecciona un audio primero"
        )

        return


    procesando = True

    progreso.set(
        0
    )


    hilo_animacion = threading.Thread(
        target=animar_carga
    )

    hilo_animacion.start()


    datos = procesar_audio(
        archivo_actual,
        barra_sens.get(),
        actualizar_estado
    )


    procesando = False


    progreso.set(
        1
    )


    if datos:


        estado.configure(
            text="✅ Proceso terminado"
        )


        resultado.configure(
            text=
            f"Archivo generado:\n"
            f"{datos['nombre']}\n\n"
            f"Duración:\n"
            f"{datos['duracion_original']}s → "
            f"{datos['duracion_final']}s"
        )


        boton_abrir.configure(
            state="normal",
            command=lambda:
                abrir_audio(
                    datos["ruta"]
                )
        )


        boton_carpeta.configure(
            state="normal",
            command=abrir_carpeta
        )


    else:

        estado.configure(
            text="❌ No se detectó voz"
        )


# ===============================
# INICIO
# ===============================

def iniciar_app():

    app.mainloop()