# -----------------------Day-5 Assignment -----------------------------

# q1. wap to check if a number is palindrome or not 
num = int(input("Please enter a multi-digit number to check palindrome: "))
n = num
rev = 0
while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10
if rev == n:
    print(f"{n} is a palindrome.")
else:
    print(f"{n} is not a palindrome.")


# q2. wap to ignore multiples of 3 from 1 to 22 using continue statement
for i in range(1, 23):
    if i% 3 == 0:
        continue
    print(i, end=" ")
print()


#q3. program to print 1st five odd numbers between 1-20
count = 0
for i in range(1, 21):
    if i %2 != 0:
        print(i, end=" ")
        count +=1
        if count ==5:
            break
print()


#q4. program to find sum of even numbers from 1 to n
num = int(input("Enter the number upto which you want the sum of even numbers: "))
sum = 0
for i in range(1, num+1):
    if i % 2 == 0:
        sum += i
print(sum)


#q5. program to find 1st number divisible by 7 between 1-100
for i in range(1, 101):
    if i%7 == 0:
        break
print(i)
