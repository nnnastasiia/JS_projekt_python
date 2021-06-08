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
        przechowywaczMonet=PrzechowywaczMonet()
        self.parkomat = Parkomat(master, przechowywaczMonet)

    def test_niepopawny_format_daty_set(self):
        '''
        Test sprawdza poprawność formatu podanej daty
        '''

        #data1 = datetime.datetime.now()
        self.parkomat.getData.delete(0, END)
        self.parkomat.getData.insert(0, "2000-03-30 22:30:00")

        self.assertRaises(parkomatNiepoprawnyFormatDaty, lambda self=self : self.parkomat.countPieniadze())

    def test_4godziny_po_aktualnym_czasie(self):
        '''
        Test spzawdza, czy po wrzyceniu odpowiedniej wartości doda się odpowiedni czas
        '''
        self.parkomat.akt_data_click()
        data1 = self.parkomat.getData.get()
        data1 = datetime.datetime.strptime(data1, "%d/%m/%Y %H:%M:%S")


        self.parkomat.przechowywaczMonet.dodaj_monete(m2)
        self.parkomat.countPieniadze()
        self.assertEqual(self.parkomat.data_odj, (data1 + timedelta(minutes=60)).strftime("%d/%m/%Y %H:%M:%S"))

        self.parkomat.przechowywaczMonet.dodaj_monete(m2)
        self.parkomat.przechowywaczMonet.dodaj_monete(m2)
        self.parkomat.countPieniadze()
        self.assertEqual(self.parkomat.data_odj, (data1 + timedelta(minutes=120)).strftime("%d/%m/%Y %H:%M:%S"))

        self.parkomat.przechowywaczMonet.dodaj_monete(m5)
        self.parkomat.countPieniadze()
        self.assertEqual(self.parkomat.data_odj, (data1 + timedelta(minutes=180)).strftime("%d/%m/%Y %H:%M:%S"))

        self.parkomat.przechowywaczMonet.dodaj_monete(m5)
        self.parkomat.countPieniadze()
        self.assertEqual(self.parkomat.data_odj, (data1 + timedelta(minutes=240)).strftime("%d/%m/%Y %H:%M:%S"))


    # def test_polgodziny_za_1zl(self):
    #     '''
    #     Test sprawdza czy po wrzuceniu 1 zł doda się pół godziny
    #     '''
    #     self.parkomat.getData = datetime.combine(date(2021, 6, 8), time(13, 15, 00))

    #     self.parkomat.przechowywaczMonet.dodaj_monete(m1)

    #     self.assertEqual(self.parkomat.data_odj, datetime(2021, 6, 8, 13, 45, 00))

    # def test_plus_1godzina_monetami_z_mala_wartoscia(self):
    #     '''
    #     Test sprawdza, czy po wrzyceniu odpowiedniej wartości monetami 1 g doda odpowiednia godzina
    #     '''
    #     self.parkomat.resetParkomat()
    #     self.parkomat.getData = datetime.combine(date(2021, 6, 8), time(14, 30, 00))

    #     for _ in range(200):
    #         self.parkomat.przechowywaczMonet.dodaj_monete(m001)

    #     self.assertEqual(self.parkomat.data_odj, datetime(2021, 6, 8, 15, 30, 00))

    # def test_pelny_parkomat_error(self):
    #     '''
    #     Test sprawdza, czy po wrzyceniu za duzo monet, program wypisze bląd o przepelnieniu
    #     '''
    #     self.parkomat.resetParkomat()
    #     self.parkomat.getData = datetime.combine(date(2021, 6, 8), time(19, 40, 00))

    #     with self.assertRaises(parkomatFullException):
    #         for _ in range(201):
    #             self.parkomat.przechowywaczMonet.dodaj_monete(m001)


    # def test_nie_wrzucono_pieniadze_error(self):
    #     '''
    #     Test sprawdza, czy jeżeli nie wrzuconożadnej monety, program wypisze bląd, że nie wrzucono żadnej monety
    #     '''
    #     self.parkomat.reset()
    #     self.parkomat.getData = datetime.combine(date(2021, 6, 8), time(11, 40, 00))
    #     self.parkomat.registration_number = "WR0101L"

    #     self.assertRaises(parkomatNieWrzuconoPieniadze, self.parkomat.zatw_click)

    def test_pusty_numer_rejestracyjny_pojazdu_error(self):
        '''
        Test sprawdza, czy jezeli nie podano numer pojadzu, 
        program wypisze bląd o postym lub niepoprawnym numerze pojazdy
        '''
        self.assertRaises(parkomatPustyNumerRejestracyjnyExeption, lambda self=self : self.parkomat.dodajnr_click())
        
        self.parkomat.akt_data_click()
        self.parkomat.przechowywaczMonet.dodaj_monete(m2)
        self.parkomat.countPieniadze()

        self.assertRaises(parkomatPustyNumerRejestracyjnyExeption, lambda self=self : self.parkomat.zatw_click())

    
    def test_niepoprawny_numer_rejestracyjny_pojazdu_error(self):
        '''
        Test sprawdza, czy jezeli podano niepoprawny numer rejestracyjny pojazdu, 
        program wypisze bląd o postym lub niepoprawnym numerze pojazdy
        '''
        self.parkomat.getNrPoj.insert(0, "wr000001010111")
        self.assertRaises(parkomatNiepoprawnyNumerRejestracyjnyExeption, lambda self=self : self.parkomat.dodajnr_click())
        
        self.parkomat.akt_data_click()
        self.parkomat.przechowywaczMonet.dodaj_monete(m2)
        self.parkomat.countPieniadze()

        self.assertRaises(parkomatNiepoprawnyNumerRejestracyjnyExeption, lambda self=self : self.parkomat.zatw_click())




if __name__ == "__main__":
    unittest.main()