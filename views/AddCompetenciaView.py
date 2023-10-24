import tkinter as tk
from tkinter import ttk
from views.View import View


class AddCompetenciaView(tk.Tk, View):
    #-----------------------------------------------------------------------
    #        Constants
    #-----------------------------------------------------------------------
    PAD = 10
    DICIPLINAS = ["Ingeniería Informatica", "Hijiene y Seguridad laboral"]
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
        self._make_buttons()
        self._make_combobox()
        self._make_textBox()
        
    
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
        title = ttk.Label(self.mainFrame, text="Crean nueva competencia", font=("Helvetica", 14))
        title.grid(row=0, column=0, columnspan=6)

        
    def _make_buttons(self):
        buttonAceptar = tk.Button(self.mainFrame, text="Aceptar", command=lambda: self.homeController.btn_add(self.textBox.get(1.0, "end-1c"), self.comboBox_diciplina.get()))
        buttonAceptar.grid(row=8, column=0, rowspan=1)

        buttonCancelar = tk.Button(self.mainFrame, text="Cancelar", command=self.close)
        buttonCancelar.grid(row=8, column=1, rowspan=1)


    def _make_combobox(self):
        self.comboBox_diciplina = ttk.Combobox(self.mainFrame, width=23, state="readonly", values=self.DICIPLINAS)
        self.comboBox_diciplina.grid(row=1, column=0, rowspan=1, columnspan=1)
        
       
    def _make_textBox(self):
        self.textBox = tk.Text(self.mainFrame, width= 20, height=10)
        self.textBox.grid(row=2, column=0, rowspan=2, columnspan=2)
    

    """
    @Overrite
    """
    def main(self):
        self.mainloop()
        
    """
    @Overrite
    """
    def close(self):
        self.destroy()


