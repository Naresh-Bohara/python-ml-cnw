### -------------------------- Day-07 Assignment -----------------------------
## Solve the following using list comprehensions:

#q1. create a list of even numbers from 1-20
even_numbers =[i for i in range(1, 21) if i%2 == 0]
print("List of even numberes form 1 to 20: ", even_numbers)

#q2. create a list of odd numbers from 1-20
odd_numbers = [i for i in range(1, 21) if i%2 != 0]
print("List of odd numberes form 1 to 20: ", odd_numbers)

#q3. create a list of square of numbers from 1-20
square_numbers = [i**2 for i in range(1, 21)]
print("square numbers from 1 to 20: ", square_numbers)

#q4. create a list of lenght of each words in ["apple","orange","kiwi"]
words = ["apple", "orange", "kiwi"]
words_length = [len(word) for word in words]
print("length of words: ", words_length)

#q5. create a list of squares of only even numbers from 1-20
even_numbers_square = [i**2 for i in range(1, 21) if i%2 == 0]
print("Even numbers square from 1 to 20: ", even_numbers_square)

#q6. create a list of numbers divisible by 3 from 1-100
divisible_by_3 = [i for i in  range(1, 101) if i%3 == 0]
print("Numbers divisible by 3 from (1, 100): ", divisible_by_3)