from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui
import datetime
import time
import json
import os
import shutil
import sys

def login_macro():
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

        user_name = 'danielscattone'
        password = 'abcd1672'

        #Inicio automatizacion web
        driver.get('https://www.macro.com.ar/bancainternet/#')

        input_username = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By. XPATH, '/html/body/div[2]/div/form/div[2]/div[3]/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div/div[4]/div/div/div/div/div/div[1]/input')))
        input_username.send_keys(user_name)

        time.sleep(3)
        pyautogui.press('enter')
        time.sleep(3)

        input_password = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By. XPATH, '/html/body/div[2]/div/form/div[2]/div[2]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div/div[3]/div/div/div[1]/div/div/div/div/div/div[1]/input')))
        input_password.send_keys(password)

        time.sleep(3)
        pyautogui.press('enter')
        time.sleep(10)
        return driver
    except Exception as e:
        print('Error en login Macro Banca Internet, ', {str(e)})