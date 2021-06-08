import unittest
from datetime import datetime, date, timedelta, time
from Parkomat_app import Parkomat
from Parkomat_app.Parkomat import *
from parkomat_money.pieniadze import *
from parkomat_money.przechowywaczMonet import *
from errors import *

from tkinter import Tk


class testyParkomat(unittest.TestCase):

    def setUp(self):
        master = Tk()
        przechowywaczMonet = PrzechowywaczMonet()
        self.parkomat = Parkomat(master, przechowywaczMonet)

    def test_niepopawny_format_daty_set(self):
        '''
        Test sprawdza poprawność formatu podanej daty
        '''

        self.parkomat.getData.delete(0, END)
        self.parkomat.getData.insert(0, "2000-03-30 22:30:00")

        self.assertRaises(parkomatNiepoprawnyFormatDaty,
                          lambda self=self: self.parkomat.countPieniadze(False))

    def test_4godziny_po_aktualnym_czasie(self):
        '''
        Test spzawdza, czy po wrzyceniu odpowiedniej wartości doda się odpowiedni czas
        '''
        self.parkomat.akt_data_click()
        data1 = self.parkomat.getData.get()
        data1 = datetime.datetime.strptime(data1, "%d/%m/%Y %H:%M:%S")

        self.parkomat.przechowywaczMonet.dodaj_monete(m2, False)
        self.parkomat.countPieniadze(False)
        self.assertEqual(self.parkomat.data_odj, (data1 +
                         timedelta(minutes=60)).strftime("%d/%m/%Y %H:%M:%S"))

        self.parkomat.przechowywaczMonet.dodaj_monete(m2, False)
        self.parkomat.przechowywaczMonet.dodaj_monete(m2, False)
        self.parkomat.countPieniadze(False)
        self.assertEqual(self.parkomat.data_odj, (data1 +
                         timedelta(minutes=120)).strftime("%d/%m/%Y %H:%M:%S"))

        self.parkomat.przechowywaczMonet.dodaj_monete(m5, False)
        self.parkomat.countPieniadze(False)
        self.assertEqual(self.parkomat.data_odj, (data1 +
                         timedelta(minutes=180)).strftime("%d/%m/%Y %H:%M:%S"))

        self.parkomat.przechowywaczMonet.dodaj_monete(m5, False)
        self.parkomat.countPieniadze(False)
        self.assertEqual(self.parkomat.data_odj, (data1 +
                         timedelta(minutes=240)).strftime("%d/%m/%Y %H:%M:%S"))

    def test_polgodziny_za_1zl(self):
        '''
        Test sprawdza czy po wrzuceniu 1 zł doda się pół godziny
        '''
        self.parkomat.akt_data_click()
        data = self.parkomat.getData.get()
        data = datetime.datetime.strptime(data, "%d/%m/%Y %H:%M:%S")

        self.parkomat.przechowywaczMonet.dodaj_monete(m1, False)
        self.parkomat.countPieniadze(False)

        dataEnd = self.parkomat.data_odj
        dataEnd = datetime.datetime.strptime(dataEnd, "%d/%m/%Y %H:%M:%S")

        self.assertEqual(dataEnd, (data + timedelta(minutes=30)))

    def test_plus_1godzina_monetami_z_mala_wartoscia(self):
        '''
        Test sprawdza, czy po wrzyceniu odpowiedniej wartości monetami 1 g doda odpowiednia godzina
        '''
        self.parkomat.akt_data_click()
        data = self.parkomat.getData.get()
        data = datetime.datetime.strptime(data, "%d/%m/%Y %H:%M:%S")

        for _ in range(200):
            self.parkomat.przechowywaczMonet.dodaj_monete(m001, False)

        self.parkomat.countPieniadze(False)

        dataEnd = self.parkomat.data_odj
        dataEnd = datetime.datetime.strptime(dataEnd, "%d/%m/%Y %H:%M:%S")

        self.assertEqual(dataEnd, (data + timedelta(hours=1)))

    def test_pelny_parkomat_error(self):
        '''
        Test sprawdza, czy po wrzyceniu za duzo monet, program wypisze bląd o przepelnieniu
        '''
        self.parkomat.akt_data_click()

        with self.assertRaises(parkomatFullException):
            for _ in range(201):
                self.parkomat.przechowywaczMonet.dodaj_monete(m001, False)

    def test_nie_wrzucono_pieniadze_error(self):
        '''
        Test sprawdza, czy jeżeli nie wrzucono żadnej monety, program wypisze bląd, że nie wrzucono żadnej monety
        '''
        self.parkomat.akt_data_click()
        self.parkomat.getNrPoj.insert(0, "WR0101L")

        self.assertRaises(parkomatNieWrzuconoPieniadze,
                          lambda self=self: self.parkomat.zatw_click(False))

    def test_pusty_numer_rejestracyjny_pojazdu_error(self):
        '''
        Test sprawdza, czy jezeli nie podano numer pojadzu, 
        program wypisze bląd o postym lub niepoprawnym numerze pojazdy
        '''
        self.assertRaises(parkomatPustyNumerRejestracyjnyExeption,
                          lambda self=self: self.parkomat.dodajnr_click())

        self.parkomat.akt_data_click()
        self.parkomat.przechowywaczMonet.dodaj_monete(m2, False)
        self.parkomat.countPieniadze(False)

        self.assertRaises(parkomatPustyNumerRejestracyjnyExeption,
                          lambda self=self: self.parkomat.zatw_click(False))

    def test_niepoprawny_numer_rejestracyjny_pojazdu_error(self):
        '''
        Test sprawdza, czy jezeli podano niepoprawny numer rejestracyjny pojazdu, 
        program wypisze bląd o postym lub niepoprawnym numerze pojazdy
        '''
        self.parkomat.getNrPoj.insert(0, "wr000001010111")
        self.assertRaises(parkomatNiepoprawnyNumerRejestracyjnyExeption,
                          lambda self=self: self.parkomat.dodajnr_click())

        self.parkomat.akt_data_click()
        self.parkomat.przechowywaczMonet.dodaj_monete(m2, False)
        self.parkomat.countPieniadze(False)

        self.assertRaises(parkomatNiepoprawnyNumerRejestracyjnyExeption,
                          lambda self=self: self.parkomat.zatw_click(False))


if __name__ == "__main__":
    unittest.main()
