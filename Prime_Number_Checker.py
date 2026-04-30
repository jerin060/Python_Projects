import math

def is_prime(n):
    if n <= 1:
        return False
    # Check for divisibility from 2 up to the square root of n
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


number = int(input("Enter a number: "))
print(f"{number} is prime: {is_prime(number)}")
