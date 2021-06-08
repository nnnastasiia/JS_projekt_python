
from tkinter import Tk
from Parkomat_app.Parkomat import *
from parkomat_money.przechowywaczMonet import PrzechowywaczMonet



root=Tk()
przechowywaczMonet=PrzechowywaczMonet()
my_window=Parkomat(root, przechowywaczMonet)
my_window.startWindow()
