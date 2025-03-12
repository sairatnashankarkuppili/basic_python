import math

first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
print("Prime numbers:", [num for num in range(first_number, second_number + 1) if is_prime(num)])
