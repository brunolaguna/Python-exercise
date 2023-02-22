#-> Lines of code I'm not using, but I was using
#from ctypes import windll
#import threading
#import pyautogui
#import keyboard

from selenium import webdriver # Import webdriver to open chrome
from selenium.webdriver.support.ui import WebDriverWait #-> This import serves to use the method of waiting for the element to appear to continue the line of code. 
from selenium.webdriver.chrome.service import Service #-> Use service on my program
from webdriver_manager.chrome import ChromeDriverManager
from tkinter import * #-> Create a form window
from selenium.webdriver.support import expected_conditions as EC #-> Use the EC to check what the status of the element is
from selenium.webdriver.common.by import By #-> BY.XPATH is the same as using 'xpath'

import multiprocessing #-> With this module I can execute any process "simultaneous"
import time #-> Pause between commands
import os #-> Use Windows command lines through python

# Just an array with the links of each edge
link = ['https://apps.mypurecloud.com/directory/#/engage/telephonyAdmin/edges/update/L2FwaS92Mi90ZWxlcGhvbnkvcHJvdmlkZXJzL2VkZ2VzLzRhNTdhYTQyLTJkMmQtNGVmNy1hY2Y5LTkyZjc3OTU2M2JlZg',
        'https://apps.mypurecloud.com/directory/#/engage/telephonyAdmin/edges/update/L2FwaS92Mi90ZWxlcGhvbnkvcHJvdmlkZXJzL2VkZ2VzLzNhZTM5YTgyLWM0YjItNDFkMC04YTRmLTZmY2I5OTE3ZDM1MQ',
        'https://apps.mypurecloud.com/directory/#/engage/telephonyAdmin/edges/update/L2FwaS92Mi90ZWxlcGhvbnkvcHJvdmlkZXJzL2VkZ2VzLzYwYzljNzBjLWFkYzgtNGQ1OC05Yjk3LWZmMTlmMmYyNDlhMw',
        'https://apps.mypurecloud.com/directory/#/engage/telephonyAdmin/edges/update/L2FwaS92Mi90ZWxlcGhvbnkvcHJvdmlkZXJzL2VkZ2VzLzEwNTE0YzlhLWJlYTMtNGEyZC05ZmIzLWI2ZDE5N2ExOWFmNw',
        'https://apps.mypurecloud.com/directory/#/engage/telephonyAdmin/edges/update/L2FwaS92Mi90ZWxlcGhvbnkvcHJvdmlkZXJzL2VkZ2VzL2FiY2RiZTIxLTU5ZmItNDI1Yy04NmU4LWEzOTcyYmQyY2QxNA',
        'https://apps.mypurecloud.com/directory/#/engage/telephonyAdmin/edges/update/L2FwaS92Mi90ZWxlcGhvbnkvcHJvdmlkZXJzL2VkZ2VzLzkxMTc2YTI0LTJiM2YtNDhhNi1iZDIxLTk0Mjc0ODU2MDEyYw',
        'https://apps.mypurecloud.com/directory/#/engage/telephonyAdmin/edges/update/L2FwaS92Mi90ZWxlcGhvbnkvcHJvdmlkZXJzL2VkZ2VzL2NmYWM4ZmNhLTIzNTYtNDA4Ny1iZDFmLTViOWExMzIzZmUxNw',
        'https://apps.mypurecloud.com/directory/#/engage/telephonyAdmin/edges/update/L2FwaS92Mi90ZWxlcGhvbnkvcHJvdmlkZXJzL2VkZ2VzLzg3YWFhNGVjLTU3ZjEtNDE0Yy1hNzkwLTEyNDk4YzQ4MzlmOA']

# Function to execute the spreadsheet
def excel():
    print("\nLoading...\n")
    os.system('"C:\\Users\\bandrezzo\Desktop\\Checklist_v5_Calculo_Metrica.xlsx"') #-> Run the file in this path       

