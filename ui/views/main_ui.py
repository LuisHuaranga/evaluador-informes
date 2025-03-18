import tkinter as tk
from ui.views.pestana_plantilla import PestanaPlantilla
from tkinter import ttk
from ui.config.config import *
from src.core.settings import *

class MainUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title(WINDOW_TITLE)
        self.geometry(WINDOW_SIZE)
        self.resizable(False, False)

        self.style = ttk.Style(self)
        self.style.configure('TButton', font=FONT_CONFIG)
        self.style.configure('TNotebook.Tab', font=FONT_CONFIG)
                
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(expand=True, fill='both')
                        
        self.crear_pestanas()        
        
    def crear_pestanas(self):
        self.pestana1 = ttk.Frame(self.notebook)
        self.pestana2 = ttk.Frame(self.notebook)
        
        self.notebook.add(self.pestana1, text='Estado de Cuenta')
        self.notebook.add(self.pestana2, text='Proviciones Mensuales')
        
        PestanaPlantilla(self.pestana1,OPTIONS_ECC)
        PestanaPlantilla(self.pestana2,OPTIONS_PROV)


if __name__ == '__main__':
    app = MainUI()
    app.mainloop()