
#Klasy wszystkich możliwych wyjątków

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

