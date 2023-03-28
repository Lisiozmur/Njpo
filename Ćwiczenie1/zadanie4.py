def sieve(n):
    A = [True for i in range(n+1)]
    A[0] = False
    i = 2
    while i*i <= n:
        if A[i]: 
            j = i*i
            while j <= n:
                A[j] = False
                j = j+i
        i = i+1
    return A
x = 0
for i in sieve(100000):
    if i: print(x)
    x = x+1