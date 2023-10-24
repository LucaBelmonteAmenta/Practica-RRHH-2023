import tkinter as tk
from tkinter import ttk
from views.View import View


"""
    View responsible for showing registered customers.
"""
class ShowView(tk.Tk, View):
    #-----------------------------------------------------------------------
    #        Constants
    #-----------------------------------------------------------------------
    PAD = 10
    THEADER = ("Id", "Nombre", "Apellido","Email" , "Telefono", "Work_For_Us")
    
    
    #-----------------------------------------------------------------------
    #        Constructor
    #-----------------------------------------------------------------------
    """
        @param controller Controller of this view
    """
    def __init__(self, controller):
        super().__init__()
        self.title("Show Customers")
        self.showController = controller
    
        self._make_mainFrame()
        self._make_title()
        self._make_search()
        self._show_personas()
        self.update()

    
    #-----------------------------------------------------------------------
    #        Methods
    #-----------------------------------------------------------------------


    def _make_mainFrame(self):
        self.frame_main = ttk.Frame(self)
        self.frame_main.pack(padx=self.PAD, pady=self.PAD)
        

    def _make_title(self):
        title = ttk.Label(self.frame_main, text="Busqueda de Personal", font=("Helvetica", 20))
        title.pack(padx=self.PAD, pady=self.PAD)


    def _make_search(self):
        frame_search = tk.Frame(self.frame_main)
        frame_search.pack()

        label_edad_minima = ttk.Label(frame_search, text="Edad Minima: ")
        label_edad_minima.grid(row=0, column=0)
        self.spin_edad_minima = ttk.Spinbox(frame_search, from_=18, to=100, increment=1, state="readonly")
        self.spin_edad_minima.grid(row=0, column=1)
        

        label_edad_maxima = ttk.Label(frame_search, text="Edad Maxima: ")
        label_edad_maxima.grid(row=1, column=0)
        self.spin_edad_maxima = ttk.Spinbox(frame_search,from_=18 , to=100, increment=1, state="readonly" )
        self.spin_edad_maxima.grid(row=1, column=1)

        button_competencias = ttk.Button(frame_search, text="Filtrar por competencias", command=self.showController.selectListCompetencia)
        button_competencias.grid(row=0, column=4)

        button_experiencia = ttk.Button(frame_search, text="Filtrar por Experiencia")
        button_experiencia.grid(row=1, column=4)

        button_edad = ttk.Button(frame_search, text="Filtrar por Edad", command=lambda: self.showController.cargarEdad(self.spin_edad_minima.get(), self.spin_edad_maxima.get()))
        button_edad.grid(row=2, column=4)

        label_nivel_academico = ttk.Label(frame_search, text="Nivel Academico Minimo: ")
        label_nivel_academico.grid(row=2, column=0)
        combobox_nivel_academico = ttk.Combobox(frame_search, values=("Primario","Secundario","Universitario"), state="readonly")
        combobox_nivel_academico.grid(row=2, column=1)





    def _show_personas(self):
        self.tablaPersonas = ttk.Treeview(self.frame_main, columns=self.THEADER, show='headings')
        
        self.tablaPersonas.heading('Id', text='ID')
        self.tablaPersonas.heading('Nombre', text='Nombre')
        self.tablaPersonas.heading('Apellido', text='Apellido')
        self.tablaPersonas.heading('Telefono', text='Telefono')
        self.tablaPersonas.heading('Email', text='Email')
        self.tablaPersonas.heading('Work_For_Us', text='Trabaja para la empresa')

        self.tablaPersonas.pack()

        

    def update(self):

        for item in self.tablaPersonas.get_children():
            self.tablaPersonas.delete(item)

        for persona in self.showController.lista_filtrada:
            self.tablaPersonas.insert(
                "",
                tk.END,
                values = tuple([ persona[campo] for campo in self.THEADER])
            )
        
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
        