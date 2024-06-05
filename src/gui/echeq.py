import tkinter as tk
from banks.bbva.bbva_echeq import bbva

def echeq(automation_var):
    try:
        selection_window = tk.Tk()
        selection_window.title('E-Cheqs')
        selection_window.geometry('300x200')

        bank_type = ['BBVA Frances']

        bank = tk.StringVar(selection_window)
        bank.set(bank_type[0])
        tk.Label(selection_window, text='Seleccione e_cheq:').pack()
        tk.OptionMenu(selection_window, bank, *bank_type).pack()

        #Inicio de automatizacion 
        start_btn = tk.Button(selection_window, text='Iniciar automatizacion', command=lambda: login_and_open_vouchers(bank.get(), automation_var))
        start_btn.pack(padx=3, pady=3)

        selection_window.mainloop()
    except Exception as e:
        print('Error en ventana E-Cheq, ', {str(e)})

def login_and_open_vouchers(bank, automation_var):
    try:
        bbva(bank, automation_var)
    except Exception as e:
        print('Error al seleccionar entidad bancaria en E_Cheqs, ', {str(e)})