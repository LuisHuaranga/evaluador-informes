import os
import pandas as pd

def buscar_mem_num(carpeta_reporte, cabecera, valor_mem_num):
    """
    Busca un valor específico en la columna 'MEM_NUM' en todos los archivos CSV de una carpeta.

    Args:
        carpeta_reporte (str): Ruta de la carpeta que contiene los archivos CSV.
        valor_mem_num (str): Valor a buscar en la columna 'MEM_NUM'.
        cabecera (list): Lista con los nombres de las columnas para el DataFrame.

    Returns:
        list: Lista con los nombres de los archivos CSV donde se encontró el valor.
    """
    archivos_encontrados = []

    # Iterar sobre todos los archivos en la carpeta
    for archivo in os.listdir(carpeta_reporte):
        if archivo.endswith(".csv"):
            ruta_archivo = os.path.join(carpeta_reporte, archivo)
            try:
                df = pd.read_csv(ruta_archivo, sep=";", header=None, low_memory=False)
                df.columns = cabecera
                if 'MEM_NUM' in df.columns and valor_mem_num in df['MEM_NUM'].values:
                    archivos_encontrados.append(archivo)
            except Exception:
                continue

    return archivos_encontrados

def leer_cabecera(nombre_archivo):
    """Lee las cabeceras de un archivo de texto y las devuelve como una lista."""
    with open(nombre_archivo, 'r') as file:
        return [linea.strip() for linea in file.readlines()]


def lista_reportes(carpeta):
    """Devuelve una lista de archivos CSV en la carpeta especificada."""
    return [archivo for archivo in os.listdir(carpeta) if archivo.endswith('.csv')]


def cargar_datos_csv(ruta_archivo, cabecera):
    """
    Carga los datos de un archivo CSV y calcula las sumas de 'SALDO_FINAL' y 'SALDO_INICIAL'.

    Args:
        ruta_archivo (str): Ruta del archivo CSV.
        cabecera (list): Lista con los nombres de las columnas para el DataFrame.

    Returns:
        tuple: Suma de 'SALDO_FINAL', suma de 'SALDO_INICIAL' y cantidad de registros.
    """
    try:
        df = pd.read_csv(ruta_archivo, sep=";", header=None, low_memory=False)
        df.columns = cabecera
        return df['SALDO_FINAL'].sum(), df['SALDO_INICIAL'].sum(), len(df)
    except (pd.errors.EmptyDataError, Exception):
        return '-', '-', '-'


def filtrar_datos_csv(ruta_archivo, cabecera):
    """
    Filtra los registros con saldo final negativo de un archivo CSV.

    Args:
        ruta_archivo (str): Ruta del archivo CSV.
        cabecera (list): Lista con los nombres de las columnas para el DataFrame.

    Returns:
        pd.DataFrame: DataFrame con los registros filtrados (saldo final negativo).
    """
    try:
        df = pd.read_csv(ruta_archivo, sep=";", header=None, low_memory=False)
        df.columns = cabecera
        return df[df['SALDO_FINAL'] < 0]
    except (pd.errors.EmptyDataError, KeyError, FileNotFoundError, Exception):
        return pd.DataFrame()


def procesar_saldos(carpeta_reporte, archivos_csv, cabecera):
    """
    Procesa todos los archivos CSV y calcula las sumas de saldo y registros.

    Args:
        carpeta_reporte (str): Ruta de la carpeta que contiene los archivos CSV.
        archivos_csv (list): Lista de nombres de archivos CSV.
        cabecera (list): Lista con los nombres de las columnas para el DataFrame.

    Returns:
        pd.DataFrame: DataFrame con los resultados calculados.
    """
    resultados = []
    for archivo in archivos_csv:
        ruta_archivo = os.path.join(carpeta_reporte, archivo)
        suma_final, suma_inicial, cantidad_registro = cargar_datos_csv(ruta_archivo, cabecera)
        resultados.append({
            "nombre_archivo": archivo.rsplit('.', 1)[0],
            "suma_saldo_final": suma_final,
            "suma_saldo_inicial": suma_inicial,
            "cantidad_registro": cantidad_registro
        })
    
    pd.DataFrame(resultados).to_excel('result/sumSaldos_CantidadReg.xlsx', index=False) 
    


def guardar_saldos_negativos(carpeta_reporte, archivos_csv, cabecera):
    """
    Guarda los archivos con saldo final negativo en un archivo Excel.

    Args:
        carpeta_reporte (str): Ruta de la carpeta que contiene los archivos CSV.
        archivos_csv (list): Lista de nombres de archivos CSV.
        cabecera (list): Lista con los nombres de las columnas para el DataFrame.
    """
    borrar_archivos_en_carpeta("result/Menbers_saldoFinalNegativo")
    for archivo in archivos_csv:
        ruta_archivo = os.path.join(carpeta_reporte, archivo)
        df = filtrar_datos_csv(ruta_archivo, cabecera)
        if not df.empty:
            df.to_excel(f"result/Menbers_saldoFinalNegativo/{archivo.rsplit('.', 1)[0]}.xlsx", index=False)
                    

def borrar_archivos_en_carpeta(carpeta):
    """
    Borra todos los archivos dentro de una carpeta.

    Args:
        carpeta (str): Ruta de la carpeta.
    """
    try:
        # Lista todos los elementos en la carpeta
        for archivo in os.listdir(carpeta):
            ruta_completa = os.path.join(carpeta, archivo)            
            if os.path.isfile(ruta_completa):
                os.remove(ruta_completa)                
    except Exception as e:
        print(f"Error al eliminar archivos: {e}")
