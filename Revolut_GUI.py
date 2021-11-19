from time import sleep
import pyautogui

pyautogui.PAUSE = 2.5

def buy(stock, amount):
	try:
		
		R_location = None
		while R_location is None:
			R_location = pyautogui.locateOnScreen('R.png', confidence = 0.9)
				
		pyautogui.click(pyautogui.center(R_location))

		
		one_location = None
		while one_location is None:
			one_location = pyautogui.locateOnScreen('1.png', confidence = 0.9)
		
		pyautogui.click('1.png')
		pyautogui.click('4.png')
		pyautogui.click('5.png')
		pyautogui.click('2.png')
		
		azioni_location = None
		while azioni_location is None:
			azioni_location = pyautogui.locateOnScreen('azioni.png', confidence = 0.9)
				
		pyautogui.click(pyautogui.center(azioni_location))
		
		investi_location = None
		while investi_location is None:
			investi_location = pyautogui.locateOnScreen('investi.png', confidence = 0.9)
		
		pyautogui.click(pyautogui.center(investi_location))
		
		cerca_location = None
		while cerca_location is None:
			cerca_location = pyautogui.locateOnScreen('cerca.png', confidence = 0.9)
		
		pyautogui.click(pyautogui.center(cerca_location))
		
		dollaro_location = None
		while dollaro_location is None:
			dollaro_location = pyautogui.locateOnScreen('dollaro.png', confidence = 0.9)
		
		pyautogui.click(pyautogui.center(dollaro_location))

		
		back_location = None
		while back_location is None:
			back_location = pyautogui.locateOnScreen('back.png', confidence = 0.9)
		
		pyautogui.click(pyautogui.center(back_location))

		
		sleep(2)
		pyautogui.write(stock)
		
		dollaro_location = None
		while dollaro_location is None:
			dollaro_location = pyautogui.locateOnScreen('dollaro.png', confidence = 0.9)
		
		pyautogui.click(pyautogui.center(dollaro_location))

		
		compra_location = None
		while compra_location is None:
			compra_location = pyautogui.locateOnScreen('compra.png', confidence = 0.9)
		
		pyautogui.click(pyautogui.center(compra_location))

		
		saldo_location = None
		while saldo_location is None:
			saldo_location = pyautogui.locateOnScreen('saldo.png', confidence = 0.9)
		
		pyautogui.write(amount)

		acquista_location = None
		while acquista_location is None:
			acquista_location = pyautogui.locateOnScreen('acquista.png', confidence = 0.9)
		
		pyautogui.click(pyautogui.center(acquista_location))

		
		reset_1_location = None
		while reset_1_location is None:
			reset_1_location = pyautogui.locateOnScreen('reset_1.png', confidence = 0.9)
		
		pyautogui.click(pyautogui.center(reset_1_location))

		
		bin_location = None
		while bin_location is None:
			bin_location = pyautogui.locateOnScreen('bin.png', confidence = 0.9)
		
		pyautogui.click(pyautogui.center(bin_location))

		return print('Stock acquistato')
		
	except Exception as e:
		print(e)
		
	

buy('AMD', '5')
