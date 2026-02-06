# check whether a string is a palindrome or not

# def is_palindrome():
#     str = input("Enter a word to check palindrome: ").lower().replace(" ", "")
#     if str == str[::-1]:
#         print("The word is a palindrome.")
#     else:
#         print("The word is not a palindrome.")

# is_palindrome()


# with parameter:
def is_palindrome(word):
    word = word.lower()
    if word == word[::-1]:
        return "Palindrome"
    else:
        return "Not a Palindrome"
    
word = input("Enter a word to check palindrome: ")
result = is_palindrome(word)
print(result)


    

