from selenium.common.exceptions import NoSuchElementException
from banks.bbva.bbva_login import login_bbva
from utils.folders import *
import datetime
import time
import shutil
import os
import sys

def bbva(bank, automation_var):
    try:
        driver = login_bbva()
        client_folder = 'Scattone Daniel Oscar'
        if automation_var == 'Posicion Consolidada' or automation_var == 'E-Cheqs':
            date_folder = folders(bank, client_folder, automation_var)
        elif automation_var == 'Reporte General':
            date_folder = folders_report(client_folder, automation_var)
        else:
            print('Error al elegir tipo de automatizacion')
        #Esperas explicitas por lentitud de web y uso de pyautogui
        time.sleep(25)

        try:
            driver.execute_script('window.print();')
            time.sleep(10)
            route_base = r'D:\Clientes\default_automatizacion_bancos'
            download_dir = date_folder
            date = datetime.datetime.now()
            formatted_file = date.strftime("%d-%m-%Y")
            name_file = f'Posicion Consolidada - {client_folder} - Banco BBVA Frances - Emisión {formatted_file}.pdf'
            time.sleep(5)
            #Busco archivos en el directorio
            list_of_files = os.listdir(route_base)
            find_file = max(list_of_files, key=lambda f: os.path.getctime(os.path.join(route_base, f)))
            # Mover el archivo más reciente al directorio de destino
            shutil.move(os.path.join(route_base, find_file), download_dir)
            # Verificar que el archivo se haya movido correctamente
            rute_destiny = os.path.join(download_dir, find_file)
            new_file_path = os.path.join(download_dir, name_file)
            os.rename(rute_destiny, new_file_path)
            if os.path.exists(new_file_path):
                print("El archivo de posicion consolidada y prestamos se movió correctamente")
        except Exception as e:
            print('Error al descargar posicion consolidada y prestamos BBVA', {str(e)})

    except Exception as e:
        print('Error al descargar e-cheqs BBVA', {str(e)})
    except NoSuchElementException as nse:
        print('No se encontró un elemento necesario en la página:', str(nse))
    finally:
        if driver:
            driver.quit()
        if automation_var == 'Posicion Consolidada' or automation_var == 'E-Cheqs':
            sys.exit()
        elif automation_var == 'Reporte General':
            pass
