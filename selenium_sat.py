import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import datetime


#https://topswagcode.com/xpath/
#https://flukeout.github.io/


#zmienna globalna (moze byc uzyta w kazdym przypadku
#driver = webdriver.Chrome()

class RegistrationTests(unittest.TestCase):
    def setUp(self):
        #przygotowanie testu (warunki wstępne0
        #1. Otwarta strona glowna
        #1a) tworze instancje klasy Chrome()
        self.driver = webdriver.Chrome()    # zmienna lokalna z uzycie self
        # maksymalizacja okna
        self.driver.maximize_window()
        #1b) otwieram strone glowna
        self.driver.get("https://www.eobuwie.com.pl/")
        #cookie accept
        cookie_accept = self.driver.find_element(By.XPATH, '//div[@class="e-consents-alert__actions"]/button[1]')
        cookie_accept.click()

    def tearDown(self):
        #wylacz przegladarke
        self.driver.quit()



    def testNoNameEntered(self):
        #Kroki
        #1a) kliknij zarejestruj
        #1b)
        zarejestruj_a = self.driver.find_element(By.PARTIAL_LINK_TEXT, "Zarejestruj")
        zarejestruj_a.click()

