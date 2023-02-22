from selenium import webdriver # Import webdriver to open chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from tkinter import * #-> Create a form window

# -- If I need to use --

import os
import time #-> Pause between commands
import random
import pyautogui

# Update Chrome driver -> run some times
servico = Service(ChromeDriverManager().install())
#browser = webdriver.Chrome(service=servico)

# Error correction -> ERROR:device_event_log_impl.cc(214)
browser = webdriver.ChromeOptions()
browser.add_experimental_option('excludeSwitches', ['enable-logging'])
browser.add_experimental_option('prefs', {"profile.default_content_setting_values.media_stream_mic": 1})
browser = webdriver.Chrome(options=browser)

# Other device permissions like microphone and camera
#"profile.default_content_setting_values.media_stream_camera": 1,
#"profile.default_content_setting_values.geolocation": 1, 
#"profile.default_content_setting_values.notifications": 1 

# --I found the error on stack overflow site and the code was like this--
#options = webdriver.ChromeOptions()
#options.add_experimental_option('excludeSwitches', ['enable-logging'])
#driver = webdriver.Chrome(options=options)

#browser.set_window_size(1366, 768) --> Set window

browser.maximize_window() # -> Maxime window
browser.get('https://www.bbseguros.com.br/seguros/ajuda/telefones-atendimento-seguros') # -> Open chrome in this website
time.sleep(2)
#assert "www.bbseguros.com.br" in browser.title

# --Beginning of the code to fill the form on the bb insurance website--
#browser.find_element('xpath', '//*[@id="page"]/article/div/div[5]/div/div/div/div[2]/div/a').click()
#time.sleep(2)
#
#pyautogui.click(x=1032, y=565)
#time.sleep(2)
#pyautogui.write('Bruno')
#pyautogui.press('tab')
#
#time.sleep(1)
#pyautogui.write('55555555555')
#pyautogui.press('tab')
#
#time.sleep(1)
#pyautogui.write('11971607521')
#pyautogui.press('tab')
#
#time.sleep(1)

#pyautogui.write('bandrezzo@brasilseg.com.br')
#pyautogui.press('tab')
#
#time.sleep(1)
#pyautogui.press('space')
#pyautogui.press('tab')
#
#time.sleep(1)
#pyautogui.press('space')
# --End of code to fill in the form on the bb insurance website--

# Open a new window
browser.execute_script("window.open('');")
time.sleep(1)

#Switch to the new window and open new URL
browser.switch_to.window(browser.window_handles[1])
browser.get('https://apps.mypurecloud.com/directory/#/admin/routing/datatables/fee09d78-8386-4574-b2e0-95e6c776e87b/rows')
#assert "mypurecloud" in browser.title
#time.sleep(8)

# Login Genesys
i=0
login_array = ['//*[@id="ember412"]', '//*[@id="org"]', '//*[@id="ember505"]/div[1]/div[2]/div/div[1]/form/button', '//*[@id="ember597"]/div/a/img']

while(i != 4):
    element = WebDriverWait(browser, 120).until(EC.element_to_be_clickable((By.XPATH, login_array[i])))

    if i!=1:
        element.click()
    else:
        element.send_keys('Brasilseg')
    
    i+=1

# Login microsoft if need
try:
    element = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="i0116"]')))
    from loginTest import *
    element.send_keys(username.get())
    browser.find_element('xpath', '//*[@id="idSIButton9"]').click()
    element = WebDriverWait(browser, 40).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="i0118"]')))
    element.send_keys(password.get())
    browser.find_element('xpath', '//*[@id="idSIButton9"]').click()
    element = WebDriverWait(browser, 40).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="idBtn_Back"]')))
    element.click()
except:
    print("You're in the brasilsegcorp network.\n Loading...")


