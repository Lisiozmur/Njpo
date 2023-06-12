import json

def zapisz(kolekcja, nazwa_pliku):
    with open(nazwa_pliku, 'w') as plik:
        json.dump(kolekcja, plik)

kolekcja = [
    {'Tytuł': 'Rok 1984 1', 'Gatunek': 'Fantasy', 'Autor': 'Gorge Orwell', 'isbn': '7463528561'},
    {'Tytuł': 'Birmańskie dni', 'Gatunek': 'Literatura Pięka', 'Autor': 'Gorge Orwell', 'isbn': '0926354719'},
    {'Tytuł': 'Becoming. Moja historia', 'Gatunek': 'Autobiografia', 'Autor': 'Michelle Obama', 'isbn': '8364514253'}
]
zapisz(kolekcja, 'kolekcja.json')

def wczytaj(nazwa_pliku):
    with open(nazwa_pliku, 'r') as plik:
        kolekcja = json.load(plik)
    return kolekcja

wczytaj = wczytaj('kolekcja.json')
print(wczytaj)

def statystyki(kolekcja):
    gatunek_st = {}
    autor_st = {}

    for ksiazka in kolekcja:
        gatunek = ksiazka['Gatunek']
        autor = ksiazka['Autor']

        gatunek_st[gatunek] = gatunek_st.get(gatunek, 0) + 1
        autor_st[autor] = autor_st.get(autor, 0) + 1

    return gatunek_st, autor_st

st_gatunek, st_autor = statystyki(kolekcja)
print("Statystyki Gatunku:")
print(st_gatunek)
print("Statystyki Autora:")
print(st_autor)
