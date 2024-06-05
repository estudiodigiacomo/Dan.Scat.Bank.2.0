from banks.report.report_general import report_general
import tkinter as tk

def report(automation_var):
    try:
        selection_window = tk.Tk()
        selection_window.title('Reporte general Daniel Scattone')
        selection_window.geometry('300x200')
        #Inicio de automatizacion 
        start_btn = tk.Button(selection_window, text='Continuar', command=lambda: report_general(automation_var))
        start_btn.pack(padx=3, pady=3)
        
    except Exception as e:
        print('Error al iniciar automatizacion de reporte: ', {str(e)})
