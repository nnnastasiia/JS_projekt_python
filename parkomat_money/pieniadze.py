from errors import *
from decimal import Decimal

# Pieniądze
class Pieniadze:
    '''
    Klasa reprezentująca dostępne wartości monet i banknotów oraz wyjątki przy pomyłkach
    '''
    def __init__(self, wartosc):
        try:
            if wartosc in {0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1, 2, 5, 10, 20, 50}:
                self._wartosc = Decimal(str(wartosc))
            else:
                raise ZlyNominalException("Nieznany nominal")
        except ZlyNominalException as zne:
            print(zne.message)
    #@property
    def pobierz_wartosc(self):
        return self._wartosc


#Dodanie dozwolonych wartości
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

