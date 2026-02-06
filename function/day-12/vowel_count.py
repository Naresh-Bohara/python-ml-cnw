# count the vowels in a string
def count_vowels(string):
    vowels = "aeiou"
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    return count

string = input("Enter a string to count the number of vowels: ").lower()
result = count_vowels(string)
print(f"The number of vowels in the string is: {result}")