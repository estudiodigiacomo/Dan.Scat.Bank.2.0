from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time
import sys
import json

def login_bbva():
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

                client_folder = 'Scattone Daniel Oscar'
                dni = '22749393'
                user_name = 'daniel'
                password = 'macavi23'

                driver.get('https://www.bbva.com.ar/')

                banca_online = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By. XPATH,'/html/body/div[1]/header/nav/div/nav/ul/li[3]/div/a/span[1]')))
                banca_online.click()

                iframe = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/header/div[3]/div[1]/div[2]/iframe')))

                # Cambiar al iframe
                driver.switch_to.frame(iframe)

                time.sleep(1)
                input_dni = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By. XPATH, '/html/body/div[1]/main/form/fieldset/bbva-web-form-text/input')))
                input_dni.send_keys(dni)
                time.sleep(1)
                input_user = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By. XPATH, '/html/body/div[1]/main/form/bbva-web-form-password[1]/input')))
                input_user.send_keys(user_name)
                time.sleep(1)
                input_password = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By. XPATH, '/html/body/div[1]/main/form/bbva-web-form-password[2]/input')))
                input_password.send_keys(password)
                time.sleep(3)
                btn_login = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By. XPATH, '/html/body/div[1]/main/form/bbva-button')))
                btn_login.click()
                #Volver al iframe
                driver.switch_to.default_content()
                return driver
        except Exception as e:
                print('Error inesperado:', str(e))
        except NoSuchElementException as nse:
                print('No se encontró un elemento necesario en la página:', str(nse))
        