import tkinter as tk
from tkinter import ttk, filedialog
from ui.config.config import FONT_CONFIG, FONT_CONFIG_TEXT_ENTRY
from src.core.settings_loader import ConfigManager

class PestanaPlantilla:
    def __init__(self, pestana, opciones):
        self.pestana = pestana
        self.opcion = tk.IntVar(value=-1)
        self.caja_texto = None
        self.button_ejecutar = None
        self.funcion_seleccionada = None
        self.radiobuttons = [] 
        self.ruta_carpeta = tk.StringVar()
        self.parametros = None
        self.opciones = opciones
        self.crear_contenido_pestana(opciones["opciones"])

    def crear_contenido_pestana(self, opciones):
        self.crear_grupo_carpetas()        
        self.crear_grupo_opciones(opciones)
        self.estado_opciones("disabled")
        self.estado_button_ejecutar('disable')

    def crear_grupo_carpetas(self):
        grupo_carpeta = ttk.LabelFrame(self.pestana, text='Carpeta Origen', padding=(5, 5))
        grupo_carpeta.pack(padx=10, pady=10, fill="both", anchor='w')

        self.caja_texto = ttk.Entry(grupo_carpeta, width=55, textvariable=self.ruta_carpeta, font=FONT_CONFIG_TEXT_ENTRY)
        self.caja_texto.grid(row=0, column=0, padx=10, pady=10)
        self.caja_texto.bind("<KeyRelease>", self.cambio_texto_ruta)

        boton_carpeta = ttk.Button(grupo_carpeta, text='Buscar...', command=self.seleccionar_carpeta, style="TButton")
        boton_carpeta.grid(row=0, column=1)

    def crear_grupo_opciones(self, opciones):
        grupo_opciones = ttk.LabelFrame(self.pestana, text='Opciones', padding=(5, 5))
        grupo_opciones.pack(padx=10, pady=10, fill="both", anchor='w')

        for index, (texto, funcion) in enumerate(opciones):
            radio = tk.Radiobutton(grupo_opciones, text=texto, variable=self.opcion, command=lambda func=funcion: self.seleccionar_funcion(func), value=index, font=FONT_CONFIG)
            radio.grid(row=index, column=0, sticky="w", padx=5, pady=2)
            self.radiobuttons.append(radio)
            
        self.button_ejecutar = ttk.Button(grupo_opciones, text='Ejecutar', command=self.ejecutar_opcion_seleccionada, style="TButton")    
        self.button_ejecutar.grid(row=len(opciones), column=0, sticky="w", padx=10, pady=2)

    def seleccionar_carpeta(self):
        ruta = filedialog.askdirectory(title="Seleccionar una carpeta")
        if ruta:
            self.ruta_carpeta.set(ruta)
            self.caja_texto.delete(0, tk.END)
            self.caja_texto.insert(0, ruta)
            print(f"Carpeta seleccionada: {ruta}")
            ConfigManager().put(self.opciones["archivo"] + '.ruta', ruta)
            self.estado_opciones("normal")

    def seleccionar_funcion(self, funcion):
        self.funcion_seleccionada = funcion      
        self.estado_button_ejecutar('normal')

    def ejecutar_opcion_seleccionada(self):
        ruta = self.caja_texto.get()
        ConfigManager().put(self.opciones["archivo"] + '.ruta', ruta)
        if self.funcion_seleccionada:
            self.funcion_seleccionada()

    def estado_opciones(self, state):
        for radio in self.radiobuttons:
            radio.config(state=state)

    def estado_button_ejecutar(self, state):
        self.button_ejecutar.config(state=state)

    def cambio_texto_ruta(self, event):
        ruta = event.widget.get()
        if ruta:
            self.estado_opciones("normal")
        else:
            self.estado_opciones("disabled")
            self.opcion.set(-1)
            self.estado_button_ejecutar('disable')
