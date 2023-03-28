def zadanie5():
    n1, n2, n = 1,2,0

    for i in range(93):
        n = n1 + n2
        print(n)
        n1 = n2
        n2 = n
zadanie5()