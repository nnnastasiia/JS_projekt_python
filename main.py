
from tkinter import Tk
from parkomat_money import *
from Parkomat_app.Parkomat import *
import tkinter as tk
from tkinter import *
from parkomat_money.przechowywaczMonet import PrzechowywaczMonet


root=tk.Tk()
przechowywaczMonet=PrzechowywaczMonet()
my_window=Parkomat(root, przechowywaczMonet)


