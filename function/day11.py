## String Methods:
text = "    Hello World!  "

'''
upper(): convert to uppercase
upper(): convert to lowercase
upper(): convert to capitalize first letter of each word
strip(): remove leading and trailing spaces
replace(old, new): replace old substring with new substring
find(substring): find the index of substring
replace(): replace old substring with new substring
split(): split string into list of substrings
find(): find the index of substring
join(): join list of strings into a single string
count(): count occurrences of a substring
startswith(): check if string starts with a substring
endswith(): check if string ends with a substring

'''

# print(text.upper())
# print(text.lower())
# print(text.title())
# print(text.strip())

str1 = "apple, banana, orange"

str2 = "python programming"
# print(str2.replace("python", "java"))
# print(str2.find("programming"))
print(str1.split(" s"))

lst = ["Hello", "world", "from", "Python"]
print(" ".join(lst))

# print(str1.count("a"))

# print(str1.startswith("apple"))
# print(str1.endswith("es"))