# Zadanie 1 - Szybkość dodawania elementów do tablicy
"""
import time

start_time = time.time()
i: int = 0
wej = int(input("Ilosc danych do tabeli --> "))
t=["Element"]

while i<wej:
    t.append("Element")
    print(t)
    i += 1

print("%s s" % (time.time() - start_time))
"""

# Zadanie 2 - Kalkulator UTC
"""
from datetime import datetime, timedelta
x: int = 6 #podajemy strefę czasową 

if x<-12 or x>12:
    print("Blędna strefa czasowa")

else:
    czas = datetime.now() + timedelta(hours=x-1)
    obecny = czas.strftime("%H:%M:%S")
    print("Czas w strefie UTC",x,obecny )
"""
# Zadanie 3 - Losowanie liczb
"""
import random

ran: int
i: int = 0
srednia: int = random.randint(0,10)

while i<1000000:
    ran = random.randint(0,10)
    srednia += ran
    srednia = srednia/2
    i += 1

print("Przewidywana liczba: ",srednia)
print("Wylosowana liczba: ", random.randint(0,10))
""" 
# Zadanie 4 - Liczby pierwsze

# Zadanie 5 - Ciąg Fibonacciego

"""
a: int = 1;
b: int = 2;
i: int = 0;
c: int;

while i < 93:
    c = a+b;
    print(c);
    a = b;
    b = c;
    i += 1;
"""