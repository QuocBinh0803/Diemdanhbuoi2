def count_letters(word):
    letter_count = {}
    word = word.lower()

    for char in word:
        if char.isalpha():
            if char in letter_count:
                letter_count[char] += 1

            else:
                letter_count[char] = 1

    return letter_count
word = "Hello World"
print(count_letters(word))  
