def find_single_digit(n):
    while n >= 10:
        sum_digits = 0
        while n > 0:
            sum_digits += n % 10
            n //= 10
        n = sum_digits
    return n
num = int(input("Enter a number: "))
result = find_single_digit(num)
print("The single-digit sum is:", result)
