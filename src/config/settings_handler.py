import json
from pathlib import Path

class ConfigManager:
    def __init__(self, config_file="config.json"):
        self.config_file = Path(config_file)
        self.config = self._load_config()

    def _load_config(self):
        """Carga el archivo JSON de configuraciones."""
        if not self.config_file.exists():
            raise FileNotFoundError(f"El archivo {self.config_file} no existe.")
        
        with open(self.config_file, "r") as file:
            return json.load(file)

    def get(self, key, default=None):
        """Obtiene un valor de la configuración."""
        return self.config.get(key, default)

    def set(self, key, value):
        """Establece un valor en la configuración."""
        self.config[key] = value
        self._save_config()

    def _save_config(self):
        """Guarda los cambios en el archivo JSON."""
        with open(self.config_file, "w") as file:
            json.dump(self.config, file, indent=4)

    def __str__(self):
        """Muestra la configuración actual de forma legible."""
        return json.dumps(self.config, indent=4)


# Ejemplo de uso
if __name__ == "__main__":
    try:
        manager = ConfigManager()

        # Obtener un valor
        print("Idioma actual:", manager.get("rutaECC"))

        # Cambiar un valor
        manager.set("rutaECC", "/OHSSII")
        print("Idioma actualizado:", manager.get("rutaECC"))

        # Mostrar toda la configuración
        print("\nConfiguración completa:")
        print(manager)
    except Exception as e:
        print(f"Error: {e}")