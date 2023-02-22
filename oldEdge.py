from selenium import webdriver # Import webdriver to open chrome
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from tkinter import * #-> Create a form window
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
#import jpype
#import asposecells
#jpype.startJVM()    
#from asposecells.api import Workbook, FileFormatType

import os
import time #-> Pause between commands
import pyautogui

# Update Chrome driver -> run some times
servico = Service(ChromeDriverManager().install())

# Error correction -> ERROR:device_event_log_impl.cc(214)
browser = webdriver.ChromeOptions()
browser.add_experimental_option('excludeSwitches', ['enable-logging'])
browser.add_experimental_option('prefs', {"profile.default_content_setting_values.media_stream_mic": 1})
browser = webdriver.Chrome(options=browser)

browser.maximize_window()  # -> Maxime window
browser.get('https://apps.mypurecloud.com/directory/#/engage/telephonyAdmin/edges/update/L2FwaS92Mi90ZWxlcGhvbnkvcHJvdmlkZXJzL2VkZ2VzLzRhNTdhYTQyLTJkMmQtNGVmNy1hY2Y5LTkyZjc3OTU2M2JlZg')

# Login Genesys
i=0
login_array = ['//*[@id="ember412"]', '//*[@id="org"]', '//*[@id="ember505"]/div[1]/div[2]/div/div[1]/form/button', '//*[@id="ember597"]/div/a/img']

while(i != 4):
    element = WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.XPATH, login_array[i])))

    if i!=1:
        element.click()
    else:
        element.send_keys('Brasilseg')
    
    i+=1

#-> Uma medida por enquanto, pois está precisando clicar 2x no "Microsoft"
try:
    element = WebDriverWait(browser, 6).until(EC.element_to_be_clickable((By.XPATH, login_array[3])))
    element.click()
except:
    print('Continue')
 
from loginTest_genesys import *

#element = WebDriverWait(browser, 40).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div[1]/div[3]/div/div/div/div[2]/div[2]/div/input[1]')))
#element.send_keys(username)
#element = WebDriverWait(browser, 40).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div[1]/div[3]/div/div/div/div[4]/div/div/div/div[2]/input')))
#element.click()
#
#element = WebDriverWait(browser, 40).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div[2]/div/div[3]/div/div[2]/input')))
#element.send_keys(password.get())
#element = WebDriverWait(browser, 40).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div[2]/div/div[4]/div[2]/div/div/div/div/input')))
#element.click()
#
#element = WebDriverWait(browser, 40).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/form/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div[2]/div/div[3]/div[2]/div/div/div[1]/input')))
#element.click()

#os.system('cd C:\\Users\\bandrezzo\\Desktop')
#os.system('start Checklist_v5_Calculo_Metrica.xlsx')

# create a new XLSX workbook
#wb = Workbook(FileFormatType.XLSX)
## insert value in the cells
#wb.getWorksheets().get(0).getCells().get("A1").putValue("Hello World!")
## save workbook as .xlsx file
#wb.save("workbook.xlsx")
#jpype.shutdownJVM()


def getMetrics_values(link, n):
    print('Edge'+n)
    browser.get(link)

    element = WebDriverWait(browser, 40).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div/div[2]/div[1]/div[1]/div[2]/div[2]/iframe'))) #-> Wait the presence of <iframe> to get metrics
    browser.switch_to.frame("engage-frame")

    element = WebDriverWait(browser, 40).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div/div/div/div/div/div[2]/div/div[2]/div[2]/form/div[1]/div[3]/div/edge-metric-info-general/div[4]/metric-info-link/div/icon-text-control/div/div[2]/fc-btn-link/button')))

    metrics = browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div/div/div/div[2]/div/div[2]/div[2]/form/div[1]/div[3]/div/edge-metric-info-general/div[4]/metric-info-link/div/icon-text-control/div/div[2]/fc-btn-link/button').text
    metrics = float(metrics)
    metrics = round(metrics, 0)
    print(metrics)
    pyautogui.write(metrics)
    pyautogui.press('tab')

    metrics = browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div/div/div/div[2]/div/div[2]/div[2]/form/div[1]/div[3]/div/edge-metric-info-general/div[5]/metric-info-link/div/icon-text-control/div/div[2]/fc-btn-link/button').text
    metrics = float(metrics)
    metrics = round(metrics, 0)
    print(metrics)
    pyautogui.write(metrics)
    pyautogui.press('tab')
    pyautogui.press('tab')

    metrics = browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div/div/div/div[2]/div/div[2]/div[2]/form/div[1]/div[3]/div/edge-metric-info-general/div[6]/metric-info-link/div/icon-text-control/div/div[2]/fc-btn-link/button').text
    metrics = float(metrics)
    metrics = round(metrics, 0)
    print(metrics)
    pyautogui.write(metrics)
    pyautogui.press('enter')


