import tkinter as tk
from tkinter import ttk
from views.View import View


class ShowCompetenciasView(tk.Tk, View):
    #-----------------------------------------------------------------------
    #        Constants
    #-----------------------------------------------------------------------
    PAD = 10
    
    #-----------------------------------------------------------------------
    #        Constructor
    #-----------------------------------------------------------------------

    def __init__(self, controller):
        super().__init__()
        self.title("Administración de competencias")
        self.geometry()
        self.resizable(width=False, height=False)

        self.homeController = controller
        
        self._make_mainFrame()
        self._make_title()
        self._make_listBox()
        self._make_buttons()
        self._make_searchEntry()
        self._make_textBox()
        self.cargarLista()
        
    
    #-----------------------------------------------------------------------
    #        Methods
    #-----------------------------------------------------------------------
    """
        Creates view's frame.
    """
    def _make_mainFrame(self):
        self.mainFrame = ttk.Frame(self)
        self.mainFrame.pack(padx=self.PAD, pady=self.PAD)

    """
        Sets view's title.
    """
    def _make_title(self):
        title = ttk.Label(self.mainFrame, text="Seleccionar las competencias", font=("Helvetica", 14))
        title.grid(row=0, column=0, columnspan=6)

        
    def _make_listBox(self):
        self.listBox = tk.Listbox(self.mainFrame, width= 20)
        self.listBox.grid(row=2, column=0, rowspan=2, columnspan=2)
        

    def _make_buttons(self):
        buttonAceptar = tk.Button(self.mainFrame, text="Crear nueva competencia", command=self.homeController.addCompetencia)
        buttonAceptar.grid(row=8, column=0, rowspan=1)

        buttonCancelar = tk.Button(self.mainFrame, text="Eliminar competencia seleccionada")
        buttonCancelar.grid(row=8, column=5, rowspan=1)


    def _make_searchEntry(self):
        self.searchEntry = tk.Entry(self.mainFrame, width=50, textvariable="Buscar competencia")
        self.searchEntry.grid(row=1, column=0, rowspan=1, columnspan=6)
        
       
    def _make_textBox(self):
        self.textBox = tk.Text(self.mainFrame, width= 20, height=10)
        self.textBox.grid(row=2, column=5, rowspan=2, columnspan=2)


    def cargarLista(self):
        competencias = self.homeController.competencias.getAllCompetencias()
        for competencia in competencias:
            self.listBox.insert(tk.END, competencia["Descripcion"])

    """
    @Overrite
    """
    def main(self):
        self.mainloop()
        
    """
    @Overrite
    """
    def close(self):
        return

