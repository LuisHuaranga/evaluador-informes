from services.ecc_service import *
import os
import time

class opcion:
    def __init__(self, carpeta_reporte, archivos_csv, cabecera):
        self.carpeta_reporte = 'Reporte EECC Loyalty'
        self.archivos_csv = lista_reportes(carpeta_reporte)
        self.cabecera = leer_cabecera('cabecera.txt')
        
    #Buscar menber en los reportes:
    def buacar_member():
        member = input("Introduzca menber: ")
        archivo_encontrado = buscar_mem_num(carpeta_reporte,cabecera, member)
        print("Member encontrado en los siguientes archivos: ")
        print("\033[1;35m" + f"{archivo_encontrado}")


    # 2. Crear un archivo (Excel) de la suma total de saldos iniciales y suma de saldos finales. 
    # 3. Crear un archivo para que muestre la cantidad total de registros por cada archivo reporte
    def sumaSaldos_cantRegistros():
        procesar_saldos(carpeta_reporte, archivos_csv, cabecera)
    
    # 4. Listado de clientes con saldo final negativo
    def saldo_negativos():
        guardar_saldos_negativos(carpeta_reporte, archivos_csv, cabecera)

