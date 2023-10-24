import tkinter as tk
from tkinter import ttk
from views.View import View


"""
    View associated with HomeController. It will be responsible for program's 
    main screen view.
"""
class SelectListsCompetenciasView(tk.Tk, View):
    #-----------------------------------------------------------------------
    #        Constants
    #-----------------------------------------------------------------------
    PAD = 10

    
    
    #-----------------------------------------------------------------------
    #        Constructor
    #-----------------------------------------------------------------------
    """
        @param controller Controller of this view
    """
    def __init__(self, controller):
        super().__init__()
        self.title("Elegir competencias")
        self.geometry()
        self.resizable(width=False, height=False)

        self.homeController = controller

        self.competencias = self.homeController.getAllCompetencias()
        self.competencias_seleccionadas = []
        
        self._make_mainFrame()
        self._make_title()
        self._make_listBoxes()
        self._make_buttons()
        self._make_searchEntry()
        
    
    #-----------------------------------------------------------------------
    #        Methods
    #-----------------------------------------------------------------------

    def _make_mainFrame(self):
        self.mainFrame = ttk.Frame(self)
        self.mainFrame.pack(padx=self.PAD, pady=self.PAD)

    def _make_title(self):
        title = ttk.Label(self.mainFrame, text="Seleccionar las competencias", font=("Helvetica", 14)).grid(row=0, column=1)

        
    def _make_listBoxes(self):
        self.listBox1 = tk.Listbox(self.mainFrame, selectmode=tk.MULTIPLE)
        self.listBox1.grid(row=2, column=0, rowspan=5)
        self.listBox2 = tk.Listbox(self.mainFrame, selectmode=tk.MULTIPLE)
        self.listBox2.grid(row=2, column=2, rowspan=5)

        for competencia in self.competencias:
            self.listBox1.insert(tk.END, competencia["Descripcion"])


    def agregarCompetencia(self):
        selected_checkboxs = self.listBox1.curselection() 
        for selected_checkbox in selected_checkboxs[::-1]: 

            for competencia in self.competencias:
                if (competencia["Descripcion"] == self.listBox1.get(selected_checkbox)):
                    self.competencias_seleccionadas.append(competencia)

            self.listBox2.insert(tk.END, self.listBox1.get(selected_checkbox))
            self.listBox1.delete(selected_checkbox)


    def removerCompetencia(self):
        selected_checkboxs = self.listBox2.curselection() 
        for selected_checkbox in selected_checkboxs[::-1]: 

            for competencia in self.competencias:
                if (competencia["Descripcion"] == self.listBox2.get(selected_checkbox)):
                    self.competencias_seleccionadas.remove(competencia)

            self.listBox1.insert(tk.END, self.listBox2.get(selected_checkbox))
            self.listBox2.delete(selected_checkbox)
            

    def _make_buttons(self):
        buttonAdd = tk.Button(self.mainFrame, text="Agregar  ->", command=self.agregarCompetencia).grid(row=3, column=1, rowspan=1)
        buttonRemove = tk.Button(self.mainFrame, text="<- Remover", command=self.removerCompetencia).grid(row=4, column=1, rowspan=1)

        buttonAceptar = tk.Button(self.mainFrame, text="Aceptar", command=self.aceptar ).grid(row=8, column=0, rowspan=1)
        buttonCancelar = tk.Button(self.mainFrame, text="Cancelar", command=self.close).grid(row=8, column=2, rowspan=1)


    def _make_searchEntry(self):
        self.searchEntry = tk.Entry(self.mainFrame, textvariable="Buscar competencia").grid(row=1, column=0, rowspan=1)


    def aceptar(self):
        self.homeController.cargarCompetenciasElegidas(self.competencias_seleccionadas)
        self.close()


    def main(self):
        self.mainloop()
        
    """
    @Overrite
    """
    def close(self):
        self.destroy()

