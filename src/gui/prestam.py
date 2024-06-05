import tkinter as tk
from banks.macro.macro_prestam import macro

def prestam(automation_var):
    try:
        selection_window = tk.Tk()
        selection_window.title('Prestamos')
        selection_window.geometry('300x200')

        bank_type = ['Banco Macro']

        bank = tk.StringVar(selection_window)
        bank.set(bank_type[0])
        tk.Label(selection_window, text='Seleccione prestamo :').pack()
        tk.OptionMenu(selection_window, bank, *bank_type).pack()

        #Inicio de automatizacion 
        start_btn = tk.Button(selection_window, text='Iniciar automatizacion', command=lambda: login_and_open_vouchers(bank.get(), automation_var))
        start_btn.pack(padx=3, pady=3)

        selection_window.mainloop()
    except Exception as e:
        print('Error en ventana de Prestamos, ', {str(e)})

def login_and_open_vouchers(bank, automation_var):
    try:
        if bank == 'Banco Macro':
            macro(bank, automation_var)
        else:
            print('Error al seleccionar ente bancaria')
    except Exception as e:
        print('Error al seleccionar entidad bancaria para prestamos, ', {str(e)})