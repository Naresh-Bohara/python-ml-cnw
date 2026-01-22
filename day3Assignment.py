# -------------------------Day-3 Assignment---------------------------

#q1. Wap to enter 2 number and display greater number
num1 = float(input("Please enter your first number: "))
num2 = float(input("Please enter your second number: "))
if num1>num2:
    print(f"The number you entered at first is greater which is, {num1}")
elif num1 < num2:
    print(f"The number you entered at second is greater which is, {num2}")
else:
    print(f"The numbers you entered are equal, first:{num1} = second:{num2}")

#q2. Wap to check if number lies between 1 to 100
number = int(input("Please enter the number: "))
if number > 0 and number <= 100:
    print(f"Yes, the number you entered, {number} lies between 1 to 100 ")
else:
    print(f"No, the number you entered, {number} doesn't lies between 1 to 100")

#q3. Wap to check if user's age is less than 18
user_age = int(input("Please enter your age: "))
if user_age < 18:
    print("You are below 18. Enjoy childhood! Responsibilities are loading...")

#q4. Wap to to check if username and password is correct
u, p = "naresh112", "@Naresh123#"
username = input("Please enter username: ")
password = input("Please enter password: ")
if username == u and password == p:
    print("Login successfull!")
else:
    print("Invalid username or password")

