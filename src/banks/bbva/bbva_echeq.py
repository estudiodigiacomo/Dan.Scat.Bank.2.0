from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from banks.bbva.bbva_login import login_bbva
from utils.folders import *
import pyautogui
import datetime
import shutil
import os
import time
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
        # Esperar carga de pagina
        WebDriverWait(driver, 20).until(
            lambda d: d.execute_script('return document.readyState') == 'complete'
        )
        
        # Carga de body
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, 'body'))
        )
        #Esperas explicitas por lentitud de web y uso de pyautogui
        time.sleep(10)
        driver.execute_script("window.scrollBy(0, 250);")
        time.sleep(5)
        def click_btn(img):
            try:
                x, y = pyautogui.locateCenterOnScreen(img, confidence=0.5)
                pyautogui.click(x, y)
            except Exception as e:
                print('Error en funcion click_btn', {str(e)})
                
        # Recorro imagenes y ejecuto funcion btn_click
        image_names = ['pago_btn.png', 'e_cheq_btn.png', 'bandeja_de_salida.png']
        dir_path = r'C:\Daniel Scattone - Automatizacion\src\bbva\img'

        for image_name in image_names:
            path_btns = os.path.join(dir_path, image_name)
            click_btn(path_btns)
            time.sleep(5)
        #Esperas explicitas por lentitud de web y uso de pyautogui
        time.sleep(50)

        #Imprimo la pagina como pdf
        driver.execute_script('window.print();')
        time.sleep(5)
        try:
            date = datetime.datetime.now()
            formatted_file = date.strftime("%d-%m-%Y")
            name_file = f'E-Cheqs - {client_folder} - Banco BBVA Frances - Emisión {formatted_file}.pdf'
            route_base = r'D:\Clientes\default_automatizacion_bancos' 
            download_dir = date_folder
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
                print("El archivo de e-checks BBVA se movió correctamente")
        except Exception as e:
            print('Error al mover archivo de e-checks BBVA')

    except Exception as e:
        print('Error al descargar e-cheqs BBVA')
    except NoSuchElementException as nse:
        print('No se encontró un elemento necesario en la página:', str(nse))
    finally:
        if driver:
            driver.quit()
        if automation_var == 'Posicion Consolidada' or automation_var == 'E-Cheqs':
            sys.exit()
        elif automation_var == 'Reporte General':
            pass
