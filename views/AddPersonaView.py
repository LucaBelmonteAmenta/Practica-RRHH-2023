import tkinter as tk
from tkinter import ttk
from views.View import View
from tkcalendar import DateEntry



"""
    View responsible for adding new customers.
"""
class AddPersonaView(tk.Tk, View):
    #-----------------------------------------------------------------------
    #        Constants
    #-----------------------------------------------------------------------
    PAD = 10
    FIELDS = [
        "Nombre", "Apellido", "Direccion", "Telefono", "Email"
    ]
    
    
    #-----------------------------------------------------------------------
    #        Constructor
    #-----------------------------------------------------------------------


    def __init__(self, controller):
        super().__init__()
        self.competencias = []
        self.addController = controller

    #-----------------------------------------------------------------------
    #        Methods
    #-----------------------------------------------------------------------
 
    def _make_mainFrame(self):
        self.frame_main = tk.Frame(self)
        self.frame_main.pack()
    
 
    def _make_title(self):
        title = ttk.Label(self.frame_main, text="Cargar nuevo registro", font=("Helvetica", 20))
        title.pack(padx=self.PAD, pady=self.PAD)
    

    def _make_fields(self):
        frame_fields = tk.Frame(self.frame_main)
        frame_fields.pack()
        self.fields = []
        
        i = 0
        for field in self.FIELDS:
            # Show headers
            f = ttk.Label(frame_fields, text=field)
            f.grid(row=i, column=0)
            
            # Show fields
            e = ttk.Entry(frame_fields, width=25)
            e.grid(row=i, column=1)
            self.fields.append(e)
            
            i += 1


        label_sexo = ttk.Label(frame_fields, text="Sexo")
        label_sexo.grid(row=i, column=0)
        self.comboBox_sexo = ttk.Combobox(frame_fields, width=23, state="readonly", values=["Masculino", "Femenino", "Otro"])
        self.comboBox_sexo.grid(row=i, column=1)

        label_fecha = ttk.Label(frame_fields, text="Fecha de nacimiento")
        label_fecha.grid(row=i+1, column=0)
        self.cal=DateEntry(frame_fields, selectmode='day', width=23, date_pattern='MM/dd/yyyy')
        self.cal.grid(row=i+1,column=1)

        self.checkbox_value = tk.BooleanVar(self)
        checkbox_work = ttk.Checkbutton(frame_fields, text="Trabaja para la empresa", variable=self.checkbox_value)
        checkbox_work.grid(row=i+2, column=0, columnspan=2)
        self.checkbox_value.set(True)
            
        frame_buttons = tk.Frame(self.frame_main)
        frame_buttons.pack()

        btn_Cancelar = ttk.Button(frame_buttons, text="Cancelar", command=self.destroy)
        btn_Cancelar.pack(side="left")

        btn_registrar = ttk.Button(frame_buttons, text="Registrar", command=lambda:self.addPersona())
        btn_registrar.pack()

   
    def _make_addEducation(self):
        frame_education = tk.Frame(self.frame_main)
        frame_education.pack(side="left")

        self.listBox_educacion = tk.Listbox(frame_education, width = 20)
        self.listBox_educacion.pack()

        btn_educacion = ttk.Button(frame_education, text="Agregar Educación", command=lambda:self.addEducacion())
        btn_educacion.pack()


    def _make_addCompetencia(self):
        frame_competencia = tk.Frame(self.frame_main)
        frame_competencia.pack(side="left")

        self.listBox_competencia = tk.Listbox(frame_competencia, width = 20)
        self.listBox_competencia.pack()

        btn_competencia = ttk.Button(frame_competencia, text="Agregar Competencias", command=lambda:self.addCompetencias())
        btn_competencia.pack()

    
    def _make_addExperienciaLaboral(self):
        frame_laboral = tk.Frame(self.frame_main)
        frame_laboral.pack(side="left")

        self.listBox_laboral = tk.Listbox(frame_laboral, width = 20)
        self.listBox_laboral.pack()

        btn_laboral = ttk.Button(frame_laboral, text="Agregar Experiencia Laboral", command=lambda:self.addExperienciaLaboral())
        btn_laboral.pack()


    def addEducacion(self):
        pass

        
    def addExperienciaLaboral(self):
        
        pass

    def addCompetencias(self):
        self.addController.selectListCompetencia()
        
    def cargarCompetenciasElegidas(self, competencias_seleccionadas):
        self.competencias = competencias_seleccionadas
        self.listBox_competencia.delete(0,tk.END)
        for competencia in competencias_seleccionadas:
            self.listBox_competencia.insert(tk.END, competencia["Descripcion"])

    def addPersona(self):

        persona = {}

        contador_campo = 0
        for entry in self.fields:
            persona[self.FIELDS[contador_campo]] = entry.get()
            contador_campo+=1

        persona["Work_For_Us"] = (lambda x : "True" if x else "False")(self.checkbox_value.get())
        persona["Fecha_nacimiento"]=self.cal.get_date()
        persona["Sexo"]=self.comboBox_sexo.get()

        self.addController.btn_add_persona(persona)
        self.addController.btn_add_competencias(self.competencias)
        
        

    def main(self):
        self._make_mainFrame()
        self._make_title()
        self._make_fields()
        self._make_addEducation()
        self._make_addExperienciaLaboral()
        self._make_addCompetencia()
        
        self.mainloop()
    
    """
    @Overrite
    """
    def close(self):
        self.destroy()
        