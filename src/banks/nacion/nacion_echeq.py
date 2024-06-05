from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.folders import folders
from nacion.login_nacion import login_nacion
from dateutil.relativedelta import relativedelta
from selenium.webdriver.support.ui import Select
import datetime
import locale
import shutil
import os
import time
import sys

def nacion(bank, automation_var):
    try:
        driver = login_nacion()
        client_folder = 'Scattone Daniel Oscar'
        date_folder = folders(bank, client_folder, automation_var)
        locale.setlocale(locale.LC_TIME, 'Spanish_Spain.1252')

        acounts = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By. XPATH, '/html/body/div[3]/div[2]/div[3]/div/ul/li[2]/a')))
        acounts.click()
        time.sleep(2)
        cheq = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By. ID, '_menu_chequeElectronico')))
        cheq.click()
        time.sleep(5)
        issued = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By. XPATH, '/html/body/div[3]/div[2]/div[2]/div[4]/div/div[2]/div[1]/div[1]/div[2]/label[2]/span')))
        issued.click()
        time.sleep(2)
        cbu = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By. ID, 'cbuEmisor')))
        cbu.send_keys('0110526120052600894228')

        #Fechas desde y hasta
        today = datetime.datetime.now()
        a_year_ago = today - relativedelta(years=1)
        
        # Formatear las fechas
        day = a_year_ago.day
        month = a_year_ago.strftime('%B').capitalize()
        year = a_year_ago.year

        # Esperar a que el campo de fecha sea visible y hacer clic en él para abrir el calendario
        campo_fecha = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'fechaEmisionDesde'))  # Cambia ID_DEL_CAMPO_FECHA por el id real
        )
        campo_fecha.click()

        # Seleccionar el año del desplegable
        select_year = Select(WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'select.datepick-new-year'))
        ))
        select_year.select_by_visible_text(str(year))

        # Seleccionar el mes del desplegable
        select_month = Select(WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'datepick-new-month'))
        ))
        select_month.select_by_visible_text(str(month))

        # Seleccionar el día del calendario
        selector_day = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, f'//td[a[text()="{day}"]]'))
        )
        selector_day.click()

        consult = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By. XPATH, '/html/body/div[3]/div[2]/div[1]/div[4]/div/div[2]/div[1]/div[2]/div[3]/div[4]/a')))
        consult.click()

        exit = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By. XPATH, '/html/body/div[3]/div[1]/div[4]/div[1]/ul/li[3]/b/a')))
        exit.click()

        time.sleep(20)
    except Exception as e:
        exit = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By. XPATH, '/html/body/div[3]/div[1]/div[4]/div[1]/ul/li[3]/b/a')))
        exit.click()
        print('Error al descargar los E-Cheqs de Nacion', {str(e)})
    finally:
        if driver:
            driver.quit()
        if automation_var == 'Posicion Consolidada' or automation_var == 'E-Cheqs':
            sys.exit()
        elif automation_var == 'Reporte General':
            pass