#if browser.current_url == 'https://login.microsoftonline.com/cb80994c-e21f-444b-abba-37fd0011e511/saml2?SAMLRequest=fJJRb5swFIX%2FCvK7g6FQjFUisUTTsrULapJm6stkzKX1ZGzma9Z0v34q7aRuD3m17znfsc%2B9QjmYUdRTeLS38HMCDNFpMBbFfFGRyVvhJGoUVg6AIiixq2%2BuRbpgYvQuOOUMeSc5r5CI4IN2lkSbdUW%2BnI6F2fJ0PAZm6rvt55r3vfNPl99XR%2F7j%2FvRNnfDQ3Pz26kCiO%2FCona1IumAkat7YH7TttH04j21fh1B82u8b2mx3exLVf6OsnMVpAL8D%2F0srONxeV%2BQxhBFFHBv3oO1ieB4nD8q4qVsoN8Qv7yTRBnGCjcUgbahIytILyhLK%2BD5lIs8E4%2FckWgMGbWWYc%2F9nqpV36PrgrNEWZmPVclaWmaKQJj3Nsqylsm0lvSj6jrEkgTxJZnpKlnNzYg7hl1x2l3lRlrQr8pRmeZdQzrKeygISqS55UWbFVfxe8Vb8VznAZt04o9VzVBvjnlYeZICKBD8BiT46P8hw%2FndfTnRH%2B3lUBC8tarCBxMtX5L%2FrtfwTAAD%2F%2Fw%3D%3D&sso_reload=true':
#    from loginTest import *

#element = WebDriverWait(browser, 120).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ember412"]'))) #browser.find_element('xpath', '//*[@id="ember412"]').click() # -> Clicked on "Mais opções de logon"
#element.click()
#
#element = WebDriverWait(browser, 120).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="org"]'))) #browser.find_element('xpath', '//*[@id="org"]').send_keys('Brasilseg') # -> Write "Brasilseg"
#element.send_keys('Brasilseg')
#
#element = WebDriverWait(browser, 120).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ember505"]/div[1]/div[2]/div/div[1]/form/button'))) # browser.find_element('xpath', '//*[@id="ember505"]/div[1]/div[2]/div/div[1]/form/button').click()  # -> Clicked on next
#element.click()
#
#element = WebDriverWait(browser, 120).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ember597"]/div/a/img'))) #browser.find_element('xpath', '//*[@id="ember597"]/div/a/img').click() # -> Clicked on Microsoft
#element.click()

# Close microphone notification
#time.sleep(45)
#for z in range (0, 2):
#    time.sleep(5)
#    pyautogui.press('esc')
#    print('Passou por mim')
#time.sleep(10)

element = WebDriverWait(browser, 40).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ember938"]/nav[1]/div[2]/div[3]/div[3]')))
time.sleep(10)
fila = browser.find_element('xpath', '//*[@id="ember938"]/nav[1]/div[2]/div[3]/div[3]').text #-> Get text if you're on queue or off queue

# -> If you're off queue click and stay on queue. Else, just click and hidden the tab
if fila == 'Fora da fila':
    element = WebDriverWait(browser, 40).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ember938"]/nav[1]/div[2]/div[3]/div[3]')))
    element.click()
    #browser.find_element('xpath', '//*[@id="ember938"]/nav[1]/div[2]/div[3]/div[3]').click()
    #browser.find_element('xpath', '//*[@id="ember3053"]/div/button[1]').click()
    element = WebDriverWait(browser, 40).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div/nav[1]/div[1]/div[2]/nav/ul/li[8]/a')))
    element.click()
else:
    element = WebDriverWait(browser, 40).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div/nav[1]/div[1]/div[2]/nav/ul/li[8]/a')))
    element.click()

#pyautogui.hotkey('alt', 'tab')
#onqueue = input("Você está na fila?\n")

#time.sleep(100)
#pyautogui.click(x=713, y=190)
#time.sleep(2)
##browser.find_element('xpath', '//*[@id="ember748"]').send_keys('5511971607515')
#pyautogui.click(x=741, y=607)
#time.sleep(3)
#pyautogui.doubleClick(x=360, y=529)
##fila = browser.find_element('xpath', '//*[@id="ember1439"]')
#time.sleep(1)
#pyautogui.hotkey('ctrl', 'c')
#time.sleep(1)
#pyautogui.hotkey('alt', 'tab')
#time.sleep(2)
#fila = input("Qual a fila? (Telecom ou Telecom1)\n")
##else:
#    #pyautogui.hotkey('alt', 'tab')
#    #time.sleep(1)
#    #pyautogui.click(x=1263, y=141)
#    #time.sleep(0.7)
#    #pyautogui.click(x=713, y=190)
#    #time.sleep(1)
#
#if fila == 'Telecom1':
#    pyautogui.hotkey('alt', 'tab')
#    time.sleep(1)
#    pyautogui.press('right')
#    time.sleep(1)
#    pyautogui.press('backspace')
#    time.sleep(1)
#    pyautogui.press('tab')
#    time.sleep(0.4)
#    pyautogui.press('enter')

os.system('start msedge "https://web.whatsapp.com/"')
time.sleep(15)

