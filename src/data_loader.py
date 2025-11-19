"""
data_loader.py
Funciones para verificar, generar y cargar el archivo de números.
"""

from pathlib import Path
import random
import os


def verificar_o_generar_archivo(ruta: Path, semilla=42):
    """
    Verifica si existe el archivo. Si no existe o está vacío, lo genera
    con 1000 números aleatorios entre 1 y 100.
    """
    ruta = ruta.resolve()
    ruta.parent.mkdir(parents=True, exist_ok=True)

    if not ruta.exists() or os.stat(ruta).st_size == 0:
        print(f"Archivo no encontrado o vacío. Generando... (semilla usada: {semilla})")
        random.seed(semilla)
        numeros = [random.randint(1, 100) for _ in range(1000)]
        with ruta.open("w") as f:
            for n in numeros:
                f.write(str(n) + "\n")
        print("Archivo generado.")
    else:
        print("Archivo encontrado y listo para usar.")


def cargar_numeros(ruta: Path):
    """
    Carga todos los números del archivo especificado.
    """
    ruta = ruta.resolve()
    with ruta.open("r") as f:
        return [int(line.strip()) for line in f.readlines()]
