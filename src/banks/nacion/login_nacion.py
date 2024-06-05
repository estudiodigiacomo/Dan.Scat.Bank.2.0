from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import datetime
import shutil
import os
import time
import sys

def login_nacion():
    try:
        options = webdriver.ChromeOptions()
        options.add_argument('--start-maximized')
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--disable-gpu")
        options.add_argument("--remote-debugging-port=9222")
        options.add_experimental_option('prefs', {
            "download.prompt_for_download": False, 
            "download.default_directory": r'D:\Clientes\default_automatizacion_bancos',
            'savefile.default_directory': r'D:\Clientes\default_automatizacion_bancos',
            'printing.print_preview_sticky_settings.appState': json.dumps({
                "recentDestinations": [
                    {
                        "id": "Save as PDF",
                        "origin": "local",
                        "account": ""
                    }
                ],
                "selectedDestinationId": "Save as PDF",
                "version": 2
            }),
            'profile.default_content_setting_values.automatic_downloads': 1
        })
        options.add_argument('--kiosk-printing')
        options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36")
        driver = webdriver.Chrome(options=options)  

        user_name = 'daniel256121'
        password = '652danio'

        driver.get('https://hb.redlink.com.ar/bna/login.htm')

        input_username = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By. XPATH, '/html/body/form[1]/div[2]/div[2]/div[3]/div[2]/div[1]/div[1]/input')))
        input_username.send_keys(user_name)
        click_username = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By. CLASS_NAME, 'btn_ingresar')))
        click_username.click()
        time.sleep(1)
        input_password = WebDriverWait(driver, 10).until(EC. presence_of_element_located((By. XPATH, '/html/body/form[1]/div[2]/div[2]/div[3]/div[2]/div[2]/div[1]/input')))
        input_password.send_keys(password)
        click_password = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By. XPATH, '/html/body/form[1]/div[2]/div[2]/a')))
        click_password.click()
        time.sleep(1)
        return driver
    except Exception as e:
        print('Error al hacer login en Banco Nacion', {str(e)})