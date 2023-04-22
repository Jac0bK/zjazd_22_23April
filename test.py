import unittest

class MojPrzypadekTestowy(unittest.TestCase):
    def setUp(self):
        print("Przygotowanie testu (warunki wstępne)")

    def testPierwszy(self):
        #zaczyna się od slowa "test"
        print("Test (kroki)")
        wynik_oczekiwany = 4
        wynik_rzeczywisty = 5
        self.assertEqual(wynik_oczekiwany, wynik_rzeczywisty)

    def tearDown(self):
        print("'Sprzątanie' po teście")

#sprawdzam czy ten modul jest modulem glownym
#(czy uruchomiono caly projekt z tego pliku)

if __name__ == "__main__":
    unittest.main()