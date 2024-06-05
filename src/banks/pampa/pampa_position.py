from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.folders import *
from banks.pampa.login_pampa import login_pampa
import datetime
import time
import sys
import os
import shutil

def pampa(bank, automation_var):
    try:
        driver = login_pampa()
        client_folder = 'Scattone Daniel Oscar'
        if automation_var == 'Posicion Consolidada' or automation_var == 'E-Cheqs':
            date_folder = folders(bank, client_folder, automation_var)
        elif automation_var == 'Reporte General':
            date_folder = folders_report(client_folder, automation_var)
        else:
            print('Error al elegir tipo de automatizacion')

        view = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By. XPATH, '/html/body/div[1]/div[1]/div[2]/div[2]/main/div[2]/div[3]/div/div[1]/div/div[4]/button')))
        view.click()
          
        time.sleep(3)


        date = datetime.datetime.now()
        formatted_file = date.strftime("%d-%m-%Y")

        # Descargar archivos
        download_btn = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/main/div/div[1]/div/header/div[3]/div/div/button'))
        )
        time.sleep(5)
        def download_file(option_xpath):
            download_btn.click()
            download_option = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, option_xpath)))
            download_option.click()
            time.sleep(3)
        
        download_file('/html/body/div/div[1]/div[2]/div[2]/main/div/div[1]/div/header/div[3]/div/div/ul/div[1]/button')
        download_file('/html/body/div/div[1]/div[2]/div[2]/main/div/div[1]/div/header/div[3]/div/div/ul/div[2]/button')
        download_file('/html/body/div/div[1]/div[2]/div[2]/main/div/div[1]/div/header/div[3]/div/div/ul/div[3]/button')

        exit = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div/div[1]/div[1]/header/div[2]/div[3]/button'))
        )
        exit.click()

        route_base = r'D:\Clientes\default_automatizacion_bancos'
        download_dir = date_folder

        # Obtener lista de archivos
        list_of_files = os.listdir(route_base)

        # Iterar sobre los archivos descargados
        for downloaded_file in list_of_files:
            if downloaded_file.endswith('.pdf'):
                extension = 'pdf'
            elif downloaded_file.endswith('.xls'):
                extension = 'xls'
            elif downloaded_file.endswith('.csv'):
                extension = 'csv'
            else:
                continue

            date = datetime.datetime.now()
            formatted_file = date.strftime("%d-%m-%Y")
            name_file = f'Posición consolidada - {client_folder} - Banco de La Pampa - Emisión {formatted_file}.{extension}'

            try:
                source_file = os.path.join(route_base, downloaded_file)
                dest_file = os.path.join(download_dir, name_file)
                
                # Mover y renombrar el archivo
                shutil.move(source_file, dest_file)
                print(f"El archivo se movió y renombró correctamente a: {dest_file}")
            except Exception as e:
                print(f'Error al mover y renombrar el archivo {downloaded_file}: {e}')

        driver.quit()
    except Exception as e:
        print('Error en la automatizacion :', e)
    finally:
        if driver:
            driver.quit()
            driver.quit()
        if automation_var == 'Posicion Consolidada' or automation_var == 'E-Cheqs':
            sys.exit()
        elif automation_var == 'Reporte General':
            pass



def pampa_report(bank, automation_var):
    try:
        driver = login_pampa()
        client_folder = 'Scattone Daniel Oscar'
        date_folder = folders_report(client_folder, automation_var)
        view = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/div[2]/div[2]/main/div[2]/div[3]/div/div[1]/div/div[4]/button')))
        view.click()
          
        time.sleep(3)

        date = datetime.datetime.now()
        formatted_file = date.strftime("%d-%m-%Y")

        # Descargar archivos PDF
        download_btn = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/main/div/div[1]/div/header/div[3]/div/div/button'))
        )
        time.sleep(5)
        def download_file(option_xpath):
            download_btn.click()
            download_option = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, option_xpath)))
            download_option.click()
            time.sleep(3)
        
        download_file('/html/body/div/div[1]/div[2]/div[2]/main/div/div[1]/div/header/div[3]/div/div/ul/div[1]/button')

        exit = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div/div[1]/div[1]/header/div[2]/div[3]/button'))
        )
        exit.click()

        route_base = r'D:\Clientes\default_automatizacion_bancos'
        download_dir = date_folder

        # Obtener lista de archivos
        list_of_files = os.listdir(route_base)

        # Iterar sobre los archivos descargados
        for downloaded_file in list_of_files:
            if downloaded_file.endswith('.pdf'):
                date = datetime.datetime.now()
                formatted_file = date.strftime("%d-%m-%Y")
                name_file = f'Posición consolidada - {client_folder} - Banco de La Pampa - Emisión {formatted_file}.pdf'

                try:
                    source_file = os.path.join(route_base, downloaded_file)
                    dest_file = os.path.join(download_dir, name_file)
                    
                    # Mover y renombrar el archivo
                    shutil.move(source_file, dest_file)
                    print(f"El archivo se movió y renombró correctamente a: {dest_file}")
                except Exception as e:
                    print(f'Error al mover y renombrar el archivo {downloaded_file}: {e}')

        driver.quit()
    except Exception as e:
        print('Error en la automatizacion:', e)
    finally:
        if driver:
            driver.quit()
        if automation_var == 'Posicion Consolidada' or automation_var == 'E-Cheqs':
            sys.exit()
        elif automation_var == 'Reporte General':
            pass