def press_tab(x):
    i=0
    while(i!=x):
        pyautogui.press('tab')
        i+=1

def say_hello(contact):
    time.sleep(1)
    pyautogui.write(contact)
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.write('Hello')
    time.sleep(0.5)
    pyautogui.press('enter')
    time.sleep(1)

press_tab(4)
say_hello('teste bb')
press_tab(5)
say_hello('bb seg chat')

#pyautogui.write('bb seg chat')
#time.sleep(1)
#pyautogui.press('enter')
#time.sleep(0.5)
#pyautogui.write('Hello')
#time.sleep(0.5)
#pyautogui.press('enter')

time.sleep(22)
pyautogui.write('55555555555')
time.sleep(1)
pyautogui.press('enter')
#time.sleep(2)
#pyautogui.keyDown('alt')
#time.sleep(1)
#pyautogui.press('tab')
#pyautogui.press('tab')
#time.sleep(1)
#pyautogui.keyUp('alt')
pyautogui.hotkey('alt', 'tab')

element = WebDriverWait(browser, 40).until(EC.element_to_be_clickable((By.XPATH, '/html/body/ul/li/div/div[2]/span[1]/a')))
element.click()

element = WebDriverWait(browser, 60).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div/main/section[7]/div/div/div[2]/div/div/div[1]/div[4]/div/button[2]')))
element.click()

element = WebDriverWait(browser, 40).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="acd-chat-textarea"]')))
element.send_keys('Hi')
webdriver.ActionChains(browser).key_down(Keys.ENTER).perform()

pyautogui.hotkey('alt', 'tab')
time.sleep(0.6)
pyautogui.write('Hi')
time.sleep(0.5)
pyautogui.press('enter')
pyautogui.hotkey('alt', 'tab')

time.sleep(10)
browser.save_screenshot('whatsappBot_screenshots/Perfil_tab.png')

element = WebDriverWait(browser, 40).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div/main/section[7]/div/div/div[2]/div/div/div[2]/div[2]/div[2]/button[6]')))
element.click()
time.sleep(4)
browser.save_screenshot('whatsappBot_screenshots/WrapupCode_tab.png')

element = WebDriverWait(browser, 40).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div/main/section[7]/div/div/div[2]/div/div/div[2]/div[2]/div[2]/button[5]')))
element.click()
time.sleep(1)
browser.save_screenshot('whatsappBot_screenshots/Notes_tab.png')

element = WebDriverWait(browser, 40).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div/main/section[7]/div/div/div[2]/div/div/div[2]/div[2]/div[2]/button[4]')))
element.click()
time.sleep(4)
browser.save_screenshot('whatsappBot_screenshots/ReadyAnswers_tab.png')

element = WebDriverWait(browser, 40).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div/main/section[7]/div/div/div[2]/div/div/div[2]/div[2]/div[2]/button[2]')))
element.click()
time.sleep(1.5)
browser.save_screenshot('whatsappBot_screenshots/InteractionsDetails_tab.png')

element = WebDriverWait(browser, 40).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div/main/section[7]/div/div/div[2]/div/div/div[2]/div[2]/div[2]/button[1]')))
element.click()
time.sleep(2)
browser.save_screenshot('whatsappBot_screenshots/Scripts_tab.png')

#element = WebDriverWait(browser, 40).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[2]/div[1]/div/div[4]/div/div/div[1]/button[1]')))
#element.click()

def chrome_press_tab(press, t):
    i=0
    while(i != press):
        time.sleep(t)
        webdriver.ActionChains(browser).send_keys(Keys.TAB).perform()
        i+=1
        
    webdriver.ActionChains(browser).send_keys(Keys.SPACE).perform()

#element = WebDriverWait(browser, 40).until(EC.element_to_be_clickable((By.CLASS_NAME, 'midia__upload__dropzone')))
#element.click()

#pyautogui.keyDown('pagedown')
#time.sleep(3)
#pyautogui.keyUp('pagedown')

#location = browser.find_element('xpath', '/html/body/div/div[2]/div[1]/div/div[2]/div[2]/div/div/div/div[1]').location
#print(location)


#ed = ActionChains(browser)
#ed.move_by_offset(665, 300).click().perform()

chrome_press_tab(9, 0)
time.sleep(1.7)

pyautogui.click(x=676, y=674)
print('Já passou por mim')

time.sleep(1.5)

pyautogui.write('C:\\Users\\bandrezzo\\Downloads\\Cardapio Rodizio de Hamburguer.pdf')
time.sleep(1)
pyautogui.press('enter')

