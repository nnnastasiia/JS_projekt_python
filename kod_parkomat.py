import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Frame, Label
import datetime
from datetime import timedelta
import random
from threading import Timer
from time import sleep
from collections import OrderedDict
from tkinter import *  
from tkinter import ttk  
from tkinter import Entry, Label, Button
from tkinter.messagebox import showinfo
from tkinter import StringVar
from decimal import Decimal
from typing import Tuple


#Pieniądze
class Pieniadze:
    def __init__(self, wartosc):
        try:
            if wartosc in {0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1, 2, 5, 10, 20, 50}:
                self._wartosc = Decimal(str(wartosc))
            else:
                raise ZlyNominalException("Nieznany nominal")
        except ZlyNominalException as zne:
            print(zne.message)

    def pobierz_wartosc(self):
        return  self._wartosc
        
m001 = Pieniadze(0.01)
m002 = Pieniadze(0.02)
m005 = Pieniadze(0.05)
m01 = Pieniadze(0.1)
m02 = Pieniadze(0.2) 
m05 = Pieniadze(0.5)
m1 = Pieniadze(1)
m2 = Pieniadze(2)
m5 = Pieniadze(5)
m10 = Pieniadze(10)
m20 = Pieniadze(20)
m50 = Pieniadze(50)

class PrzechowywaczMonet:  
    def __init__(self):
        self._lista_monet = []
    def dodaj_monete(self, moneta):
        try:
            if isinstance(moneta, Pieniadze):
                if len(self._lista_monet) < 200:
                    self._lista_monet.append(moneta)
                else:
                    raise parkomatFullExeption ("Parkomat jest pelny")
        except parkomatFullExeption as pFE:
            showinfo("Pakromat pelny", "Przepraszamy, parkomat jest pelny")

    def suma(self):
        suma_monet = Decimal(0)
        for moneta in self._lista_monet:
            suma_monet = suma_monet + moneta.pobierz_wartosc()
        return suma_monet
        
    def reset(self):
        self._lista_monet = []
        
