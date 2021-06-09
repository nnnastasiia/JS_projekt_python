
from tkinter import Tk
from Parkomat_app.Parkomat import *
from parkomat_money.przechowywaczMonet import PrzechowywaczMonet


def main():
    '''
    Funkcja główna która wykonuje i uruchamia cały program
    '''
    root=Tk()
    przechowywaczMonet=PrzechowywaczMonet()
    my_window=Parkomat(root, przechowywaczMonet)
    my_window.startWindow()

if __name__ == '__main__':
    main() 
    