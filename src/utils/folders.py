import os
import datetime

def folders(type_bank, client_folder, automation_var):
    #Verifico existencia de las carpetas necesarias
    try:
        date = datetime.datetime.now()
        formatted_folder = date.strftime("%d-%m-%Y %H.%M.%S")

        #Condicional creacion de carpeta segun tipo de proceso
        if automation_var == 'Posicion Consolidada':
            name_folder_process = 'Posicion Consolidada'
        elif automation_var == 'E-Cheqs':
            name_folder_process = 'E-Cheqs'
        elif automation_var == 'Prestamos':
            name_folder_process = 'Prestamos'

        base_dir = r'D:\Clientes'
        client_dir = os.path.join(base_dir, client_folder)
        automatitation = os.path.join(client_dir, 'Automatizaciones')
        banks = os.path.join(automatitation, 'Bancos')
        bank_type = os.path.join(banks, type_bank)
        position_cons = os.path.join(bank_type, name_folder_process)
        date_folder = os.path.join(position_cons, formatted_folder)

        if not os.path.exists(base_dir):
            os.makedirs(base_dir)
            print(f'Creada la carpeta Clientes en el directorio {base_dir}')
        if not os.path.exists(client_dir):
            os.makedirs(client_dir)
            print(f'Creada la carpeta {client_folder} en el directorio {client_dir}')
        if not os.path.exists(automatitation):
            os.makedirs(automatitation)
            print(f'Creada la carpeta Automatizacion en el directorio {automatitation}')
        if not os.path.exists(banks):
            os.makedirs(banks)
            print(f'Creada la carpeta Banco en el directorio {banks}')
        if not os.path.exists(bank_type):
            os.makedirs(bank_type)
            print(f'Creada la carpeta {type_bank} en el directorio {bank_type}')
        if not os.path.exists(position_cons):
            os.makedirs(position_cons)
            print(f'Creada la carpeta {type_bank} en el directorio {position_cons}')
        if not os.path.exists(date_folder):
            os.makedirs(date_folder)
            print(f'Creada la carpeta {date_folder}')
    
        return date_folder
    except Exception as e:
        print('Error al verificar o crear carpetas de directorio', str(e))


def folders_report(client_folder, automation_var):
    #Verifico existencia de las carpetas necesarias
    try:
        base_dir = r'D:\Clientes'
        client_dir = os.path.join(base_dir, client_folder)
        automatitation = os.path.join(client_dir, 'Automatizaciones')
        date_folder = os.path.join(automatitation, automation_var)

        if not os.path.exists(base_dir):
            os.makedirs(base_dir)
            print(f'Creada la carpeta Clientes en el directorio {base_dir}')
        if not os.path.exists(client_dir):
            os.makedirs(client_dir)
            print(f'Creada la carpeta {client_folder} en el directorio {client_dir}')
        if not os.path.exists(automatitation):
            os.makedirs(automatitation)
            print(f'Creada la carpeta Automatizacion en el directorio {automatitation}')
        if not os.path.exists(date_folder):
            os.makedirs(date_folder)
            print(f'Creada la carpeta Banco en el directorio {date_folder}')
        return date_folder
    except Exception as e:
        print('Error al verificar o crear carpetas de directorio', str(e))