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

def login_macro():
    try:
        options = webdriver.ChromeOptions()
        options.add_argument('--start-maximized')
        options.add_experimental_option('prefs', {
        "download.prompt_for_download": False, 
        "download.default_directory": r'D:\Clientes\default_automatizacion_bancos'
        })
        driver = webdriver.Chrome(options=options)

        user_name = 'danielscattone'
        password = 'abcd1672'

        #Inicio automatizacion web
        driver.get('https://www.macro.com.ar/biempresas/#')

        input_username = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By. XPATH, '/html/body/div[1]/div/form/div[2]/div[1]/div/div/div[2]/div/div/div[2]/div/div/div/div/div/div[1]/div/div/div[5]/div/div/div/div/div/div[1]/input')))
        input_username.send_keys(user_name)

        time.sleep(3)
        pyautogui.press('enter')
        time.sleep(3)

        input_password = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By. XPATH, '/html/body/div[1]/div/form/div[2]/div[1]/div/div/div[2]/div/div/div[2]/div/div/div/div/div/div[3]/div/div/div[1]/div/div/div/div/div/div[1]/input')))
        input_password.send_keys(password)

        time.sleep(3)
        pyautogui.press('enter')
        time.sleep(10)
        return driver
    except Exception as e:
        print('Error en login Macro, ', {str(e)})