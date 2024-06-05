from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.folders import *
from banks.credicoop.login_credicoop import login_credicoop
from reportlab.pdfgen import canvas
import datetime
import shutil
import time
import sys
import os

def credicoop(bank, automation_var):
    try:
        driver = login_credicoop()
        client_folder = 'Scattone Daniel Oscar'
        if automation_var == 'Posicion Consolidada' or automation_var == 'E-Cheqs':
            date_folder = folders(bank, client_folder, automation_var)
        elif automation_var == 'Reporte General':
            date_folder = folders_report(client_folder, automation_var)
        else:
            print('Error al elegir tipo de automatizacion')

        date = datetime.datetime.now()
        formatted_file = date.strftime("%d-%m-%Y")
        time.sleep(5)
        # Inyectar CSS para ocultar elementos que no deben imprimirse
        css_to_hide_elements = """
        var style = document.createElement('style');
        style.id = 'hide-elements-style';
        style.innerHTML = `
            .leftbar, 
            .topbar, 
            .boxWhite,
            #2182
               {
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
            name_file = f'Posición Consolidada - {client_folder} - Banco Credicoop - Emisión {formatted_file}.pdf'
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
                print("El archivo de prestamos finalizo con exito")
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

        exit = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/table/tbody/tr/td[2]/table[1]/tbody/tr/td[3]/a')))
        exit.click()

    except Exception as e:
        print('Error al procesar automatizacion', {str(e)})
        exit = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/table/tbody/tr/td[2]/table[1]/tbody/tr/td[3]/a')))
        exit.click()
    finally:
        if driver:
            driver.quit()
        if automation_var == 'Posicion Consolidada' or automation_var == 'E-Cheqs':
            sys.exit()
        elif automation_var == 'Reporte General':
            pass