class Parkomat():
    
    def __init__(self, master, przech):
        self._master = master
        self.przechowywaczMonet = przech
        self._current_delta = timedelta(seconds=0)
        
        
        self._master.title("Parkomat")
    
        
    
        Label(self._master, text = " ")

        frame_coins1 = Frame(self._master)
        frame_coins1.pack(fill=BOTH, expand=True)

        button1g = Button(frame_coins1, text="1g", width=12, bg='bisque2',\
                          command= lambda self=self: [self.przechowywaczMonet.dodaj_monete(m001), self.countPieniadze()]).pack(side = LEFT, padx=5, pady=5)

        button2g = Button(frame_coins1, text="2g", width=12, bg='bisque2',\
                          command= lambda self=self: [self.przechowywaczMonet.dodaj_monete(m002), self.countPieniadze()]).pack(side = LEFT, padx=5, pady=5)

        button5g = Button(frame_coins1, text="5g", width=12, bg='bisque2',\
                          command= lambda self=self: [self.przechowywaczMonet.dodaj_monete(m005), self.countPieniadze()]).pack(side = LEFT, padx=5, pady=5)

        frame_coins2 = Frame(self._master)
        frame_coins2.pack(fill=BOTH, expand=True)

        button10g = Button(frame_coins2, text="10g", width=12, bg='MistyRose2',\
                          command= lambda self=self: [self.przechowywaczMonet.dodaj_monete(m01), self.countPieniadze()]).pack(side = LEFT, padx=5, pady=5)

        button20g = Button(frame_coins2, text="20g", width=12, bg='MistyRose2',\
                          command= lambda self=self: [self.przechowywaczMonet.dodaj_monete(m02), self.countPieniadze()]).pack(side = LEFT, padx=5, pady=5)

        button50g = Button(frame_coins2, text="50g", width=12, bg='MistyRose2',\
                          command= lambda self=self: [self.przechowywaczMonet.dodaj_monete(m05), self.countPieniadze()]).pack(side = LEFT, padx=5, pady=5)

        frame_coins3 = Frame(self._master)
        frame_coins3.pack(fill=BOTH, expand=True)

        button1zl = Button(frame_coins3, text="1zł", width=12, bg='LightPink1',\
                          command= lambda self=self: [self.przechowywaczMonet.dodaj_monete(m1), self.countPieniadze()]).pack(side = LEFT,padx=5, pady=5)

        button2zl = Button(frame_coins3, text="2zł", width=12, bg='LightPink1',\
                          command= lambda self=self: [self.przechowywaczMonet.dodaj_monete(m2), self.countPieniadze()]).pack(side = LEFT,padx=5, pady=5)

        button5zl = Button(frame_coins3, text="5zł", width=12, bg='LightPink1',\
                          command= lambda self=self: [self.przechowywaczMonet.dodaj_monete(m5), self.countPieniadze()]).pack(side = LEFT,padx=5, pady=5)

        frame_banktoty1 = Frame(self._master)
        frame_banktoty1.pack(fill=BOTH, expand=True)

        button10zl = Button(frame_banktoty1, text="10zł", width=12, bg='HotPink1',\
                          command= lambda self=self: [self.przechowywaczMonet.dodaj_monete(m10), self.countPieniadze()]).pack(side = LEFT,padx=5, pady=5)

        button20zl = Button(frame_banktoty1, text="20zł", width=12, bg='HotPink1',\
                          command= lambda self=self: [self.przechowywaczMonet.dodaj_monete(m20), self.countPieniadze()]).pack(side = LEFT,padx=5, pady=5)

        button50zl = Button(frame_banktoty1, text="50zł", width=12, bg='HotPink1',\
                          command= lambda self=self: [self.przechowywaczMonet.dodaj_monete(m50), self.countPieniadze()]).pack(side = LEFT,padx=5, pady=5)


        self.nrPoj_lbl = Label(frame_coins1, text="Numer rejest.pojazdu:")
        self.nrPoj_lbl.pack(side = LEFT,padx=5, pady=5)
        self.getNrPoj = Entry(frame_coins1, width = 20)
        self.getNrPoj.pack(side=LEFT, padx=10)
        self.dodajnr_button = Button(frame_coins1, text= "Dodaj", width = 10, command = self.dodajnr_click, bg='alice blue')
        self.dodajnr_button.pack(side = LEFT, padx=5, pady=5)

        self.data_park = Label(frame_coins2, text="Data parkowania:")
        self.data_park.pack(side = LEFT,padx=5, pady=5)
        self.getData = Entry(frame_coins2, width=20)
        self.getData.pack(side=LEFT, padx=10)
        #getData.insert(END, datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))


        self.akt_data_button = Button(frame_coins2, text="Akt. data", width=10, command = self.akt_data_click, bg='alice blue')
        self.akt_data_button.pack(side = LEFT, padx=5, pady=5)


        self.czas_label = Label(frame_coins3, text="Czas wyjazdu:")
        self.czas_label.pack(side = LEFT,padx=5, pady=5)

        self.zaplacono_lbl = Label(frame_banktoty1, text="Zaplacono:")
        self.zaplacono_lbl.pack(side=LEFT, padx=5, pady=5)

        Button(self._master, text="Anuluj", command = self.closeWindow, bg='IndianRed1').pack(side = RIGHT,padx=5, pady=5)
        Button(self._master, text="Zatwierdz",command = self.zatw_click, bg='lawn green').pack(side = RIGHT,padx=5, pady=5)

            
        self._master.mainloop()
        
    def closeWindow(self):
        self._master.destroy() 

    def dodajnr_click(self):
        NrPoj = self.getNrPoj.get()
            
        if (len(NrPoj)==0):
            raise parkomatPustyNumerRejestracyjnyExeption
        elif (len(NrPoj)>9):
            raise parkomatNiepoprawnyNumerRejestracyjnyExeption

        self.nrPoj_lbl.config(text = "Numer rejest.pojazdu:  " + str(NrPoj.upper()))
        self.getNrPoj.pack_forget()
        self.dodajnr_button.pack_forget()
        
    def akt_data_click(self):
        self.getData.delete(0, END)
        self.getData.insert(0, datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))
        
        
    def countPieniadze(self):
        wplacono = self.przechowywaczMonet.suma()
        data1 = self.getData.get()

        self.data_park.config(text = "Data parkowania:  " + data1)
        self.getData.pack_forget()
        self.akt_data_button.pack_forget()

        if wplacono <= Decimal('2'):
            timedelta1 = timedelta(seconds=float(wplacono/Decimal('2')*3600))
            self.czas_label.config(text='Czas wyjazdu: ' + str(data1 + str(timedelta1)))
            return
        wplacono -= Decimal('2')
        timedelta1 = timedelta(seconds=3600)
            
        if total_value <= Decimal('4'):
            timedelta1 += timedelta(seconds=float(wplacono/Decimal('4')*3600))
            self.czas_label.config(text='Czas wyjazdu: ' + str(data1 + str(timedelta1)))
            return
        wplacono -= Decimal('4')
        timedelta1 += timedelta(seconds=3600)
            
        timedelta1 = timedelta(seconds=float(wplacono/Decimal('5')*3600))
        self.czas_label.config(text='Czas wyjazdu: ' + str(data1 + str(timedelta1)))
        
    def zatw_click(self):
        NrPoj = self.getNrPoj.get()
        term = self.getData.get()

        messagebox.showinfo("Sukces!", "Numer rejestracyjny pojazdu:"+ str(NrPoj.upper()) + "\nWplacono:"+ str((round(wplacono/100.0,2)))+"\nTermin wyjazdu: ")
             
        
    
       

    
from tkinter import Tk 

root = tk.Tk()
przechowywaczMonet = PrzechowywaczMonet()
my_window = Parkomat(root, przechowywaczMonet)   
        
        
        
        
        
        

class parkomatExeption(Exeption):
    '''
    Klasa ogólna dla wszystkich wyjątków
    '''
class ZlyNominalException(Exception):
    '''
    Wyjątek zgłoszony, jeśli wplacona nieznana wartosc
    '''
    def __init__(self,message):
        self.message = message
class parkomatFullException(parkomatException):
    '''
    Wyjątek zgłoszony, jeśli parkomat jest pelny
    '''
class parkomatNiepoprawnyNumerRejestracyjnyExeption(parkomatExeption):
    '''
    Wyjątek zgłoszony, jeśli podano niepoprawny numer rejestracyjny pojazdu
    '''
class parkomatPustyNumerRejestracyjnyExeption(parkomatExeption):
    '''
    Wyjątek zgłoszony, jeśli nie podano numeru rejestracyjnego pojazdu
    '''
class parkomatNieWrzuconoPieniadze(parkomatExeption):
    '''
    Wyjątek zgłoszony, jeśli nie wrzucono zadnej monety
    '''
