from errors import *
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from decimal import Decimal
from parkomat_money.pieniadze import *


class PrzechowywaczMonet:
    def __init__(self):
        self._lista_monet = []

    def esli5zl(self):
        if len(self._lista_monet) == 1:
            if self._lista_monet[0].pobierz_wartosc() == 5:
                return True
        return False

    def dodaj_monete(self, moneta):
        try:
            if isinstance(moneta, Pieniadze):
                if len(self._lista_monet) < 200:
                    self._lista_monet.append(moneta)
                else:
                    raise parkomatFullException
        except parkomatFullException as pFE:
            messagebox.showinfo(
                "Parkomat pelny", "Przepraszamy, parkomat jest pelny")

    def suma(self):
        suma_monet = Decimal(0)
        for moneta in self._lista_monet:
            suma_monet = suma_monet + moneta.pobierz_wartosc()
        return suma_monet

    def reset(self):
        self._lista_monet = []
