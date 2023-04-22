import unittest
from selenium import webdriver
import datetime

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
        # 1b) otwieram strone glowna
        self.driver.get("https://www.eobuwie.com.pl/")



    def testNoNameEntered(self):
        pass
