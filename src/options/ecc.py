from services.ecc_service import *
from src.core.settings_loader import ConfigManager


carpeta_reporte = carpeta_reporte
archivos_csv = lista_reportes(carpeta_reporte)
cabecera = leer_cabecera("cabecera.txt")
        
class OpcionesECC:
        
    def __init__(self):
        self.carpeta_reporte = ConfigManager().get_ruta('rutaECC')
        self.archivos_csv = archivos_csv
        self.cabecera = cabecera
               
    #Buscar menber en los reportes:
    def buscar_member(self):
        member = input("Introduzca menber: ")
        archivo_encontrado = buscar_mem_num(self.carpeta_reporte,self.cabecera, member)
        print("Member encontrado en los siguientes archivos: ")   

    # 2. Crear un archivo (Excel) de la suma total de saldos iniciales y suma de saldos finales. 
    # 3. Crear un archivo para que muestre la cantidad total de registros por cada archivo reporte
    def sumaSaldos_cantRegistros(self):
        procesar_saldos(self.carpeta_reporte, self.archivos_csv, self.cabecera)

    # 4. Listado de clientes con saldo final negativo
    def saldo_negativos(self):
        guardar_saldos_negativos(self.carpeta_reporte, self.archivos_csv, self.cabecera)

