from opciones import buacar_member, sumaSaldos_cantRegistros, saldo_negativos
import time
import itertools
import os

# Función para mostrar la animación de cargando
def animacion_cargando(mensaje, tarea):
    spinner = itertools.cycle(["|", "/", "-", "\\"])
    print(f"{mensaje} ", end="", flush=True)
    terminado = False

    # Crear un hilo o utilizar un enfoque no bloqueante para mostrar la animación mientras se ejecuta la tarea
    def ejecutar_tarea():
        nonlocal terminado
        tarea()
        terminado = True

    ejecutar_tarea()
    while not terminado:
        print(next(spinner), end="\r", flush=True)
        time.sleep(0.1)
    print("\033[1;32m Tarea completada.\n")

# Función para mostrar el menú principal con un estilo mejorado
def menu_principal():
    opciones = [
        {"nombre": "Buscar menber en los reportes", "funcion": lambda: animacion_cargando("Procesando...\n", buacar_member)},
        {"nombre": "Crear archivo de suma de saldos y registros", "funcion": lambda: animacion_cargando("Procesando...", sumaSaldos_cantRegistros)},
        {"nombre": "Listado de clientes con saldo final negativo", "funcion": lambda: animacion_cargando("Procesando...", saldo_negativos)},
        {"nombre": "Salir", "funcion": lambda: print("¡Hasta luego!")}
    ]

    while True:
        os.system("cls" if os.name == "nt" else "clear")
        
        # Cabecera del sistema
        print("\033[1;32m" + "=" * 50)
        print("\033[1;32m" + "     Mini Sistema Operativo - Menú Principal     ")
        print("\033[1;32m" + "=" * 50)
        print("\033[1;37m")  # Restablecer color a blanco
        
        # Opciones del menú
        for i, opcion in enumerate(opciones, start=1):
            print(f"\033[1;34m[{i}]\033[1;37m {opcion['nombre']}")

        print("\n\033[1;35m" + "=" * 50)
        print("\033[1;35m" + " Por favor, seleccione una opción de arriba. ")
        print("\033[1;35m" + "=" * 50)

        try:
            opcion = int(input("\033[1;36mSeleccione una opción: \033[1;37m"))
            if 1 <= opcion <= len(opciones):
                if opcion == len(opciones):  # Si selecciona la última opción (Salir)
                    opciones[opcion - 1]["funcion"]()
                    break
                opciones[opcion - 1]["funcion"]()
                input("\n\033[1;33mPresione Enter para regresar al menú principal...\033[1;37m")
            else:
                print("\033[1;31mOpción no válida. Intente de nuevo.\033[1;37m")
        except ValueError:
            print("\033[1;31mEntrada inválida. Por favor, ingrese un número.\033[1;37m")

if __name__ == "__main__":
    menu_principal()
