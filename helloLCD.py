#!/usr/bin/python
#show "Hello World on the LCD screen"
#

import Adafruit_CharLCD as LCD
import time
import subprocess

lcd = LCD.Adafruit_CharLCDPlate()
Name = subprocess.check_output(['hostname']).strip()
IPaddr = subprocess.check_output(['hostname','-I'])
displaytext2 = IPaddr+Name
displayText = "Hello World"
lcd.clear()
lcd.message(displayText)
while (True):
    if lcd.is_pressed(LCD.SELECT):
        lcd.clear()
        lcd.message(displayText)
    else:
        lcd.clear()
        lcd.message(displaytext2)
    time.sleep(0.5)
