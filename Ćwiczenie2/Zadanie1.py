import random
import math

def szacowanie(proby):
    wew = 0
    total = proby

    for i in range(proby):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        if x ** 2 + y ** 2 <= 1:
            wew += 1
    pioszacowane = 4 * wew / total
    return pioszacowane

licz_prob = [10, 100, 1000, 10000, 100000]

for proby in licz_prob:
    okolo = szacowanie(proby)
    trafnosc = abs(okolo - math.pi) / math.pi * 100
    print("Liczba prób: ", proby, "Oszacowane pi", okolo, "Trafność", trafnosc)