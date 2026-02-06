# check whether given number is an Armstrong number or not

def is_armstrong(number):
    temp = number
    num_digits = len(str(number))
    total  = 0
    while temp > 0:
        digit = temp % 10
        total += digit ** num_digits
        temp //= 10
    
    if total == number:
        return "Armstrong number"
    else:
        return "Not an Armstrong number"

num = int(input("Enter a number to check if it is an Armstrong number: "))
result = is_armstrong(num)
print(result)
  
'''
# example of armstrong number: 153
1^3 + 5^3 + 3^3 = 153

Iteration-1:
temp = 153
num_digits = 3
total = 0
digit = 153 % 10 = 3
total = 0 + 3^3 = 27
temp = 153 // 10 = 15

Iteration-2:
temp = 15
num_digits = 3
total = 27
digit = 15 % 10 = 5
total = 27 + 5^3 = 152
temp = 15 // 10 = 1

Iteration-3:
temp = 1
num_digits = 3
total = 152
digit = 1 % 10 = 1
total = 152 + 1^3 = 153
temp = 1 // 10 = 0


'''