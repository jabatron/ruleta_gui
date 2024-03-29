"""
ORIGINAL:
Alright is unofficial Python wrapper for whatsapp web made as an inspiration from PyWhatsApp
allowing you to send messages, images, video and documents programmatically using Python 

MODIFICADO (ja):
He tenido que retocar el XPATH de enviar mensajes porque no los enviaba.
También he modificado el envio de imagenes por le mismo motivo.
"""


import os
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import UnexpectedAlertPresentException

import pyautogui


class WhatsApp(object):
    def __init__(self):
        self.BASE_URL = 'https://web.whatsapp.com/'
        self.suffix_link = 'https://wa.me/'
        chrome_options = Options()
        chrome_options.add_argument("start-maximized")
        chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
        chrome_options.add_argument("service_log_path=NUL")
        #chrome_options.add_argument('--user-data-dir=./User_Data')
        self.browser = webdriver.Chrome(options=chrome_options)
        self.wait = WebDriverWait(self.browser, 600)
        self.login()
        self.mobile = ''


    def login(self):
        self.browser.get(self.BASE_URL)
        action_button = self.wait.until(EC.presence_of_element_located(
            #    (By.XPATH, '//*[@id="action-button"]')))
                (By.XPATH, '//*[@id="side"]/div[1]/div/button/div/span')))
        
        time.sleep(1)
        #self.browser.maximize_window()

    def get_phone_link(self, mobile) -> str:
        """get_phone_link (), create a link based on whatsapp (wa.me) api

        Args:
            mobile ([type]): [description]

        Returns:
            str: [description]
        """
        return f'{self.suffix_link}{mobile}'

    def find_user(self, mobile) -> None:
        """find_user()
        Makes a user with a given mobile a current target for the wrapper

        Args:
            mobile ([type]): [description]
        """
        try:
            self.mobile = mobile
            link = self.get_phone_link(mobile)
            self.browser.get(link)
            action_button = self.wait.until(EC.presence_of_element_located(
            #    (By.XPATH, '//*[@id="action-button"]')))
                (By.XPATH, '//*[@id="action-button"]')))
            action_button.click()
            time.sleep(1)
            go_to_web = self.wait.until(EC.presence_of_element_located(
                # (By.XPATH, '//*[@id="fallback_block"]/div/div/a'))) 
                (By.XPATH, '//*[@id="fallback_block"]/div/div/h4[2]/a'))) 
            go_to_web.click()
            time.sleep(1)
        except UnexpectedAlertPresentException as bug:
            print(bug)
            time.sleep(1)
            self.find_user(mobile)

    def send_message(self, message):
        """send_message ()
        Sends a message to a target user 

        Args:
            message ([type]): [description]
        """
        try:
            # RETOCADO
            # inp_xpath = '//*[@id="main"]/footer/div[1]/div/div/div[2]/div[1]/div/div[2]'
            # cambio 6/12/2021 
            #inp_xpath = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]'
            #inp_xpath = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div[2]/div[1]/p'
            inp_xpath = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p'

            input_box = self.wait.until(
                EC.presence_of_element_located((By.XPATH, inp_xpath)))
            input_box.send_keys(message + Keys.ENTER)
            print(f"Message sent successfuly to {self.mobile}")
        except (NoSuchElementException, Exception) as bug:
            print(bug)
            print(f'Failed to send a PDF to {self.mobile}')

        finally:
            print("send_message() finished running ")

    def find_attachment(self):
        clipButton = self.wait.until(EC.presence_of_element_located(
            (By.XPATH,'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div/div/div/div/span')))
        clipButton.click()
              
    def send_attachment(self):
        # Waiting for the pending clock icon to disappear
        self.wait.until_not(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="main"]//*[@data-icon="msg-time"]')))

        sendButton = self.wait.until(EC.presence_of_element_located(
            #(By.XPATH, '//*[@id="app"]/div[1]/div[1]/div[2]/div[2]/span/div[1]/span/div[1]/div/div[2]/div/div[2]/div[2]/div/div/span')))
            (By.XPATH, '//*[@id="app"]/div/div/div[3]/div[2]/span/div/span/div/div/div[2]/div/div[2]/div[2]/div')))
        
                        
        sendButton.click()
        
        time.sleep(12)    

    def send_picture(self, picture):
        """send_picture ()

        Sends a picture to a target user

        Args:
            picture ([type]): [description]
        """
        try:
            filename = os.path.realpath(picture)
            self.find_attachment()
            # To send an Image
            imgButton = self.wait.until(EC.presence_of_element_located(
                #(By.XPATH, '//*[@id="main"]/footer//*[@data-icon="attach-image"]/../input')))
                #(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/span/div/ul/div/div[2]/li')))
                (By.XPATH,'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div/div/span/div/ul/div/div[2]/li')))
                            
            imgButton.click()
            time.sleep(1)
            pyautogui.hotkey('alt', 'm')
            pyautogui.write(filename)
            pyautogui.press('enter')

            time.sleep(1)
            self.send_attachment()
            print(f"Picture has been successfully sent to {self.mobile}")
        except (NoSuchElementException, Exception) as bug:
            print(bug)
            print(f'Failed to send a picture to {self.mobile}')

        finally:
            print("send_picture() finished running ")

    def send_video(self, video):
        """send_video ()

        Sends a video to a target user

        Args:
            video ([type]): [description]
        """
        try:
            filename = os.path.realpath(video)
            self.find_attachment()
            # To send a Video
            video_button = self.wait.until(EC.presence_of_element_located(
                (By.XPATH, '//*[@id="main"]/footer//*[@data-icon="attach-image"]/../input')))
            video_button.send_keys(filename)
            self.send_attachment()
            print(f'Video has been successfully sent to {self.mobile}')
        except (NoSuchElementException, Exception) as bug:
            print(bug)
            print(f'Failed to send a video to {self.mobile}')
        finally:
            print("send_video() finished running ")

    def send_file(self, filename):
        """send_file()

        Sends a file to target user

        Args:
            filename ([type]): [description]
        """
        try:
            filename = os.path.realpath(filename)
            self.find_attachment()
            #document_button = self.wait.until(EC.presence_of_element_located(
            #    (By.XPATH, '//*[@id="main"]/footer//*[@data-icon="attach-document"]/../input')))
            file_button = self.wait.until(EC.presence_of_element_located(
                (By.XPATH,'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div/div/span/div/ul/div/div[1]/li')))
            file_button.click()
            time.sleep(1)
            pyautogui.hotkey('alt', 'm')
            pyautogui.write(filename)
            pyautogui.press('enter')

            time.sleep(1)
            self.send_attachment()
        except (NoSuchElementException, Exception) as bug:
            print(bug)
            print(f'Failed to send a PDF to {self.mobile}')
        finally:
            print("send_file() finished running ")

    def __del__(self):
        self.browser.quit()