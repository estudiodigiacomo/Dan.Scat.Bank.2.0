from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys


def login_pampa():
    try:
        options = webdriver.ChromeOptions()
        options.add_argument('--start-maximized')
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-popup-blocking")
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-web-security")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--ignore-certificate-errors")
        options.add_argument("--ignore-ssl-errors")
        options.add_experimental_option('prefs', {
        "download.prompt_for_download": False, 
        "download.default_directory": r'D:\Clientes\default_automatizacion_bancos'
        })
        driver = webdriver.Chrome(options=options)
        options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36")

        user_name = 'danielscattone'
        password = '296Carlos?+'
    
        driver.get('https://digital.bancodelapampa.com.ar/loginUsuario')

        #Login de usuario
        input_username = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By. XPATH, '/html/body/div/div/div[1]/div/form/main/div/div[2]/div[1]/div/div/div[2]/input')))
        input_username.send_keys(user_name)

        btn_continue = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By. XPATH, '/html/body/div/div/div[1]/div/form/main/div/div[3]/div[1]/button')))
        btn_continue.click()
    
        input_password = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By. XPATH, '/html/body/div/div/div[1]/div/form/main/div/div[4]/div/div/div/div/div[2]/input')))
        input_password.send_keys(password)

        btn_login = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By. XPATH, '/html/body/div/div/div[1]/div/form/main/div/div[6]/div[1]/button')))
        btn_login.click()
        return driver
    except Exception as e:
        print('Error al iniciar sesion en Banco de La Pampa', {str(e)})