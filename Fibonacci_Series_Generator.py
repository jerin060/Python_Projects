def fibonacci_gen(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

n = int(input("Enter number of terms: "))
for num in fibonacci_gen(n):
    print(num, end=" ")