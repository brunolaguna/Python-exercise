# Standardize date and time to the insight ticket

import pyautogui
import time

# Import date and time
from datetime import datetime

# Just Import date
from datetime import date

# Get date and time
currentDateAndTime = datetime.now()
currentTime = currentDateAndTime.strftime("%Hh%Mmin")

# Get just the date
today = date.today()

#Print date like this
currentDate = today.strftime("%d_%m_%Y-")  

time.sleep(3)
print(pyautogui.position())

# Convert the variable to a list
tempo = list(currentTime)
print(tempo)

# Erasing the zero before the numbers
if tempo[0] == '0':
    tempo[0] = ''

if tempo[3] == '0':
    tempo[3] = ''

# Convert the variable to a list
data = list(currentDate)
print(data)

# Erasing the zero before the numbers
if data[0] == '0':
    data[0] = ''

#tempo[1] = 2
#print(tempo)
str(tempo)
stringTempo = "".join(tempo)
stringData = "".join(data)
print(stringTempo)
print(stringData)

#str(tempo).strip('[]')
#print(tempo)

#currentTime.replace('0', '')

#print(currentTime)

#if currentTime[2] == 0:

#pyautogui.keyDown("alt")
#
#pyautogui.press("tab")
#pyautogui.press("tab")
#
#pyautogui.keyUp("alt")
