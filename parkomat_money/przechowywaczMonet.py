from errors import *
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from decimal import Decimal
from parkomat_money.pieniadze import *


class PrzechowywaczMonet:
    '''
    Klasa reprezentująca przechowywanie monet, wrzucenie i sumę wrzuconych monet
    '''
    def __init__(self):
        self._lista_monet = []

    def jesli5zl(self):
        if len(self._lista_monet) == 1:
            if self._lista_monet[0].pobierz_wartosc() == 5:
                return True
        return False

    def dodaj_monete(self, moneta, showMessage = True):     #funkcja dodająca monety odpowiedniej wartosci przy wrzuceniu do parkomatu
        counter = 0
        for mon in self._lista_monet:
            if (mon.pobierz_wartosc() == moneta.pobierz_wartosc()):
                counter += 1
        if counter == 200:
            if showMessage == True:
                 messagebox.showinfo(
                "Parkomat pelny", "Przepraszamy, parkomat jest pelny")
            raise parkomatPelnyException("Przepraszamy, parkomat jest pelny")
        
        
        self._lista_monet.append(moneta)

    def suma(self):             #funkcja sumująca wrzucone monety lub banknoty do parkomatu
        suma_monet = Decimal(0)
        for moneta in self._lista_monet:
            suma_monet = suma_monet + moneta.pobierz_wartosc()
        return suma_monet


    def reset(self):
        self._lista_monet = []