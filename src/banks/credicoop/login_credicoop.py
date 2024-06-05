from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import datetime
import time
import sys
import os

def login_credicoop():
    try:
        options = webdriver.ChromeOptions()
        options.add_argument('--start-maximized')
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--disable-gpu")
        options.add_argument("--remote-debugging-port=9222")
        options.add_experimental_option('prefs', {
        "download.prompt_for_download": False, 
        "download.default_directory": r'D:\Clientes\default_automatizacion_bancos'
        })
        appState = {
            "recentDestinations": [
                    {
                        "id": "Save as PDF",
                        "origin": "local",
                        "account": ""
                    }
                ],
                "selectedDestination": "Save as PDF",
                "version": 2
                    }
        prefs = {
            'printing.print_preview_sticky_settings.appState': json.dumps(appState),
            'savefile.default_directory': r'D:\Clientes\default_automatizacion_bancos'
                }

        options.add_experimental_option('prefs', prefs)
        options.add_argument('--kiosk-printing')
        options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36")
        driver = webdriver.Chrome(options=options)

        nro_adherente = '2804105'
        dni = '22749393'
        password = '25Bellco'

        driver.get('https://bancainternet.bancocredicoop.coop/bcclbe/')

        dropdown_adh = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By. XPATH, '/html/body/div[4]/table/tbody/tr/td[2]/table/tbody/tr[3]/td/form/table/tbody/tr[1]/td[2]/select/option[2]')))
        dropdown_adh.click()
        time.sleep(1)
        input_adh = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By. XPATH, '/html/body/div[4]/table/tbody/tr/td[2]/table/tbody/tr[3]/td/form/table/tbody/tr[3]/td[2]/input')))
        input_adh.send_keys(nro_adherente)
        time.sleep(1)
        input_dni = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By. XPATH, '/html/body/div[4]/table/tbody/tr/td[2]/table/tbody/tr[3]/td/form/table/tbody/tr[5]/td[2]/input')))
        input_dni.send_keys(dni)
        time.sleep(1)
        input_password = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/table/tbody/tr/td[2]/table/tbody/tr[3]/td/form/table/tbody/tr[6]/td[2]/input')))
        input_password.send_keys(password)
        time.sleep(1)
        btn_login = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/table/tbody/tr/td[2]/table/tbody/tr[3]/td/form/table/tbody/tr[8]/td[2]/input[3]')))
        btn_login.click()
        time.sleep(1)
        return driver
    except Exception as e:
        print('Error al hacer login en credicoop:',  {str(e)})