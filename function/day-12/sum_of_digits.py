# sum of digits of a number
def sum_of_digits(number):
    total = 0
    while number > 0:
        digit = number % 10
        total += digit
        number //= 10
    return total

num = int(input("Enter a number to find the sum of its digits: "))
result = sum_of_digits(num)
print(f"The sum of the digits of {num} is: {result}")