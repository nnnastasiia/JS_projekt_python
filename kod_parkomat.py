import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Frame, Label, Button, Entry
import datetime
from datetime import timedelta
from tkinter import *
from tkinter.messagebox import showinfo
from decimal import Decimal


# Pieniądze
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
        return self._wartosc



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
                    raise parkomatFullException
        except parkomatFullException as pFE:
            showinfo("Parkomat pelny", "Przepraszamy, parkomat jest pelny")

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
        self.data_odj = 0

        self._master.title("Parkomat")

        Label(self._master, text=" ")

        frame_coins1 = Frame(self._master)
        frame_coins1.pack(fill=BOTH, expand=True)

        button1g = Button(frame_coins1, text="1g", width=12, bg='bisque2',
                          command=lambda self=self: [self.przechowywaczMonet.dodaj_monete(m001), self.countPieniadze()]).pack(side=LEFT, padx=5, pady=5)

        button2g = Button(frame_coins1, text="2g", width=12, bg='bisque2',
                          command=lambda self=self: [self.przechowywaczMonet.dodaj_monete(m002), self.countPieniadze()]).pack(side=LEFT, padx=5, pady=5)

        button5g = Button(frame_coins1, text="5g", width=12, bg='bisque2',
                          command=lambda self=self: [self.przechowywaczMonet.dodaj_monete(m005), self.countPieniadze()]).pack(side=LEFT, padx=5, pady=5)

        frame_coins2 = Frame(self._master)
        frame_coins2.pack(fill=BOTH, expand=True)

        button10g = Button(frame_coins2, text="10g", width=12, bg='MistyRose2',
                          command=lambda self=self: [self.przechowywaczMonet.dodaj_monete(m01), self.countPieniadze()]).pack(side=LEFT, padx=5, pady=5)

        button20g = Button(frame_coins2, text="20g", width=12, bg='MistyRose2',
                          command=lambda self=self: [self.przechowywaczMonet.dodaj_monete(m02), self.countPieniadze()]).pack(side=LEFT, padx=5, pady=5)

        button50g = Button(frame_coins2, text="50g", width=12, bg='MistyRose2',
                          command=lambda self=self: [self.przechowywaczMonet.dodaj_monete(m05), self.countPieniadze()]).pack(side=LEFT, padx=5, pady=5)

        frame_coins3 = Frame(self._master)
        frame_coins3.pack(fill=BOTH, expand=True)

        button1zl = Button(frame_coins3, text="1zł", width=12, bg='LightPink1',
                          command=lambda self=self: [self.przechowywaczMonet.dodaj_monete(m1), self.countPieniadze()]).pack(side=LEFT, padx=5, pady=5)

        button2zl = Button(frame_coins3, text="2zł", width=12, bg='LightPink1',
                          command=lambda self=self: [self.przechowywaczMonet.dodaj_monete(m2), self.countPieniadze()]).pack(side=LEFT, padx=5, pady=5)

        button5zl = Button(frame_coins3, text="5zł", width=12, bg='LightPink1',
                          command=lambda self=self: [self.przechowywaczMonet.dodaj_monete(m5), self.countPieniadze()]).pack(side=LEFT, padx=5, pady=5)

        frame_banktoty1 = Frame(self._master)
        frame_banktoty1.pack(fill=BOTH, expand=True)

        button10zl = Button(frame_banktoty1, text="10zł", width=12, bg='HotPink1',
                          command=lambda self=self: [self.przechowywaczMonet.dodaj_monete(m10), self.countPieniadze()]).pack(side=LEFT, padx=5, pady=5)

        button20zl = Button(frame_banktoty1, text="20zł", width=12, bg='HotPink1',
                          command=lambda self=self: [self.przechowywaczMonet.dodaj_monete(m20), self.countPieniadze()]).pack(side=LEFT, padx=5, pady=5)

        button50zl = Button(frame_banktoty1, text="50zł", width=12, bg='HotPink1',
                          command=lambda self=self: [self.przechowywaczMonet.dodaj_monete(m50), self.countPieniadze()]).pack(side=LEFT, padx=5, pady=5)

        self.nrPoj_lbl = Label(frame_coins1, text="Numer rejest.pojazdu:")
        self.nrPoj_lbl.pack(side=LEFT, padx=5, pady=5)
        self.getNrPoj = Entry(frame_coins1, width=20)
        self.getNrPoj.pack(side=LEFT, padx=10)
        self.dodajnr_button = Button(frame_coins1, text="Dodaj", width=10, command=self.dodajnr_click, bg='alice blue')
        self.dodajnr_button.pack(side=LEFT, padx=5, pady=5)

        self.data_park = Label(frame_coins2, text="Data parkowania:")
        self.data_park.pack(side=LEFT, padx=5, pady=5)
        self.getData = Entry(frame_coins2, width=20)
        self.getData.pack(side=LEFT, padx=10)
        self.getData.insert(END, datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"))

        self.akt_data_button = Button(frame_coins2, text="Akt. data", width=10, command=self.akt_data_click, bg='alice blue')
        self.akt_data_button.pack(side=LEFT, padx=5, pady=5)

        self.czas_label = Label(frame_coins3, text="Czas wyjazdu:")
        self.czas_label.pack(side=LEFT, padx=5, pady=5)

        self.zaplacono_lbl = Label(frame_banktoty1, text="Zaplacono:")
        self.zaplacono_lbl.pack(side=LEFT, padx=5, pady=5)

        Button(self._master, text="Anuluj", command=self.closeWindow, bg='IndianRed1').pack(side=RIGHT, padx=5, pady=5)
        Button(self._master, text="Zatwierdz", command=self.zatw_click, bg='lawn green').pack(side=RIGHT, padx=5, pady=5)

        self._master.mainloop()

    def closeWindow(self):
        self._master.destroy()

    def dodajnr_click(self):
        NrPoj = self.getNrPoj.get()

        if (len(NrPoj) == 0):
            raise parkomatPustyNumerRejestracyjnyExeption("Prosze podac numer rejestracyjny pojazdu")
        elif (len(NrPoj) > 9):
            raise parkomatNiepoprawnyNumerRejestracyjnyExeption("Prosze podac poprawny numer rejestracyjny pojazdu")

        self.nrPoj_lbl.config(text="Numer rejest.pojazdu:  " + str(NrPoj.upper()))
        self.getNrPoj.pack_forget()
        self.dodajnr_button.pack_forget()

    def akt_data_click(self):
        self.getData.delete(0, END)
        self.getData.insert(0, datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"))

    def countPieniadze(self):
        
        wplacono = self.przechowywaczMonet.suma()
        data1 = self.getData.get()

        self.data_park.config(text="Data parkowania:  " + data1)
        self.getData.pack_forget()
        self.akt_data_button.pack_forget()
        try:
            data1 = datetime.datetime.strptime(data1, "%d/%m/%Y %H:%M:%S")
        except parkomatNiepoprawnyFormatDaty:
            raise parkomatNiepoprawnyFormatDaty("Niepoprawny format daty, prosze podac date w formacie d/m/Y H:M:S")

        if wplacono == Decimal('1'):
            self.zaplacono_lbl.config(text='Zapłacono: ' + str(wplacono) + ' zł')
            timedelta1 = timedelta(minutes = 30)
            self.data_odj = (data1 + timedelta1).strftime("%d/%m/%Y %H:%M:%S")
            self.czas_label.config(text='Czas wyjazdu: ' + str(self.data_odj))

            return
        timedelta1=timedelta(seconds = 3600)

        if wplacono == Decimal('2'):
            self.zaplacono_lbl.config(text='Zapłacono: ' + str(wplacono) + ' zł')
            timedelta1 = timedelta(hours = 1)
            self.data_odj = (data1 + timedelta1).strftime("%d/%m/%Y %H:%M:%S")
            self.czas_label.config(text='Czas wyjazdu: ' + str(self.data_odj))

            return
        
        timedelta1=timedelta(seconds = 3600)

        if wplacono == Decimal('4'):
            self.zaplacono_lbl.config(text = 'Zapłacono: ' + str(wplacono) + ' zł')
            timedelta1 += timedelta(hours = 2)
            self.data_odj = (data1 + timedelta1).strftime("%d/%m/%Y %H:%M:%S")
            self.czas_label.config(text='Czas wyjazdu: ' + str(self.data_odj))

            return
        
        timedelta1 += timedelta(seconds = 3600)

        self.zaplacono_lbl.config(text = 'Zapłacono: ' + str(wplacono) + ' zł')
        timedelta1 += timedelta(seconds = float(wplacono/Decimal('5')*3600))
        self.data_odj = (data1 + timedelta1).strftime("%d/%m/%Y %H:%M:%S")
        self.czas_label.config(text='Czas wyjazdu: ' + str(self.data_odj))


    def zatw_click(self):
        try:
            NrPoj=self.getNrPoj.get()
            wplacono=self.przechowywaczMonet.suma()

            if NrPoj == '':
                raise parkomatPustyNumerRejestracyjnyExeption("Prosze podac numer rejestracyjny pojazdu")
            if len(NrPoj) > 9:
                raise parkomatNiepoprawnyNumerRejestracyjnyExeption("Prosze sprawdzic numer rejestracyjny pojazdu oraz podac poprawny")
            if wplacono == 0:
                raise parkomatNieWrzuconoPieniadze("Prosze wplacic pieniadze")

        except parkomatPustyNumerRejestracyjnyExeption as pPNPE:
            messagebox.showinfo("Nie podano numer rejestracyjny pojazdu!", "Prosze podac numer rejestracyjny pojazdu")
        except parkomatNieWrzuconoPieniadze as pNWPE:
            messagebox.showinfo("Nie wrzucono pieniadze!", "Prosze wplacic pieniadze")
        except parkomatNiepoprawnyNumerRejestracyjnyExeption as pNNRPE:
            messagebox.showinfo("Podano nie numer rejestracyjny pojazdu!", "Prosze sprawdzic numer rejestracyjny pojazdu oraz podac poprawny")
        if (wplacono != 0) and (NrPoj != ''):
            self.closeWindow()
            messagebox.showinfo("Paragon", "Numer rejestracyjny pojazdu:" + str(NrPoj.upper()) + "\n\nWplacono:  " + str(wplacono)+" zł\n\n" "Czas zakupu:  " + str(datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")) + "\n\nCzas wyjazdu: " + str(self.data_odj))






class parkomatException(Exception):
    '''
    Klasa ogólna dla wszystkich wyjątków
    '''
    def __init__(self, message):
        self.message=message

class ZlyNominalException(Exception):
    '''
    Wyjątek zgłoszony, jeśli wplacona nieznana wartosc
    '''
    def __init__(self, message):
        self.message=message

class parkomatFullException(parkomatException):
    '''
    Wyjątek zgłoszony, jeśli parkomat jest pelny
    '''
    def __init__(self, message):
        self.message=message
class parkomatNiepoprawnyNumerRejestracyjnyExeption(parkomatException):
    '''
    Wyjątek zgłoszony, jeśli podano niepoprawny numer rejestracyjny pojazdu
    '''
    def __init__(self, message):
        self.message=message
class parkomatPustyNumerRejestracyjnyExeption(parkomatException):
    '''
    Wyjątek zgłoszony, jeśli nie podano numeru rejestracyjnego pojazdu
    '''
    def __init__(self, message):
        self.message=message
class parkomatNieWrzuconoPieniadze(parkomatException):
    '''
    Wyjątek zgłoszony, jeśli nie wrzucono zadnej monety
    '''
    def __init__(self, message):
        self.message=message

class parkomatNiepoprawnyFormatDaty(parkomatException):
    '''
    Wyjątek zgłoszony, jeśli podany niepoprawny format daty
    '''
    def __init__(self, message):
        self.message=message






from tkinter import Tk

root=tk.Tk()
przechowywaczMonet=PrzechowywaczMonet()
my_window=Parkomat(root, przechowywaczMonet)


