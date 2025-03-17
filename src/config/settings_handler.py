import json
from pathlib import Path

class ConfigManager:
    def __init__(self, file_name="settings.json"):

        self.ruta_config = Path(__file__).parent / file_name

        self.archivo_config = self._cargar_config()

        if not self.archivo_config:
            self.archivo_config = {
                "rutaECC": "/data1",
                "rutaPROV": "/data222"
            }
            self.guardar_config()

    def _cargar_config(self):
        """Carga el archivo JSON y lo almacena en memoria."""
        if not self.ruta_config.exists():
            print(f"El archivo {self.ruta_config} no existe. Creando uno nuevo...")
            return {}

        try:
            return json.loads(self.ruta_config.read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            print(f"⚠️ Error al leer JSON: {e}")
            return {}

    def guardar_config(self):
        """Guarda la configuración en el archivo JSON."""
        self.ruta_config.write_text(
            json.dumps(self.archivo_config, indent=4, ensure_ascii=False), encoding="utf-8")

    def modificar_ruta(self, clave, nueva_ruta):
        """Modifica una ruta específica en el JSON y la guarda."""
        if clave in self.archivo_config:
            self.archivo_config[clave] = nueva_ruta
            self.guardar_config()
            print(f" Ruta '{clave}' actualizada a '{nueva_ruta}'.")
        else:
            print(f" La clave '{clave}' no existe en la configuración.")

    def obtener_ruta(self, clave):
        """Obtiene una ruta específica."""
        return self.archivo_config.get(clave, None)


if __name__ == "__main__":
    config_manager = ConfigManager()

    print("🔹 Configuración actual:", config_manager.archivo_config)

    # Modificar una ruta existente
    config_manager.modificar_ruta("rutaECC", "/nueva_ruta_ecc")

    # Verificar la actualización
    print("🔹 Configuración después de la actualización:", config_manager.archivo_config)

    # Obtener una ruta específica
    ruta_prov = config_manager.obtener_ruta("rutaPROV")
    print("🔹 Ruta PROV:", ruta_prov)
    
    print("🔹 Ruta Luis:", config_manager.obtener_ruta("luisi"))
