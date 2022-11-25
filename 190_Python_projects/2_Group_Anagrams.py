# Anagrams are words formed by rearranging the letters of another word.
# For example, car and arc, cat and act, etc.
# Grouping anagrams is one of the popular questions in coding interviews.

from collections import defaultdict


def group_anagrams(words):
    dfdict = defaultdict(list)
    for word in words:
        sorted_words = " ".join(sorted(word))
        # print("Sorted words: ")
        # print(sorted_words)
        dfdict[sorted_words].append(word)
        # print(dfdict[sorted_words])
        # print("")
    return list(dfdict.values())


words = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagrams(words))
