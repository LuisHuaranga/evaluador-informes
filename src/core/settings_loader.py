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

    def put(self, clave, nueva_ruta):
        """Modifica una ruta específica en el JSON y la guarda."""
        claves = clave.split('.')
        config = self.archivo_config
        try:
            for k in claves[:-1]:
                config = config[k]
            config[claves[-1]] = nueva_ruta
            self.guardar_config()
            print(f" Ruta '{clave}' actualizada a '{nueva_ruta}'.")
        except KeyError:
            print(f" La clave '{clave}' no existe en la configuración.")

    def get(self, clave):
        """Obtiene una ruta específica, incluso si está anidada."""
        claves = clave.split('.')
        valor = self.archivo_config
        try:
            for k in claves:
                valor = valor[k]
            return valor
        except KeyError:
            return None

if __name__ == "__main__":
    config_manager = ConfigManager()

    # Modificar una ruta existente
    config_manager.put("ECC.ruta", "/nueva_XD")
    config_manager.put("PROV.ruta", "cabecera_SEXO")

    # Verificar la actualización
    ruta_prov = config_manager.get("ECC.ruta")
    print("🔹 Ruta ECC:", ruta_prov)

    print("🔹 ECC cabecera:", config_manager.get("ECC.cabecera")[0])
