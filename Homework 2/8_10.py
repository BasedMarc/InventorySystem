def is_palindrome(word):
    word = word.lower().replace(" ", "")
    return word == word[::-1]

user_input = input("Enter a word or phrase: ")
if is_palindrome(user_input):
    print(user_input + " is a palindrome")
else:
    print(user_input + " is not a palindrome")