#i=0
#while(i != 2):
#    webdriver.ActionChains(browser).send_keys(Keys.TAB).perform()
#    i+=1

#chrome_press_tab(2, 0)

#webdriver.ActionChains(browser).send_keys(Keys.SPACE).perform()

#i=0
#while(i != 2):
#    webdriver.ActionChains(browser).send_keys(Keys.TAB).perform()
#    i+=1

chrome_press_tab(2, 0)
time.sleep(1)
chrome_press_tab(2, 0)
time.sleep(0.8)

pyautogui.hotkey('alt', 'tab')
press_tab(12)
pyautogui.press('space')

def press_up(x):
    i=0
    while(i!=x):
        pyautogui.press('up')
        i+=1

press_up(4)
pyautogui.press('space')
time.sleep(1)
pyautogui.write('C:\\Users\\bandrezzo\\Downloads\\Cardapio Rodizio de Hamburguer.pdf')
pyautogui.press('enter')
time.sleep(4)
pyautogui.press('enter')
time.sleep(0.7)
press_tab(4)
pyautogui.press('space')
press_tab(2)
time.sleep(4)
pyautogui.press('enter')
pyautogui.hotkey('alt', 'tab')

#Get what queue you're on(Telecom or Telecom1)
element = WebDriverWait(browser, 40).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div/main/section[7]/div/div/div[1]/div/div[2]/div/div/div[1]/div[2]/div/button')))
which_queue_are_you_on = browser.find_element(By.XPATH, '/html/body/div[4]/div/main/section[7]/div/div/div[1]/div/div[2]/div/div/div[2]/div/a/div/div/div[2]/span').text
print(which_queue_are_you_on)

pyautogui.click(x=842, y=401)
time.sleep(1)
chrome_press_tab(2,0)

time.sleep(0.5)

if which_queue_are_you_on == 'Telecom1':
    print('oi')
    time.sleep(100)

#def aleatorio(x):
#    rand = random.randint(1,9)
#    print(rand)
#    i=0
#    
#    while(i != rand):
#        webdriver.ActionChains(browser).send_keys(Keys.DOWN).perform()
#        i+=1
#    webdriver.ActionChains(browser).send_keys(Keys.ENTER).perform()
#    webdriver.ActionChains(browser).send_keys(Keys.TAB).perform()
#    webdriver.ActionChains(browser).send_keys(Keys.SPACE).perform()
#        
#
#loop = 0
#if which_queue_are_you_on == 'Telecom1':
#    for loop in range(0,5):
#        if loop == 0 or 1:
#            aleatorio()
#        else:
#            aleatorio()

time.sleep(3)
#Random

element = WebDriverWait(browser, 40).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div/main/section[7]/div/div/div[2]/div/div/div[2]/div[1]/button')))
element.click()

#element = WebDriverWait(browser, 40).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[2]/div[1]/div/div[4]/div/div/div[2]/button')))
#element.click()

#time.sleep(100)

