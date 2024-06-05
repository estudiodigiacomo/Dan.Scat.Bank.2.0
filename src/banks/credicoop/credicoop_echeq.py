from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.folders import *
from credicoop.login_credicoop import login_credicoop
from reportlab.pdfgen import canvas
import datetime
import time
import sys
import os

def credicoop(bank, automation_var):
    try:
        client_folder = 'Scattone Daniel Oscar'
        date_folder = folders(bank, client_folder, automation_var)
        driver = login_credicoop()
        

        exit = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/table/tbody/tr/td[2]/table[1]/tbody/tr/td[3]/a')))
        exit.click()

    except Exception as e:
        exit = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/table/tbody/tr/td[2]/table[1]/tbody/tr/td[3]/a')))
        exit.click()
        print('Error al descargar E_Cheqs', {str(e)})
    finally:
        if driver:
            driver.quit()
        if automation_var == 'Posicion Consolidada' or automation_var == 'E-Cheqs':
            sys.exit()
        elif automation_var == 'Reporte General':
            pass
