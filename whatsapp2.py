from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import os

import webbrowser
import pyautogui
from time import sleep


class WhatsApp(object):
    def __init__ (self, url = "https://web.whatsapp.com"):
        print ('Constructing')
        # Inicializar el navegador (en este caso, Chrome)
        self.driver = webdriver.Chrome()
        # Abrir una página web (o realiza acciones en una página según tus necesidades)
        self.driver.get(url)
        
        #Espera el login hasta que carga el siguiente elemento.
        texto_esperado = "extremo a extremo."
        try:
            elemento = WebDriverWait(self.driver, 30).until(
                EC.text_to_be_present_in_element((By.CLASS_NAME, 'ubfBJ'), texto_esperado)
            )
            print ('Login Correcto')
        except Exception as e:
            print ('El login no ha ido bien')

    def find_user(self, phone):
        # Pulsar CTRL + ALT + N
        # Con esto abro una nueva conversación
        # Simular pulsación de teclas (CTRL + ALT + N)
        Keys_combination = Keys.CONTROL + Keys.ALT + 'n'
        # Puedes enviar la combinación de teclas a un elemento específico o al cuerpo de la página
        self.driver.find_element(By.TAG_NAME, 'body').send_keys(Keys_combination)
        sleep(0.1)
        pyautogui.write(phone, interval=0.1)
        pyautogui.press('enter')
        
        texto_a_buscar = "No se encontraron resultados"
        elementos_con_texto = self.driver.find_elements(By.XPATH, "//*[contains(text(), '" + texto_a_buscar + "')]")
        if elementos_con_texto:
            #no se encontro el número de telefono
            pyautogui.hotkey('esc')
            return False
        else:
            #hacer aquí lo que haya que jacer
            return True
            
    def send_message(self, message):
        pyautogui.write(message, interval=0.01)
        pyautogui.hotkey('enter')

    def send_picture(self, fichero):
        pyautogui.hotkey('shift', 'tab')
        pyautogui.hotkey('shift', 'tab')
        pyautogui.hotkey('enter')
        pyautogui.hotkey('down')
        pyautogui.hotkey('down')
        pyautogui.hotkey('enter')
        file = os.path.realpath(fichero)
        sleep(1)
        pyautogui.write(file)
        pyautogui.press('enter')
        sleep(1)
        pyautogui.hotkey('tab')
        pyautogui.hotkey('tab')
        pyautogui.hotkey('tab')
        pyautogui.hotkey('tab')
        pyautogui.press('enter')

    def send_file(self, fichero):
        pyautogui.hotkey('shift', 'tab')
        pyautogui.hotkey('shift', 'tab')
        pyautogui.hotkey('enter')
        pyautogui.hotkey('down')
        pyautogui.hotkey('enter')
        file = os.path.realpath(fichero)
        sleep(1)
        pyautogui.write(file)
        pyautogui.press('enter')
        sleep(1)
        pyautogui.hotkey('tab')
        pyautogui.hotkey('tab')
        pyautogui.hotkey('tab')
        pyautogui.hotkey('tab')
        pyautogui.press('enter')

    def __del__(self):
        self.driver.quit()

