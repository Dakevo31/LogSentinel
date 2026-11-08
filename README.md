# LogSentinel – Python Log Analysis Tool

## Descripción del proyecto

LogSentinel es una herramienta desarrollada en Python que permite analizar archivos de registros (logs) en formato `.txt`.

El programa identifica eventos según su nivel de severidad, valida las fechas de los registros, detecta líneas mal formadas o incompletas y presenta un resumen de los resultados en la consola.

Este proyecto fue desarrollado utilizando inteligencia artificial como herramienta de apoyo, manteniendo las decisiones de validación, las pruebas y la revisión de resultados bajo criterio humano.

## Requisitos

- Python 3 instalado.
- Visual Studio Code o una terminal compatible.
- Archivos de registros en formato `.txt`.

No es necesario instalar librerías externas.

## Instrucciones de ejecución

1. Abrir la carpeta `LogSentinel` en Visual Studio Code.
2. Abrir una terminal dentro de la carpeta.
3. Ejecutar el comando:

   `python main.py`

4. Cuando el programa solicite la ruta del archivo, ingresar uno de los archivos de prueba, por ejemplo:

   `logs_correctos.txt`

5. Revisar el resumen generado en la consola.

## Reglas de validación definidas

- Se reconocen únicamente los niveles `INFO`, `WARNING` y `ERROR`.
- Las fechas válidas deben utilizar el formato `AAAA-MM-DD` y existir en el calendario.
- Una fecha ausente o inválida genera una advertencia, pero no invalida automáticamente el evento.
- Una severidad desconocida o ausente hace que la línea se considere mal formada.
- Las líneas vacías se consideran mal formadas.
- Un registro sin mensaje se considera incompleto.
- Todas las líneas leídas se incluyen en el total de líneas analizadas.
- Una línea puede generar más de una advertencia, pero se cuenta una sola vez como mal formada o incompleta.

## Archivos de prueba

**logs_correctos.txt:** contiene cinco registros correctamente estructurados.

**logs_errores.txt:** contiene ocho líneas, incluyendo fechas inválidas, severidades desconocidas, registros incompletos y una línea vacía.

**logs_edge_cases.txt:** contiene seis casos especiales para comprobar años bisiestos, fechas ausentes y registros incompletos.

## Resultados de las pruebas

| Archivo | Líneas | INFO | WARNING | ERROR | Mal formadas | Fechas válidas | Advertencias de fecha |
|---|---:|---:|---:|---:|---:|---:|---:|
| logs_correctos.txt | 5 | 2 | 1 | 2 | 0 | 5 | 0 |
| logs_errores.txt | 8 | 2 | 2 | 2 | 3 | 3 | 3 |
| logs_edge_cases.txt | 6 | 2 | 1 | 2 | 3 | 2 | 3 |

Los resultados obtenidos coincidieron con los resultados esperados en las pruebas realizadas.

## Uso de inteligencia artificial

Se utilizó ChatGPT como apoyo para estructurar el código, explicar funciones de Python, proponer casos de prueba y mejorar la claridad de las advertencias.

Las reglas de validación fueron definidas por el estudiante. El comportamiento del programa fue revisado mediante pruebas con archivos correctos, incorrectos y casos especiales.

Durante la revisión se identificó que la primera versión agrupaba las fechas ausentes e inválidas en una misma advertencia. Posteriormente, se mejoró la función de análisis para distinguir ambas situaciones.

## Estructura del proyecto

```text
LogSentinel/
├── main.py
├── README.md
├── logs_correctos.txt
├── logs_errores.txt
├── logs_edge_cases.txt
└── Reflexion_Tecnica.pdf
```

## Limitaciones

El programa está diseñado para registros con niveles de severidad al inicio de cada línea y fechas en formato `AAAA-MM-DD`. No pretende interpretar todos los formatos de logs existentes.

## Conclusión

LogSentinel demuestra cómo la inteligencia artificial puede acelerar el desarrollo de software cuando sus propuestas se acompañan de decisiones humanas, validación de resultados y pruebas prácticas.