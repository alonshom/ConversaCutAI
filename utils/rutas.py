import os
import sys


def ruta_base():

    if getattr(sys, "frozen", False):

        return sys._MEIPASS

    return os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )



def obtener_ruta(
        carpeta,
        archivo=""
):

    return os.path.join(
        ruta_base(),
        carpeta,
        archivo
    )