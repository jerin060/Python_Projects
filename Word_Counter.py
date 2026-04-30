def word_counter(text):
    words = text.split()
    word_count = len(words)
    char_count = len(text)
    
    return word_count, char_count


sentence = input("Enter a sentence: ")

words, chars = word_counter(sentence)

print("Words:", words)
print("Characters:", chars)