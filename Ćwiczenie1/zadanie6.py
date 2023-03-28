def zadanie6():
    s1, s2 = input()"jutro","rano"
    koszt = 0

    if len(s1)>= len(s2):
        dlugie = s1
        krutkie = s2
    else:
        dlugie = s2
        krutkie = s1

    for i in range(0, len(krutkie)):
        if dlugie[i] != krutkie[i]:
            koszt +=1

    koszt += len(dlugie) - len(krutkie)

    print("Koszt wynosi =", koszt)
zadanie6()