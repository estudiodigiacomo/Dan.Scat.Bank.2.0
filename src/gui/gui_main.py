import tkinter as tk
from gui.position import position
from gui.echeq import echeq
from gui.report import report
from gui.prestam import prestam

def gui():
    try:
        selection_window = tk.Tk()
        selection_window.title('Automatizacion Daniel Scattone')
        selection_window.geometry('300x200')

        bank_type = ['Posicion Consolidada', 'E-Cheqs', 'Prestamos', 'Reporte General']

        automation_var = tk.StringVar(selection_window)
        automation_var.set(bank_type[0])
        tk.Label(selection_window, text='Selecciona la automatizacion bancaria:').pack()
        tk.OptionMenu(selection_window, automation_var, *bank_type).pack()

        #Inicio de automatizacion 
        start_btn = tk.Button(selection_window, text='Continuar', command=lambda: type_automation_bank(automation_var.get()))
        start_btn.pack(padx=3, pady=3)

        selection_window.mainloop()
    except Exception as e:
        print('Error en ventana principal: ', {str(e)})

def type_automation_bank(automation_var):
    try:
        if automation_var == 'Posicion Consolidada':
            position(automation_var)
        elif automation_var == 'E-Cheqs':
            echeq(automation_var)
        elif automation_var == 'Prestamos':
            prestam(automation_var)
        elif automation_var == 'Reporte General':
            report(automation_var)
        else:
            print('Error al seleccionar tipo de automatizacion')
    except Exception as e:
        print('Error al seleccionar tipo de automatizacion: ', {str(e)})