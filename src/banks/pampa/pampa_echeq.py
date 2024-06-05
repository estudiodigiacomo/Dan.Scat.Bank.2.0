from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.folders import folders
from pampa.login_pampa import login_pampa
import datetime
import time
import sys
import os
import shutil


def pampa(bank, automation_var):
    try:
        driver = login_pampa()
        client_folder = 'Scattone Daniel Oscar'

        date_folder = folders(bank, client_folder, automation_var)


        cheques = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By. XPATH, '/html/body/div[1]/div[1]/div[2]/div[1]/nav/div/div[4]/div/button')))
        cheques.click()
    
        e_cheqs = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By. XPATH, '/html/body/div[1]/div[1]/div[2]/div[1]/nav/div/div[4]/ul/div[4]/a')))
        e_cheqs.click()

        issued = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By. XPATH, '/html/body/div/div[1]/div[2]/div[2]/form/main/div/div/div/div[1]/div/div[2]/button[3]')))
        issued.click()
        time.sleep(2)        

        def download_file(option_xpath):
            download_btn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By. ID, 'global.download')))
            download_btn.click()
            time.sleep(1)
            download_option = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, option_xpath)))
            download_option.click()
            time.sleep(3)
        
        download_file('/html/body/div/div[1]/div[2]/div[2]/form/main/div/div/div/div[4]/div[2]/div[1]/div[1]/div/ul/div[1]/button')
        download_file('/html/body/div/div[1]/div[2]/div[2]/form/main/div/div/div/div[4]/div[2]/div[1]/div[1]/div/ul/div[2]/button')
        download_file('/html/body/div/div[1]/div[2]/div[2]/form/main/div/div/div/div[4]/div[2]/div[1]/div[1]/div/ul/div[3]/button')

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
            name_file = f'E-Cheqs - {client_folder} - Banco de La Pampa - Emisión {formatted_file}.{extension}'

            try:
                source_file = os.path.join(route_base, downloaded_file)
                dest_file = os.path.join(download_dir, name_file)
                
                # Mover y renombrar el archivo
                shutil.move(source_file, dest_file)
                print(f"El archivo se movió y renombró correctamente a: {dest_file}")
            except Exception as e:
                print(f'Error al mover y renombrar el archivo {downloaded_file}: {e}')
    except Exception as e:
        exit = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div/div[1]/div[1]/header/div[2]/div[3]/button'))
        )
        print('Error a descargar E-Cheqs', {str(e)})
    finally:
        if driver:
            driver.quit()
        sys.exit()