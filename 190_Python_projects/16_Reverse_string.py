def reverse(string):
    return string[::-1]  # [start:stop:step]


word = input("Enter a word: ")
print(f'Reverse of {word}: {reverse(word)}')
