# Correcting spellings in a piece of text is one of the handy features that can be used in any application where users write content.
# For example, if you want to create a notepad, it should have a feature to identify and correct the wrong spellings.

# The SpellChecker module in Python is one of the handiest tools that can be used to correct misspelt words in a piece of text.

from spellchecker import SpellChecker
checker = SpellChecker()

input_word = input("Enter a word: ")
if input_word in checker:
    print("Correct spelling")
else:
    print("Incorrect spelling")
    print("Did you mean: ", checker.correction(input_word))
    input("(y/n)? ")
    if input == "y":
        correction = checker.correction(input_word)
        print("Corrected spelling: ", correction)
    else:
        print("No correction made.")
        print("Spelling: ", input_word)
