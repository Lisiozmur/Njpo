def find_zeros(polynomial, start, end):
    n = 0
    while True:
        x = start
        while x <= end:
            value = eval(polynomial)
            if abs(value) < 1e-6:
                yield x
            x += 0.1
        n += 1

polynomial = "x**2 - 4"
start = -10
end = 10

zeros_generator = find_zeros(polynomial, start, end)

for _ in range(5):
    zero = next(zeros_generator)
    print("Zero:", zero)

polynomial = "x**3 - 6*x**2 + 9*x"

zeros_generator = find_zeros(polynomial, start, end)

for _ in range(3):
    zero = next(zeros_generator)
    print("Zero:", zero)
