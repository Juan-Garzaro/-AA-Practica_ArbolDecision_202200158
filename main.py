"""
main.py
Flujo principal: carga datos, aplica el árbol y muestra resultados.
"""

import time
from pathlib import Path
from src.data_loader import verificar_o_generar_archivo, cargar_numeros
from src.decision_tree import DecisionTreeThreshold

UMBRAL = 50  # Se puede cambiar o parametrizar


def imprimir_ejemplos(valores, arbol):
    """
    Imprime los primeros 10 ejemplos clasificados en consola.
    """
    print("\nEjemplos (primeros 10):")
    for v in valores[:10]:
        print(f"{v} → {arbol.classify(v)}")


def main():
    """
    Flujo completo del árbol de decisión simple.
    """
    inicio = time.time()

    BASE_DIR = Path(__file__).resolve().parent
    ruta_archivo = BASE_DIR.parent / "data" / "numeros_1000.txt"

    verificar_o_generar_archivo(ruta_archivo)

    numeros = cargar_numeros(ruta_archivo)
    print(f"Números cargados: {len(numeros)}")

    arbol = DecisionTreeThreshold(UMBRAL)

    clasificaciones = [arbol.classify(n) for n in numeros]
    altos = clasificaciones.count("Alto")
    bajos = clasificaciones.count("Bajo")

    imprimir_ejemplos(numeros, arbol)

    print("\nConteos:")
    print(f"Altos: {altos}")
    print(f"Bajos: {bajos}")

    fin = time.time()
    print(f"\nTiempo total de ejecución: {fin - inicio:.4f} segundos")


if __name__ == "__main__":
    main()
