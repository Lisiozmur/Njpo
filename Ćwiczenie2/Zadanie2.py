def algorytm_karuzelowy(kolejak):

    kolejak = [list(kolejka) for kolejka in kolejak]
    total = sum(len(kolejka) for kolejka in kolejak)
    wynik = []

    while total > 0:
        for i in range(len(kolejak)):
            if kolejak[i]:
                zad = kolejak[i].pop(0)
                wynik.append(zad)
                total -= 1
        kolejak = [kolejka for kolejka in kolejak if kolejka]
    return wynik

kolejak = ["CB", "DE", "AF"]
porzadek = algorytm_karuzelowy(kolejak)
print(porzadek)
