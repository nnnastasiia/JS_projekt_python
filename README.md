# JS_projekt_python


{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# `Parkomat`\n",
    "\n",
    "### ***OPIS ZADANIA***\n",
    "\n",
    "* Parkomat przechowuje informacje o monetach/banknotach znajdujących się w nim (1, 2, 5, 10, 20, 50gr, 1, 2, 5, 10, 20, 50zł)\n",
    "* Okno z polem tekstowym na numer rejestracyjny pojazdu, aktualną datą (rok, miesiąc, dzień, godzina, minuta), datą wyjazdu z parkingu (rok, miesiąc, dzień, godzina, minuta), przyciskami pozwalającymi na wrzucanie monet (proszę umieścić pole pozwalające wpisać liczbę wrzucanych monet), oraz przyciskiem \"Zatwierdź\".\n",
    "\n",
    "* Program powinien zawierać pole pozwalające na przestawienie aktualnego czasu\n",
    "\n",
    "* **Zasady strefy parkowania**:\n",
    "\n",
    "    * Strefa płatnego parkowania obowiązuje w godzinach od 8 do 20 od poniedziałku do piątku.\n",
    "\n",
    "    * Pierwsza godzina płatna 2zł.\n",
    "\n",
    "    * Druga godzina płatna 4zł.\n",
    "\n",
    "    * Trzecia i kolejne godziny płatne po 5zł.\n",
    "\n",
    "    * Czas wychodzący poza obowiązywanie płatnego parkowania przechodzi na kolejny dzień\n",
    "        * Wykupienie godziny parkowania o 19:20 w piątek pozwala na parkowanie do 8:20 w poniedziałek (koniec o 20:20, wychodzi 20 minut poza płatne parkowanie, przechodzi na kolejny płatny dzień).\n",
    "\n",
    "* Po każdym wrzuceniu monety termin wyjazdu aktualizuje się zgodnie z całą wrzuconą kwotą\n",
    "\n",
    "* Jeśli wrzucone zostało mniej pieniędzy niż potrzeba na opłacenie pełnej godziny,to opłacana jest niepełna godzina:\n",
    "\n",
    "    * Wrzucenie 1zł pozwała na parkowanie 30 minut,\n",
    "\n",
    "    * Wrzucenie Szł pozwala na parkowanie 1 godzinę i 45 minut (2zł na opłacenie pierwszej godziny, zostało 3zł, a potrzeba 4zł na opłacenie kolejnej, co daje 3/4 godziny: 45 minut).\n",
    "\n",
    "* Po wciśnięciu przycisku \"Zatwierdź\" wyświetlane jest okno z potwierdzeniem opłacenia parkingu: numer rejestracyjny pojazdu, czas zakupu i termin wyjazdu.\n",
    "\n",
    "* Numer rejestracyjny może składać się tylko z wielkich liter od A do Z i cyfr.\n",
    "* W automacie mieści się dowolna liczba banknotów (10, 20, 50zł) i po 200 monet każdego rodzaju. Próba wrzucenia monety ponad limit powoduje wyświetlenie informacji o przepełnieniu parkomatu i prośbę o wrzucenie innego nominału.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "\n",
    "### ***TESTY*** \n",
    "\n",
    "\n",
    "1. Ustaw niepoprawną godzinę. Oczekiwany komunikat o błędzie. Ustawić godzinę na 12:34.\n",
    "2. Wrzucić 2 zł, oczekiwany termin wyjazdu godzinę po aktualnym czasie. Dorzuć 4zł, oczekiwany termin wyjazdu dwie godziny po aktualnym czasie. Dorzuć Szł, oczekiwany termin wyjazdu trzy godziny po aktualnym czasie. Dorzuć kolejne Szł, oczekiwany termin wyjazdu cztery godziny po aktualnym czasie.\n",
    "3. Wrzucić tyle pieniędzy, aby termin wyjazdu przeszedł na kolejny dzień, zgodnie z zasadami -- wrzucić tyle monet aby termin wyjazdu był po godzinie 19:00, dorzucić monetę 5zł,\n",
    "4. Wrzucić tyle pieniędzy, aby termin wyjazdu przeszedł na kolejny tydzień, zgodnie z zasadami - wrzucić tyle monet aby termin wyjazdu był w piątek po godzinie 19:00, a potem dorzucić monetę 5 zł,\n",
    "5. Wrzucić 1 zł, oczekiwany termin wyjazdu pół godziny po aktualnym czasie,\n",
    "6. Wrzucić 200 monet 1 gr, oczekiwany termin wyjazdu godzinę po aktualnym czasie.\n",
    "7. Wrzucić 201 monet 1 gr, oczekiwana informacja o przepełnieniu parkomatu\n",
    "8. Wciśnięcie \"Zatwierdź\" bez wrzucenia monet -- oczekiwana informacja o błędzie.\n",
    "9. Weiśnięcie \"Zatwierdź\" bez wpisania numeru rejestracyjnego — oczekiwana informacja o błędzie. Wciśnięcie \"Zatwierdź\" po wpisaniu niepoprawnego numeru rejestracyjnego — oczekiwana informacja o błędzie.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## [LINK DO MOJEGO REPOZYTORIUM](https://github.com/nnnastasiia/JS_projekt_python) "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
