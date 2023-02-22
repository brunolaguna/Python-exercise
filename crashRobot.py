from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
import pyautogui

servico = Service(ChromeDriverManager().install())

driver = webdriver.Chrome(service=servico)
driver.set_window_size(1366, 768)
driver.maximize_window()
driver.get("https://blaze.com/pt/games/crash")
time.sleep(5)
x = 0
soma = 0
pyautogui.hotkey('alt', 'tab')
while x < 10:
    time.sleep(0.05)
    valor_aposta_total = driver.find_element('xpath', '//*[@id="crash"]/div/div[2]/div[1]/div[1]/span[1]').text
    if valor_aposta_total <= '100':
        x = x + 1
        valor = driver.find_element('xpath', '//*[@id="crash-recent"]/div[2]/div[2]/span[1]').text
        valor = valor[:-1]
        print(valor)
        valor_float = float(valor)
        x = 0
        time.sleep(2)
        if valor_float < 2.00:
            soma = soma+1
            print(soma, 'valor(es) abaixo de 2.00X')
        else:
            soma = 0
            print("A soma zerou")
        if soma >= 4:
            soma = soma+1
            print("Está na hora de Apostar!")
            pyautogui.keyDown('ctrl')
            time.sleep(1)
            pyautogui.hotkey('shift', "'")
            time.sleep(1)
            pyautogui.keyUp('ctrl')
            time.sleep(1)
            pyautogui.write('start callMeQuick.py')
            pyautogui.keyDown('fn')
            time.sleep(1)
            pyautogui.hotkey('ctrl', 'f5')
            time.sleep(1)
            pyautogui.keyUp('fn')