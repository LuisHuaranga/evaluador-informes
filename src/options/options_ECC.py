from services.funcionesECC import *
import os
import time


carpeta_reporte = carpeta_reporte
archivos_csv = lista_reportes(carpeta_reporte)
cabecera = leer_cabecera("cabecera.txt")
        
#Buscar menber en los reportes:
def buscar_member(self):
    member = input("Introduzca menber: ")
    archivo_encontrado = buscar_mem_num(self.carpeta_reporte,self.cabecera, member)
    print("Member encontrado en los siguientes archivos: ")
    print("\033[1;35m" + f"{archivo_encontrado}")

# 2. Crear un archivo (Excel) de la suma total de saldos iniciales y suma de saldos finales. 
# 3. Crear un archivo para que muestre la cantidad total de registros por cada archivo reporte
def sumaSaldos_cantRegistros(self):
    procesar_saldos(self.carpeta_reporte, self.archivos_csv, self.cabecera)

# 4. Listado de clientes con saldo final negativo
def saldo_negativos(self):
    guardar_saldos_negativos(self.carpeta_reporte, self.archivos_csv, self.cabecera)

