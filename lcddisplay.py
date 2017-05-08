
#!/usr/bin/python
# Example using a character LCD connected to a Raspberry Pi
import time
import Adafruit_CharLCD as LCD
import read_arduino
# Raspberry Pi pin setup

lcd_rs = 25
lcd_en = 24
lcd_d4 = 23
lcd_d5 = 17
lcd_d6 = 18
lcd_d7 = 22
lcd_backlight = 2

# Define LCD column and row size for 16x
lcd_columns = 16
lcd_rows = 2

lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows, lcd_backlight)
def weight(fruitWeight):
        lcd.clear()
	lcd.message('Calculating weight...')
	time.sleep(2)
	lcd.clear()
	#res=read_arduino.getweight()
	#print(res)
	lcd.message('Weight=%s gm'%(fruitWeight))

	time.sleep(3)
	lcd.clear()

#weight(read_arduino.getweight())
def fruitName(fruitName):
        lcd.clear()

        lcd.message("%s" %str(fruitName))

        time.sleep(3)
        lcd.clear()
def Nutrients(values):
        lcd.clear()
	
	Nutrientsname=["calories","protein","fat","sugar"]
	for i,x in enumerate(values):
		lcd.message(Nutrientsname[i]+"=%s"%str(x))
		time.sleep(2)
		lcd.clear()
def Display():
	lcd.message("Place RFID")
def Authenticate():
        lcd.clear()
        lcd.message("Authenticating...")
def Username(name):
        lcd.clear()
        lcd.message("Welcome %s" %name)

	

