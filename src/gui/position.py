import sys
import tkinter as tk
from banks.credicoop.credicoop_position import credicoop
from banks.nacion.nacion_position import nacion
from banks.macro.macro_position import macro
from banks.bbva.bbva_position import bbva
from banks.pampa.pampa_position import pampa

def position(automation_var):
    try:
        selection_window = tk.Tk()
        selection_window.title('Posicion Consolidada')
        selection_window.geometry('300x200')

        bank_type = ['Banco Macro', 'Banco Nacion', 'Banco Credicoop', 'BBVA Frances', 'Banco de La Pampa', 'Ejecutar en bucle']

        bank = tk.StringVar(selection_window)
        bank.set(bank_type[0])
        tk.Label(selection_window, text='Seleccione posicion consolidada:').pack()
        tk.OptionMenu(selection_window, bank, *bank_type).pack()

        #Inicio de automatizacion 
        start_btn = tk.Button(selection_window, text='Iniciar automatizacion', command=lambda: login_and_open_vouchers(bank.get(), automation_var))
        start_btn.pack(padx=3, pady=3)

        selection_window.mainloop()
    except Exception as e:
        print('Error en ventana de Posicion Consolidada, ', {str(e)})

def login_and_open_vouchers(bank, automation_var):
    try:
        if bank == 'Banco Macro':
            macro(bank, automation_var)
        elif bank == 'Banco Nacion':
            nacion(bank, automation_var)
        elif bank == 'Banco Credicoop':
            credicoop(bank, automation_var)
        elif bank == 'BBVA Frances':
            bbva(bank, automation_var)
        elif bank == 'Banco de La Pampa':
            pampa(bank, automation_var)
        elif bank == 'Ejecutar en bucle':
            banks_and_functions = [
                ('Banco Macro', macro),
                ('Banco Nacion', nacion),
                ('Banco Credicoop', credicoop),
                ('BBVA Frances', bbva),
                ('Banco de La Pampa', pampa)
            ]

            for bank_name, bank_function in banks_and_functions:
                bank_function(bank_name)
        else:
            print('Error al seleccionar ente bancaria')
    except Exception as e:
        print('Error al seleccionar entidad bancaria para posicion consolidada, ', {str(e)})