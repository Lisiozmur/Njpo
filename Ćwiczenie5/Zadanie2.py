import time

def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

def fibonacci_recursive_memo(n, memo={}):
    if n <= 1:
        return n

    if n in memo:
        return memo[n]
    else:
        memo[n] = fibonacci_recursive_memo(n - 1, memo) + fibonacci_recursive_memo(n - 2, memo)
        return memo[n]

def measure_execution_time(func, *args):
    start_time = time.time()
    result = func(*args)
    end_time = time.time()
    execution_time = end_time - start_time
    return result, execution_time

n = 30
result, execution_time = measure_execution_time(fibonacci_recursive, n)
print(f"Bez pamięci podręcznej: Wynik: {result}, Czas wykonania: {execution_time} s")

result, execution_time = measure_execution_time(fibonacci_recursive_memo, n)
print(f"Z pamięcią podręczną: Wynik: {result}, Czas wykonania: {execution_time} s")
