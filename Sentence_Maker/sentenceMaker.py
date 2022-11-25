def sentence_maker(words):
    words = words.title()
    return words


# main function
if __name__ == '__main__':
    new_sentence = ''
    words = input("Say something: ")
    while words != '\end':
        new_sentence += sentence_maker(words)
        words = input("Say something: ")

    print(new_sentence)
