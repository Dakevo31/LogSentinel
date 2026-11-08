
# ==================================================
# LogSentinel - Python Log Analysis Tool
# Analizador de registros de eventos
# ==================================================

from pathlib import Path
from datetime import datetime
import re


# ==================================================
# 1. BIENVENIDA
# ==================================================

def mostrar_bienvenida():
    """Muestra la bienvenida del programa."""

    print("=" * 50)
    print("           LOGSENTINEL")
    print("       Python Log Analysis Tool")
    print("=" * 50)
    print("Analizador de registros y eventos de aplicaciones")
    print()


# ==================================================
# 2. LECTURA DE ARCHIVOS
# ==================================================

def leer_archivo():
    """Solicita y lee un archivo de texto."""

    print("SELECCION DE ARCHIVO")
    print("-" * 50)

    ruta = input(
        "Ingresa la ruta del archivo .txt: "
    ).strip().strip('"')

    if not ruta:
        print("\nERROR: No ingresaste una ruta.")
        return None

    archivo = Path(ruta)

    if not archivo.is_file():
        print("\nERROR: El archivo no existe.")
        return None

    if archivo.suffix.lower() != ".txt":
        print("\nERROR: Solo se permiten archivos .txt")
        return None

    try:
        with archivo.open(
            "r", encoding="utf-8-sig"
        ) as contenido:
            lineas = contenido.readlines()

        print("\nArchivo cargado correctamente.")
        print(f"Total de lineas leidas: {len(lineas)}")

        return lineas

    except (OSError, UnicodeError) as error:
        print(f"\nERROR al leer el archivo: {error}")
        return None


# ==================================================
# 3. VALIDACION DE FECHAS
# ==================================================

def validar_fecha(fecha):
    """
    Valida el formato AAAA-MM-DD y comprueba
    que la fecha exista en el calendario.
    """

    # Decision del estudiante:
    # Solo se acepta el formato AAAA-MM-DD.
    if not re.fullmatch(r"[0-9]{4}-[0-9]{2}-[0-9]{2}", fecha):
        return False

    try:
        datetime.strptime(fecha, "%Y-%m-%d")
        return True

    except ValueError:
        return False


# ==================================================
# 4. ANALISIS DE REGISTROS
# ==================================================

def analizar_registros(lineas):
    """
    Analiza la severidad, fecha y mensaje
    de cada registro del archivo.
    """

    conteo = {
        "INFO": 0,
        "WARNING": 0,
        "ERROR": 0
    }

    mal_formadas = 0
    advertencias_fecha = 0
    fechas_validas = 0
    detalles = []

    for numero, linea in enumerate(lineas, start=1):

        texto = linea.strip()

        # Decision del estudiante:
        # Las lineas vacias son registros mal formados.
        if not texto:
            mal_formadas += 1
            detalles.append(
                f"Linea {numero}: Registro vacio."
            )
            continue

        # Identificar severidad valida al inicio.
        resultado = re.match(
            r"^\[(INFO|WARNING|ERROR)\](?=\s|$)",
            texto
        )

        if not resultado:
            mal_formadas += 1
            detalles.append(
                f"Linea {numero}: Severidad no valida."
            )
            continue

        nivel = resultado.group(1)
        conteo[nivel] += 1

        # Extraer contenido despues de la severidad.
        contenido = texto[resultado.end():].strip()
        partes = contenido.split(maxsplit=1)

        fecha_estado = "ausente"
        fecha_detectada = ""
        mensaje = contenido

        if partes:
            primera_parte = partes[0]

            # Reconocemos fechas con formato permitido
            # y formatos similares pero incorrectos.
            es_candidata_fecha = (
                re.fullmatch(
                    r"[0-9]{4}-[0-9]{2}-[0-9]{2}",
                    primera_parte
                ) is not None
                or re.match(
                    r"^[0-9]{4}[-/][0-9]",
                    primera_parte
                ) is not None
                or re.fullmatch(
                    r"[0-9]{1,2}/[0-9]{1,2}/[0-9]{4}",
                    primera_parte
                ) is not None
            )

            if es_candidata_fecha:
                fecha_detectada = primera_parte

                if validar_fecha(primera_parte):
                    fecha_estado = "valida"
                else:
                    fecha_estado = "invalida"

                mensaje = (
                    partes[1].strip()
                    if len(partes) > 1
                    else ""
                )

        # Decision del estudiante:
        # Fecha ausente o invalida no descarta el evento.
        if fecha_estado == "valida":
            fechas_validas += 1

        elif fecha_estado == "invalida":
            advertencias_fecha += 1
            detalles.append(
                f"Linea {numero}: Fecha invalida "
                f"({fecha_detectada})."
            )

        else:
            advertencias_fecha += 1
            detalles.append(
                f"Linea {numero}: Fecha ausente."
            )

        # Decision del estudiante:
        # El mensaje es obligatorio.
        if not mensaje:
            mal_formadas += 1
            detalles.append(
                f"Linea {numero}: Mensaje incompleto."
            )

    return {
        "total": len(lineas),
        "conteo": conteo,
        "mal_formadas": mal_formadas,
        "fechas_validas": fechas_validas,
        "advertencias_fecha": advertencias_fecha,
        "detalles": detalles
    }


# ==================================================
# 5. MOSTRAR RESULTADOS
# ==================================================

def mostrar_resultados(resultados):
    """Muestra el resumen del analisis en consola."""

    print("\n" + "=" * 50)
    print("           RESUMEN DE LOGSENTINEL")
    print("=" * 50)

    print(f"Total de lineas analizadas: {resultados['total']}")

    print("\nEVENTOS POR SEVERIDAD")
    print("-" * 50)

    conteo = resultados["conteo"]

    print(f"INFO:    {conteo['INFO']}")
    print(f"WARNING: {conteo['WARNING']}")
    print(f"ERROR:   {conteo['ERROR']}")

    print("\nVALIDACION DE REGISTROS")
    print("-" * 50)

    print(
        f"Lineas mal formadas o incompletas: "
        f"{resultados['mal_formadas']}"
    )

    print(
        f"Eventos con fecha valida: "
        f"{resultados['fechas_validas']}"
    )

    print(
        f"Advertencias de fecha: "
        f"{resultados['advertencias_fecha']}"
    )

    if resultados["detalles"]:
        print("\nDETALLE DE ADVERTENCIAS")
        print("-" * 50)

        for detalle in resultados["detalles"]:
            print(f"- {detalle}")

    print("\n" + "=" * 50)
    print("Analisis finalizado correctamente.")
    print("=" * 50)


# ==================================================
# 6. FUNCION PRINCIPAL
# ==================================================

def main():
    """Controla la ejecucion del programa."""

    mostrar_bienvenida()

    lineas = leer_archivo()

    if lineas is None:
        return

    resultados = analizar_registros(lineas)

    mostrar_resultados(resultados)


# ==================================================
# 7. INICIO DEL PROGRAMA
# ==================================================

if __name__ == "__main__":
    main()
