import pyautogui
import datetime
import time
import os
import shutil
import sys
from utils.folders import *
from banks.macro.login_macro import login_macro

def macro(bank, automation_var):
    try:
        driver = login_macro()
        client_folder = 'Scattone Daniel Oscar'
        date_folder = folders(bank, client_folder, automation_var)

        def click_btn(img):
            try:
                x, y = pyautogui.locateCenterOnScreen(img, confidence=0.5)
                pyautogui.click(x, y)
                print(f"Click realizado en el botón {img}.")
            except FileNotFoundError:
                print(f"Archivo '{img}' no encontrado.")
            except Exception as e:
                print(f"Se produjo un error al buscar y hacer click en el botón {img}: {str(e)}")

        route_base = r'D:\Clientes\default_automatizacion_bancos'

        # Recorro imagenes y ejecuto funcion btn_click
        image_names = ['btn_pdf.png', 'btn_txt.png', 'btn_xls.png']
        dir_path = r'C:\Daniel Scattone - Automatizacion\src\macro\img'

        for image_name in image_names:
            path_btns = os.path.join(dir_path, image_name)
            click_btn(path_btns)
            time.sleep(7)

            #Obtengo lista de archivos
            list_of_files = os.listdir(route_base)
            extension = None

            # Iterar sobre los archivos descargados
            for downloaded_file in list_of_files:
                # Determinar la extensión del archivo descargado
                if downloaded_file.endswith('.pdf'):
                    extension = 'pdf'
                elif downloaded_file.endswith('.txt'):
                    extension = 'txt'
                elif downloaded_file.endswith('.xls'):
                    extension = 'xls'
                else:
                    continue 

            if not extension:
                print(f"No se encontró una extensión válida para los archivos descargados de {image_name}.")
                continue

            
            date = datetime.datetime.now()
            formatted_file = date.strftime("%d-%m-%Y")
            name_file = f'Posición consolidada - {client_folder} - Banco Macro - Emisión {formatted_file}.{extension}'

            try:
                find_file = max(list_of_files, key=lambda f: os.path.getctime(os.path.join(route_base, f)))
                # Mover el archivo más reciente al directorio de destino
                shutil.move(os.path.join(route_base, find_file), date_folder)

                # Verificar que el archivo se haya movido correctamente
                rute_destiny = os.path.join(date_folder, find_file)
                new_file_path = os.path.join(date_folder, name_file)
                os.rename(rute_destiny, new_file_path)
                if os.path.exists(new_file_path):
                    print("El archivo se movió correctamente")
            except ValueError:
                pass
        
        dir_path_exit = r'C:\Daniel Scattone - Automatizacion\src\macro\img\exit.png'
        x, y = pyautogui.locateCenterOnScreen(dir_path_exit, confidence=0.5)
        pyautogui.click(x, y)
        print(f"Click realizado en el botón {dir_path_exit}.")
        
        driver.quit()
    except Exception as e:
        print('Error al procesar automatizacion:', {str(e)})
    finally:
        if driver:
            driver.quit()
        if automation_var == 'Posicion Consolidada' or automation_var == 'E-Cheqs':
            sys.exit()
        elif automation_var == 'Reporte General':
            pass


def macro_report(bank, automation_var):
    try:
        driver = login_macro()
        client_folder = 'Scattone Daniel Oscar'
        date_folder = folders_report(client_folder, automation_var)

        dir_path_pdf = r'C:\Daniel Scattone - Automatizacion\src\macro\img\btn_pdf.png'
        x, y = pyautogui.locateCenterOnScreen(dir_path_pdf, confidence=0.5)
        pyautogui.click(x, y)
        print(f"Click realizado en el botón {dir_path_pdf}.")
        time.sleep(10)
        route_base = r'D:\Clientes\default_automatizacion_bancos'

        #Obtengo lista de archivos
        list_of_files = os.listdir(route_base)
        name_file = f'Posición consolidada - {client_folder} - Banco Macro - Emisión.pdf'
        try:
            find_file = max(list_of_files, key=lambda f: os.path.getctime(os.path.join(route_base, f)))
            # Mover el archivo más reciente al directorio de destino
            shutil.move(os.path.join(route_base, find_file), date_folder)

            # Verificar que el archivo se haya movido correctamente
            rute_destiny = os.path.join(date_folder, find_file)
            new_file_path = os.path.join(date_folder, name_file)
            os.rename(rute_destiny, new_file_path)
            if os.path.exists(new_file_path):
                print("El archivo se movió correctamente")
        except ValueError:
            pass

        dir_path_exit = r'C:\Daniel Scattone - Automatizacion\src\macro\img\exit.png'
        x, y = pyautogui.locateCenterOnScreen(dir_path_exit, confidence=0.5)
        pyautogui.click(x, y)
        print(f"Click realizado en el botón {dir_path_exit}.")

        driver.quit()
    except Exception as e:
        print('Error al procesar automatizacion:', {str(e)})
    finally:
        if driver:
            driver.quit()
        if automation_var == 'Posicion Consolidada' or automation_var == 'E-Cheqs':
            sys.exit()
        elif automation_var == 'Reporte General':
            pass