getMetrics_values('https://apps.mypurecloud.com/directory/#/engage/telephonyAdmin/edges/update/L2FwaS92Mi90ZWxlcGhvbnkvcHJvdmlkZXJzL2VkZ2VzLzRhNTdhYTQyLTJkMmQtNGVmNy1hY2Y5LTkyZjc3OTU2M2JlZg', '1')
getMetrics_values('https://apps.mypurecloud.com/directory/#/engage/telephonyAdmin/edges/update/L2FwaS92Mi90ZWxlcGhvbnkvcHJvdmlkZXJzL2VkZ2VzLzNhZTM5YTgyLWM0YjItNDFkMC04YTRmLTZmY2I5OTE3ZDM1MQ', '2')
getMetrics_values('https://apps.mypurecloud.com/directory/#/engage/telephonyAdmin/edges/update/L2FwaS92Mi90ZWxlcGhvbnkvcHJvdmlkZXJzL2VkZ2VzLzYwYzljNzBjLWFkYzgtNGQ1OC05Yjk3LWZmMTlmMmYyNDlhMw', '3')
getMetrics_values('https://apps.mypurecloud.com/directory/#/engage/telephonyAdmin/edges/update/L2FwaS92Mi90ZWxlcGhvbnkvcHJvdmlkZXJzL2VkZ2VzLzEwNTE0YzlhLWJlYTMtNGEyZC05ZmIzLWI2ZDE5N2ExOWFmNw', '4')
getMetrics_values('https://apps.mypurecloud.com/directory/#/engage/telephonyAdmin/edges/update/L2FwaS92Mi90ZWxlcGhvbnkvcHJvdmlkZXJzL2VkZ2VzL2FiY2RiZTIxLTU5ZmItNDI1Yy04NmU4LWEzOTcyYmQyY2QxNA', '5')
getMetrics_values('https://apps.mypurecloud.com/directory/#/engage/telephonyAdmin/edges/update/L2FwaS92Mi90ZWxlcGhvbnkvcHJvdmlkZXJzL2VkZ2VzLzkxMTc2YTI0LTJiM2YtNDhhNi1iZDIxLTk0Mjc0ODU2MDEyYw', '6')
getMetrics_values('https://apps.mypurecloud.com/directory/#/engage/telephonyAdmin/edges/update/L2FwaS92Mi90ZWxlcGhvbnkvcHJvdmlkZXJzL2VkZ2VzL2NmYWM4ZmNhLTIzNTYtNDA4Ny1iZDFmLTViOWExMzIzZmUxNw', '7')
getMetrics_values('https://apps.mypurecloud.com/directory/#/engage/telephonyAdmin/edges/update/L2FwaS92Mi90ZWxlcGhvbnkvcHJvdmlkZXJzL2VkZ2VzLzg3YWFhNGVjLTU3ZjEtNDE0Yy1hNzkwLTEyNDk4YzQ4MzlmOA', '8')


#'/html/body/div[1]/div/div/div/div/div/div/div/div[2]/div/div[2]/div[2]/form/div[1]/div[3]/div/edge-metric-info-general/div[5]/metric-info-link/div/icon-text-control/div/div[2]/fc-btn-link/button'

#element = WebDriverWait(browser, 60).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div/div/div/div/div/div[2]/div/div[2]/div[2]/form/div[1]/div[3]/div/edge-metric-info-general/div[4]/metric-info-link/div/icon-text-control/div/div[2]/fc-btn-link/button')))
#element.click()
#cpu_use = browser.execute_script("return document.getElementsByTagName('button')[7].textContent;")
#print(cpu_use)

## Getting current URL source code
#get_source = browser.page_source
#
## Text you want to search
#search_text = "Uso de CPU"
#
## print True if text is present else False
#print(search_text in get_source)    