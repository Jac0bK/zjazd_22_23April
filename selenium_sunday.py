#https://topswagcode.com/xpath/
#https://flukeout.github.io/

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

class RegistrationTests(unittest.TestCase):
    def setUp(self):
        # Przygotowanie testu
        # 1. Otwarta strona główna
        # 1a) Tworzę instancję klasy Chrome()
        self.driver = webdriver.Chrome()
        # (Zmaksymalizuj okno)
        self.driver.maximize_window()
        # 1b) Otwieram stronę główną
        self.driver.get("https://www.eobuwie.com.pl/")
        cookie_accept = self.driver.find_element(By.XPATH, '//div[@class="e-consents-alert__actions"]/button[1]')
        cookie_accept.click()

    def tearDown(self):
        # Wyłącz przeglądarkę
        self.driver.quit()

    def testNoNameEntered(self):
        # KROKI
        # 1. Kliknij „Zarejestruj”
        # 1a) Odszukaj przycisk Zarejestruj
        # 1b) Kliknij ten przycisk
        # zarejestruj_a = self.driver.find_element(By.PARTIAL_LINK_TEXT, "Zarejestruj")
        # zarejestruj_a.click()
        sleep(4)
        pass