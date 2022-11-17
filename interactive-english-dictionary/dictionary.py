import json  # package to apply with json files
from difflib import get_close_matches  # shows matching word

# load json file containing dictionary data
data = json.load(open("data.json"))

# function to return the list of meaning of words if found else return not found


def meaning(word):
    word = word.lower()  # lower the word for selecting from dictionary data

    # return the meaning of word if found in data.json
    if word in data:
        return data[word]

    # return the meaning of word if found in data.json with first letter capital
    elif word.title() in data:
        return data[word.title()]

    # in case user enters words like USA or NATO
    elif word.upper() in data:
        return data[word.upper()]

    # else return not found
    else:
        return "No meaning found! Enter another word.\n"


# main function
if __name__ == '__main__':
    q = 'y'  # set the char to 'y' for looup
    # loop until input is not 'y'
    while q == 'y':
        # input word for getting meaning
        word = input("\nEnter a word: ")

        outputs = meaning(word)
        # print(type(outputs))

        # if the return type from function is list, print the output values accordingly
        if type(outputs) == list:
            for output in outputs:
                print(f"=> {output}")
        # else print the not found returned
        else:
            print(meaning(word))

        q = input(f"\nDo you want to enter again?(y/n): ")
