import random

def zadanie3():
    srednia = random.randint(0,10)
    proby = 1000000

    for i in range(proby):
        srednia += random.randint(0,10)
        srednia = srednia/2

    print("Przewidywana Liczna = ",srednia)
    print ("Wylosowana Liczba = ", random.randint(0,10))
zadanie3()

WERSJA 2

import random
suma = 0
for i in range(1000000):
    liczba = random.randint(1, 10)
    suma = (suma+liczba)/2
print("Liczba przewidziana: ", "%.0f" % suma
