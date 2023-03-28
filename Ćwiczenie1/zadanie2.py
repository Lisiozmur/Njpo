from datetime import datetime, timedelta


def kalkulatorutf():

    print("Wprowadź strefę czasową --->")
    strefa = int(input())

    if strefa in range(-11, 14):
        czas = datetime.now() + timedelta(hours=strefa-1)
        obecny = czas.strftime("%H:%M:%S")
        print("Czas w strefie UTC:", strefa, obecny)
    else:
        print("Błędna strefa czasowa")

kalkulatorutf()