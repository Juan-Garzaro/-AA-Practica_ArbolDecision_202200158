# Práctica: Árbol de decisión minimalista en Python

## Portada
- Universidad: Universidad Da Vinci de Guatemala 
- Curso: Analisis de Algoritmos
- Práctica: Árbol de Decisión Simple
- Nombre: Juan Garzaro
- Carnet: 202200158
- Fecha: 15 Noviembre 2025

## Objetivo General
Construir y ejecutar un árbol de decisión simple en Python (sin librerías externas) para clasificar números como “Alto” o “Bajo” a partir de un umbral, aplicando de forma rigurosa el flujo de trabajo Gitflow.

## Objetivos Específicos
- Implementar un árbol de decisión minimalista con un único nodo.
- Leer un archivo TXT con 1000 números y clasificarlos.
- Generar salidas claras en consola.
- Aplicar Gitflow correctamente.
- Documentar con docstrings (PEP-257).

## Descripción Técnica
El programa clasifica cada número según un umbral definido (por defecto: **50**):

- Si el número es **mayor o igual** al umbral → → **“Alto”**  
- Si el número es **menor** al umbral → → **“Bajo”**

Si el archivo `data/numeros_1000.txt` no existe, se **genera automáticamente** con números aleatorios.

## Estructura del Proyecto

```plaintext
📁 practica_arbol_decision/
├── 📘 README.md
├── 📄 main.py
├── 📁 src/
│   ├── 📄 __init__.py
│   ├── 📄 data_loader.py
│   └── 📄 decision_tree.py
├── 📁 data/
│   └── 📄 numeros_1000.txt
│
└── 📁 docs/
    └── 📄 evidencias/   
 
```

## Requisitos
- Python **3.13.7**
- No requiere librerías externas

## Ejecución
Para ejecutar el programa:

python main.py

El sistema:

1. Verifica si existe el archivo.
2. Lo genera si está vacío o no existe.
3. Clasifica los 1000 números.
4. Muestra ejemplos, conteos y tiempo total.

## Metodología
1. Iniciar cronómetro.
2. Verificar o generar el archivo numeros_1000.txt.
3. Cargar los datos desde la carpeta /data/.
4. Procesar cada número mediante el árbol de decisión.
5. Mostrar:

 - Ejemplos de clasificación
 - Conteos totales
 - Tiempo total de ejecución

## Análisis de Complejidad
Carga de datos
Leer 1000 números desde archivo:
O(n)

Clasificación
Operación de comparación por número:
O(1)

Clasificación total
1000 × O(1) → O(n)

Complejidad global del programa 
O(n)

## Resultados de Ejecución
(Estos son ejemplos generados automáticamente)

Archivo encontrado y listo para usar.  
Números cargados: **1000**

### Ejemplos (primeros 10)
| Número | Clasificación |
|--------|---------------|
| 82 | Alto |
| 15 | Bajo |
| 4 | Bajo |
| 95 | Alto |
| 36 | Bajo |
| 32 | Bajo |
| 29 | Bajo |
| 18 | Bajo |
| 95 | Alto |
| 14 | Bajo |

### Conteos Totales
| Clasificación | Cantidad |
|---------------|----------|
| Altos | 513 |
| Bajos | 487 |

**Tiempo total:** 0.0026 segundos

## Evidencias
- Capturas en `/docs/evidencias/`
- Historial de commits

## Flujo de Trabajo (Gitflow)

Ramas utilizadas:

- develop
- feature/implementacion_arbol

Comandos principales usados:

- git flow init
- git flow feature start implementacion_arbol
- git flow feature finish implementacion_arbol
- git push origin develop

## Conclusiones
La práctica permitió implementar un árbol de decisión básico, eficiente y funcional.
Se aplicaron principios de análisis de algoritmos y el flujo Gitflow para mantener un desarrollo ordenado, reproducible y con control de versiones adecuado.
El programa cumple los objetivos planteados y demuestra un manejo correcto de estructuras simples para clasificación de datos.
