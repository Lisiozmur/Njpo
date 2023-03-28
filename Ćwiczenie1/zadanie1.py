import time


def zadanie1():
    start = time.time()
    tab = []
    n = 1000000

    for i in range(n):
        tab.append("Object")

    print("%s s" % (time.time() - start))
zadanie1()