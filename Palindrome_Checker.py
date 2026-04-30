def is_palindrome(text):
    text = text.lower()  # ignore case
    return text == text[::-1]

# Input
word = input("Enter a word: ")

if is_palindrome(word):
    print("Palindrome")
else:
    print("Not a Palindrome")