from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui
import datetime
import time
import os
import shutil
import sys
from utils.folders import *
from banks.macro.login_macro_person import login_macro

def macro(bank, automation_var):
    try:
        driver = login_macro()
        client_folder = 'Scattone Daniel Oscar'
        if automation_var == 'Posicion Consolidada' or automation_var == 'E-Cheqs':
            date_folder = folders(bank, client_folder, automation_var)
        elif automation_var == 'Reporte General':
            date_folder = folders_report(client_folder, automation_var)
        else:
            print('Error al elegir tipo de automatizacion')

        time.sleep(5)
        driver.execute_script("window.scrollBy(0, 150);")
        time.sleep(5)

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
        image_names = ['btn_prestamos.png', 'prestamo_click.png']
        dir_path = r'C:\Daniel Scattone - Automatizacion\src\macro\img'

        for image_name in image_names:
            path_btns = os.path.join(dir_path, image_name)
            click_btn(path_btns)
            time.sleep(7)

        # Inyectar CSS para ocultar elementos que no deben imprimirse
        css_to_hide_elements = """
        var style = document.createElement('style');
        style.id = 'hide-elements-style';
        style.innerHTML = `
            #templateRow0, 
            #templateRow1, 
            .rightContent.col.s3.horizontal-separator.no-padding-right {
                display: none !important;
            }
        `;
        document.head.appendChild(style);
        """
        driver.execute_script(css_to_hide_elements)
        time.sleep(2)

        try:
            time.sleep(5)
            driver.execute_script('window.print();')
            time.sleep(10)
            route_base = r'D:\Clientes\default_automatizacion_bancos'
            
            date = datetime.datetime.now()
            formatted_file = date.strftime("%d-%m-%Y")
            name_file = f'Préstamos - {client_folder} - Banco Macro - Emisión {formatted_file}.pdf'
            time.sleep(5)
            #Busco archivos en el directorio
            list_of_files = os.listdir(route_base)
            find_file = max(list_of_files, key=lambda f: os.path.getctime(os.path.join(route_base, f)))
            # Mover el archivo más reciente al directorio de destino
            shutil.move(os.path.join(route_base, find_file), date_folder)
            # Verificar que el archivo se haya movido correctamente
            rute_destiny = os.path.join(date_folder, find_file)
            new_file_path = os.path.join(date_folder, name_file)
            os.rename(rute_destiny, new_file_path)
            if os.path.exists(new_file_path):
                print("El archivo de prestamos")
        except Exception as e:
            print('Error al descargar prestamos Macro', {str(e)})


        # Eliminar el estilo inyectado
        remove_css_to_hide_elements = """
        var styleElement = document.getElementById('hide-elements-style');
        if (styleElement) {
            styleElement.parentNode.removeChild(styleElement);
        }
        """
        driver.execute_script(remove_css_to_hide_elements)

        time.sleep(5)
        driver.execute_script("window.scrollBy(150, 0);")
        time.sleep(5)

        dir_path_exit = r'C:\Daniel Scattone - Automatizacion\src\macro\img\exit_persona.png'
        x, y = pyautogui.locateCenterOnScreen(dir_path_exit, confidence=0.5)
        pyautogui.click(x, y)
        print(f"Click realizado en el botón {dir_path_exit}.")

        time.sleep(20)
        
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