# Main function
def getEdges_metrics_values():

    # Update Chrome driver -> run some times
    servico = Service(ChromeDriverManager().install())

    # Error correction -> ERROR:device_event_log_impl.cc(214)
    browser = webdriver.ChromeOptions()
    browser.add_experimental_option('excludeSwitches', ['enable-logging'])
    browser.add_experimental_option('prefs', {"profile.default_content_setting_values.media_stream_mic": 1}) #-> Accept the use of the microphone on the page
    browser.headless = True #-> Hide the chrome.exe
    browser = webdriver.Chrome(options=browser)
    browser.maximize_window()  # -> Maxime window
    browser.get('https://apps.mypurecloud.com/directory/#/engage/telephonyAdmin/edges/update/L2FwaS92Mi90ZWxlcGhvbnkvcHJvdmlkZXJzL2VkZ2VzLzRhNTdhYTQyLTJkMmQtNGVmNy1hY2Y5LTkyZjc3OTU2M2JlZg')
    
    # Login to the genesys platform
    i=0
    login_array = ['//*[@id="ember412"]', '//*[@id="org"]', '//*[@id="ember505"]/div[1]/div[2]/div/div[1]/form/button', '//*[@id="ember597"]/div/a/img'] #-> Xpath of each button or input 
    while(i != 4):
        element = WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.XPATH, login_array[i])))
        if i!=1:
            element.click()
        else:
            element.send_keys('Brasilseg')
        i+=1

    #-> One measure for now, because I need to click twice on "Microsoft"
    try:
        element = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, login_array[3])))
        element.click()
    except:
        print('I got it!\n')

    ###->> I'm still creating it
    #from loginTest_genesys import *
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

        # New arrays for data storage
        n = ['1', '2', '3', '4', '5', '6', '7', '8']

        a=[]

        b=[]

        c=[]

    # Create the "Table"
    for i in range(8):
        print("I'm on Edge",n[i]+'...')
        browser.get(link[i])
        element = WebDriverWait(browser, 40).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div/div[2]/div[1]/div[1]/div[2]/div[2]/iframe'))) #-> Wait the presence of <iframe> to get metrics
        browser.switch_to.frame("engage-frame") #-> Switch to Iframe
        element = WebDriverWait(browser, 40).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div/div/div/div/div/div[2]/div/div[2]/div[2]/form/div[1]/div[3]/div/edge-metric-info-general/div[4]/metric-info-link/div/icon-text-control/div/div[2]/fc-btn-link/button'))) #If data is present, continue
        time.sleep(11) #-> Wait for the data to appear

        a.append(8) #-> create 8 indexes for the array a, b and c
        d = browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div/div/div/div[2]/div/div[2]/div[2]/form/div[1]/div[3]/div/edge-metric-info-general/div[4]/metric-info-link/div/icon-text-control/div/div[2]/fc-btn-link/button').text
        d = d[:-1] #-> Delete the last character of the string
        d = float(d) #-> Convert to float number
        d = round(d) #-> round the number
        a[i] = d #-> The index receives the variable d

        b.append(8)
        e = browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div/div/div/div[2]/div/div[2]/div[2]/form/div[1]/div[3]/div/edge-metric-info-general/div[5]/metric-info-link/div/icon-text-control/div/div[2]/fc-btn-link/button').text
        e = e[:-1]
        e = float(e)
        e = round(e)
        b[i] = e

        c.append(8)
        f = browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div/div/div/div[2]/div/div[2]/div[2]/form/div[1]/div[3]/div/edge-metric-info-general/div[6]/metric-info-link/div/icon-text-control/div/div[2]/fc-btn-link/button').text
        f = f[:-1]
        f = float(f)
        f = round(f)
        c[i] = f

    print("\nPaste the data into the correct column(CPU, Memory and Usage).\n\n Enjoy!\n")

    #print("CPU:\n")
    #for o in range (0,7):
    #    str(a[o]+"%\n"),

    print('CPU:\n'
    ,str(a[0])+'%\n'
    ,str(a[1])+'%\n'
    ,str(a[2])+'%\n'
    ,str(a[3])+'%\n'
    ,str(a[4])+'%\n'
    ,str(a[5])+'%\n'
    ,str(a[6])+'%\n'
    ,str(a[7])+'%\n')
    print('Memory:\n'
    ,str(b[0])+'%\n'
    ,str(b[1])+'%\n'
    ,str(b[2])+'%\n'
    ,str(b[3])+'%\n'
    ,str(b[4])+'%\n'
    ,str(b[5])+'%\n'
    ,str(b[6])+'%\n'
    ,str(b[7])+'%\n')
    print('Usage:\n'
    ,str(c[0])+'%\n'
    ,str(c[1])+'%\n'
    ,str(c[2])+'%\n'
    ,str(c[3])+'%\n'
    ,str(c[4])+'%\n'
    ,str(c[5])+'%\n'
    ,str(c[6])+'%\n'
    ,str(c[7])+'%\n')

    browser.close()

#def counter():
#    finish = time.perf_counter()
#    minutes = finish / 60
#    print("Finished running after minutes:",round(minutes))

p1 = multiprocessing.Process(target=excel)
p2 = multiprocessing.Process(target=getEdges_metrics_values)
#p3 = multiprocessing.Process(target=counter)
if __name__ == '__main__':
        p1.start()
        p2.start()
        p2.join()
        p1.terminate()
        #p3.start()

# Just comments
#cpu_use = browser.execute_script("return document.getElementsByTagName('button')[7].textContent;")
#print(cpu_use)