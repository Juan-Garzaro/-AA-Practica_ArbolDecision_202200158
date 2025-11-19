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
El programa clasifica números según un umbral (50 por defecto).  
Si el número es **mayor o igual** al umbral → “Alto”.  
Si es **menor** → “Bajo”.  

Si el archivo de datos no existe, se genera automáticamente.

## Metodología
1. Iniciar cronómetro.
2. Verificar o generar archivo `data/numeros_1000.txt`.
3. Cargar los números.
4. Clasificar usando el árbol.
5. Mostrar ejemplos, conteos y tiempo total.

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

## Conclusiones
La práctica demuestra la correcta implementación del árbol de decisión básico y el uso estructurado de Gitflow, con un flujo claro y resultados reproducibles.
