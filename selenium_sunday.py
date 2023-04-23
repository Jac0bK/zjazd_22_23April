#https://topswagcode.com/xpath/
#https://flukeout.github.io/
#https://saucelabs.com/resources/blog/selenium-4-relative-locators

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
from time import sleep

# DANE TESTOWE
nazwisko = "Nowak"
email = "jan.nowak@mail.com"
haslo = "qwerty123!"

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
        sleep(3)

    def tearDown(self):
        # Wyłącz przeglądarkę
        self.driver.quit()

    def testNoNameEntered(self):
        # KROKI
        # 1. Kliknij „Zarejestruj”
        # 1a) Odszukaj przycisk Zarejestruj
        # 1b) Kliknij ten przycisk
        zarejestruj_a = self.driver.find_element(By.XPATH, '//a[@data-testid="header-register-link"]')
        zarejestruj_a.click()
        # 2. Wpisz nazwisko
        # Odszukaj, wpisz
        nazwisko_input = self.driver.find_element(By.ID, "lastname")
        nazwisko_input.send_keys(nazwisko)
        # 3. Wpisz email
        email_input = self.driver.find_element(By.ID, "email_address")
        email_input.send_keys(email)
        # 4. Wpisz haslo
        password_input = self.driver.find_element(By.ID, "password")
        password_input.send_keys(haslo)
        # 4a) Powtorz haslo
        password_conf_input = self.driver.find_element(By.ID, "confirmation")
        password_conf_input.send_keys(haslo)
        # 5 Zaznacz zgode
        checkbox_check = self.driver.find_element(By.XPATH, '//label[@class="checkbox-wrapper__label"]')
        checkbox_check.click()
        #kliknij pole zaloz konto w celu wywolania pola
        zaloz_konto = self.driver.find_element(By.ID, "create-account")
        zaloz_konto.click()
        sleep(5)
        #uwaga tu bedzie test
        #oczekiwany rezultat
        #a) szukam wsztkich elementow (informacja o bledzie uzytkownika - puste pola)
        errors = self.driver.find_elements(By.XPATH, '//span[@class="form-error"]')
        #b) sprawdzam czy jest tylko jeden taki element
        self.assertEqual(1, len(errors))
        #c) sprawdzam tresc komunikatu i jego widocznosc
        self.assertEqual("To pole jest wymagane", errors[0].text)   #z użyciem .text sprawdzamy czy jest widoczny bo inaczej lista bylaby pusta
        #d) sprawdzam czy komunikat jest pod polem imie ( i nad nazwiskiem)
        imie_input = self.driver.find_element(By.ID, "firstname")
        errors2 = self.driver.find_elements(locate_with(By.XPATH, '//span[@class="form-error"]').near(imie_input))
        #e) sprawdzam czy element zawarty wewnatrz listy errors oraz errors2 to ten sam element
        self.assertEqual(errors[0].id, errors2[0].id)
        #print(errors2[0])
        #print(type(errors2[0]))
        #print(dir(errors2[0]))

        sleep(2)

