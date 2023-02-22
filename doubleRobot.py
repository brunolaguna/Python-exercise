from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
import pyautogui

servico = Service(ChromeDriverManager().install())

driver = webdriver.Chrome(service=servico)
driver.set_window_size(1366, 768)
driver.maximize_window()
driver.get("https://blaze.com/pt/games/double")
time.sleep(5)
i=0
soma = 0
while i < 10:
    time.sleep(0.01)
    i+=1
    newRound = driver.find_element('xpath', '//*[@id="roulette"]/div/div[2]/div/div[2]/div/div[3]/div[1]/div[2]/span').text
    final_newRound = newRound.replace('R$ ','')
    float_final_newRound = float(final_newRound)
    if float_final_newRound <= 150.00:
        try:
            lastResult = driver.find_element('xpath', '//*[@id="roulette-recent"]/div/div[1]/div[1]/div/div/div').text
            new_lastResult = int(lastResult)
            if new_lastResult >= 8:
                print('Preto! O resultado foi', lastResult)
                soma+=1
                print(soma, 'rodada(s) sem sair o branco!')
                time.sleep(3)
            else:
                print('Vermelho! O resultado foi', lastResult)
                soma+=1
                print(soma, 'rodada(s) sem sair o branco!')
                time.sleep(3)
        except:
            print('0! O Branco está a solta!')
            soma = 0
            print("Zerou a soma das rodadas sem sair o branco!")
            time.sleep(3)
    i=0