#element = WebDriverWait(browser, 40).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ember526"]/gux-search-beta/div/div/gux-text-field-legacy/div/div'))) # BODY -> '//*[@id="ember357"]' | BODYZINHO -> '//*[@id="ember357"]/div' | Search-input-control -> '//*[@id="ember526"]/gux-search-beta' full xpath: /html/body/div[2]/div/div/gux-search-beta | Gux-search-input '/html/body/div[2]/div/div/gux-search-beta/div/div' xpath: //*[@id="ember526"]/gux-search-beta/div/div | hydrated -> xpath: //*[@id="ember526"]/gux-search-beta/div/div/gux-text-field-legacy full-xpath: /html/body/div[2]/div/div/gux-search-beta/div/div/gux-text-field-legacy | Gux-fiel -> xpath: //*[@id="ember526"]/gux-search-beta/div/div/gux-text-field-legacy/div/div -- full-xpath
#print(element) #: /html/body/div[2]/div/div/gux-search-beta/div/div/gux-text-field-legacy/div/div
#time.sleep(100)
#
#element = WebDriverWait(browser, 40).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ember526"]/gux-search-beta/div/div/gux-text-field-legacy/div/div/input')))
#element.send_keys('I found you')
#
#element = WebDriverWait(browser, 40).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ember3007"]')))
#element.click()
#
#element = WebDriverWait(browser, 40).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ember7558"]/div[1]/ul/li[1]/button')))
#element.click()
#
#element = WebDriverWait(browser, 40).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ember3004"]')))
#element.click()
#
#element = WebDriverWait(browser, 40).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="interaction-notes"]')))
#element.send_keys('I found you')
#
#element = WebDriverWait(browser, 40).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ember3001"]')))
#element.send_keys('I found you')
#
#element = WebDriverWait(browser, 40).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ember7572"]/div/div[2]/div[4]/a[1]')))
#element.click()
#
#element = WebDriverWait(browser, 40).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ember7572-back-to-responses"]')))
#element.click()
#
#element = WebDriverWait(browser, 40).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ember6675"]')))
#element.click()
#time.sleep(10)
#interection_detail = browser.find_element('//*[@id="ember7927"]/ul').text
#
#print(interection_detail)
#
#element = WebDriverWait(browser, 40).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ember6672"]')))
#element.click()
#
#element = WebDriverWait(browser, 40).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/div[4]/div/div/div[1]/button')))
#element.click()
#
#element = WebDriverWait(browser, 40).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/div[2]/div[2]/div/div/div/div[1]')))
#element.click()
#
#pyautogui.write('C:\\Users\\bandrezzo\\Downloads\\Cardápio Rodízio de Hamburguer.pdf')
#time.sleep(0.4)
#pyautogui.press('enter')
#
#element = WebDriverWait(browser, 40).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/div[2]/div[2]/button')))
#element.click()
#
#element = WebDriverWait(browser, 40).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/div[4]/div/div/div[2]/button')))
#element.click()
#
#element = WebDriverWait(browser, 40).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/div[3]/div[2]/div/form/div[1]/select')))
#element.click()

time.sleep(100)


#################


pyautogui.click(x=1142, y=240)
time.sleep(5)
pyautogui.click(x=738, y=146)
time.sleep(1)
pyautogui.click(x=694, y=684)
time.sleep(0.5)
pyautogui.write('Oi')
time.sleep(0.5)
pyautogui.press('enter')
pyautogui.hotkey('alt', 'tab')
time.sleep(0.5)
pyautogui.write('Oi')
time.sleep(0.5)
pyautogui.press('enter')
time.sleep(0.5)
pyautogui.hotkey('alt', 'tab')
time.sleep(0.5)
pyautogui.click(x=1129, y=211)
time.sleep(0.5)
pyautogui.click(x=446, y=585)
time.sleep(0.5)
pyautogui.click(x=662, y=653)
time.sleep(1)
pyautogui.write('C:\\Users\\bandrezzo\\Downloads\\Cardápio Rodízio de Hamburguer.pdf')
time.sleep(0.4)
pyautogui.press('enter')
pyautogui.hotkey('alt', 'tab')
time.sleep(1)
pyautogui.click(x=484, y=697)
time.sleep(1)
pyautogui.click(x=483, y=428)
time.sleep(1)
pyautogui.write('C:\\Users\\bandrezzo\\Downloads\\Cardápio Rodízio de Hamburguer.pdf')
time.sleep(0.4)
pyautogui.press('enter')
time.sleep(2)
pyautogui.press('enter')
time.sleep(1)
pyautogui.press('tab')
time.sleep(0.6)
pyautogui.press('space')
time.sleep(2.3)
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('space')
time.sleep(1)
pyautogui.click(x=428, y=619)
time.sleep(1)
pyautogui.click(x=552, y=591)
time.sleep(1)
pyautogui.press('pagedown')
time.sleep(0.8)
pyautogui.click(x=571, y=579)
time.sleep(0.5)
pyautogui.press('down')
time.sleep(0.8)
pyautogui.press('enter')
time.sleep(0.8)
pyautogui.press('tab')
time.sleep(0.5)
pyautogui.press('space')
time.sleep(0.5)
pyautogui.press('down')
time.sleep(0.5)
pyautogui.press('enter')
time.sleep(0.8)
pyautogui.press('tab')
time.sleep(0.5)
pyautogui.press('space')
time.sleep(0.5)
pyautogui.press('down')
time.sleep(0.5)
pyautogui.press('enter')
time.sleep(0.8)
pyautogui.press('tab')
time.sleep(0.5)
pyautogui.press('space')
time.sleep(0.5)
pyautogui.press('down')
time.sleep(0.5)
pyautogui.press('enter')
time.sleep(0.5)
pyautogui.press('tab')
time.sleep(0.5)
pyautogui.press('enter')
time.sleep(1)
pyautogui.click(x=439, y=207)
time.sleep(10)