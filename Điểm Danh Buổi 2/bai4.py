import re

def count_words_in_file(file_path):
    word_count = {}
    with open(file_path, 'r') as file:
        for line in file:
            words = re.findall(r'\b\w+\b', line.lower())
            for word in words:
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1
    return word_count
file_path = "P1_data.txt"
word_counts = count_words_in_file(file_path)
print(word_counts)



