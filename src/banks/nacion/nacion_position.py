from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.folders import *
from banks.nacion.login_nacion import login_nacion
import datetime
import shutil
import os
import time
import sys

def nacion(bank, automation_var):
    try:
        driver = login_nacion()
        client_folder = 'Scattone Daniel Oscar'
        if automation_var == 'Posicion Consolidada' or automation_var == 'E-Cheqs':
            date_folder = folders(bank, client_folder, automation_var)
        elif automation_var == 'Reporte General':
            date_folder = folders_report(client_folder, automation_var)
        time.sleep(10)
        #Descargar xls
        download_xls = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By. XPATH, '/html/body/div[3]/div[2]/div[2]/div/div[4]/a[2]')))
        download_xls.click()
        # Esperar a que la descarga termine
        time.sleep(10)

        # Imprimir PDF
        driver.execute_script('window.print();')
        time.sleep(10)

        exit_btn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By. XPATH, '/html/body/div[3]/div[1]/div[4]/div[1]/ul/li[3]/b/a/span')))
        exit_btn.click()

        route_base = r'D:\Clientes\default_automatizacion_bancos'
        download_dir = date_folder
        list_of_files = os.listdir(route_base)
        
        # Filtrar archivos PDF y XLS descargados recientemente
        xls_files = [f for f in list_of_files if f.endswith('.xls')]
        pdf_files = [f for f in list_of_files if f.endswith('.pdf')]
        
        # Procesar archivos XLS
        if xls_files:
            find_xls_file = max(xls_files, key=lambda f: os.path.getctime(os.path.join(route_base, f)))
            shutil.move(os.path.join(route_base, find_xls_file), download_dir)
            rute_destiny_xls = os.path.join(download_dir, find_xls_file)
            new_xls_file_path = os.path.join(download_dir, f'Posición consolidada - {client_folder} - Banco Nacion - Emisión {datetime.datetime.now().strftime("%d-%m-%Y")}.xls')
            os.rename(rute_destiny_xls, new_xls_file_path)
            if os.path.exists(new_xls_file_path):
                print("El archivo XLS se movió correctamente")

        # Procesar archivos PDF
        if pdf_files:
            find_pdf_file = max(pdf_files, key=lambda f: os.path.getctime(os.path.join(route_base, f)))
            shutil.move(os.path.join(route_base, find_pdf_file), download_dir)
            rute_destiny_pdf = os.path.join(download_dir, find_pdf_file)
            new_pdf_file_path = os.path.join(download_dir, f'Posición consolidada - {client_folder} - Banco Nacion - Emisión {datetime.datetime.now().strftime("%d-%m-%Y")}.pdf')
            os.rename(rute_destiny_pdf, new_pdf_file_path)
            if os.path.exists(new_pdf_file_path):
                print("El archivo PDF se movió correctamente")
        driver.quit()
    except Exception as e:
        exit_btn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By. XPATH, '/html/body/div[3]/div[1]/div[4]/div[1]/ul/li[3]/b/a/span')))
        exit_btn.click()
        print('Error al descargar Posicion Consolidada de Banco Nacion', {str(e)})

def nacion_report(bank, automation_var):
    try:
        driver = login_nacion()
        client_folder = 'Scattone Daniel Oscar'
        date_folder = folders_report(client_folder, automation_var)
        time.sleep(10)
        # Esperar a que la descarga termine
        time.sleep(10)

        # Imprimir PDF
        driver.execute_script('window.print();')
        time.sleep(10)

        exit_btn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By. XPATH, '/html/body/div[3]/div[1]/div[4]/div[1]/ul/li[3]/b/a/span')))
        exit_btn.click()

        route_base = r'D:\Clientes\default_automatizacion_bancos'
        download_dir = date_folder
        list_of_files = os.listdir(route_base)
        
        # Filtrar archivos PDF
        pdf_files = [f for f in list_of_files if f.endswith('.pdf')]
        
        # Procesar archivos PDF
        if pdf_files:
            find_pdf_file = max(pdf_files, key=lambda f: os.path.getctime(os.path.join(route_base, f)))
            shutil.move(os.path.join(route_base, find_pdf_file), download_dir)
            rute_destiny_pdf = os.path.join(download_dir, find_pdf_file)
            new_pdf_file_path = os.path.join(download_dir, f'Posición consolidada - {client_folder} - Banco Nacion - Emisión {datetime.datetime.now().strftime("%d-%m-%Y")}.pdf')
            os.rename(rute_destiny_pdf, new_pdf_file_path)
            if os.path.exists(new_pdf_file_path):
                print("El archivo PDF se movió correctamente")
        driver.quit()
    except Exception as e:
        exit_btn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By. XPATH, '/html/body/div[3]/div[1]/div[4]/div[1]/ul/li[3]/b/a/span')))
        exit_btn.click()
        print('Error al descargar Posicion Consolidada de Banco Nacion', {str(e)})
    finally:
        if driver:
            driver.quit()
        if automation_var == 'Posicion Consolidada' or automation_var == 'E-Cheqs':
            sys.exit()
        elif automation_var == 'Reporte General':
            pass
