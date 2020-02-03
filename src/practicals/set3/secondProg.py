def match_word(words):
    wordsWithCharacter = []
    for word in words:
        if len(word) <= 5 and (word[0] == 'm' or word[0] == 'M'):
            wordsWithCharacter.append(word)

    return wordsWithCharacter


wordsList = []
listSize = int(input("Enter size of list : "))

while listSize > 0:
    wordsToAdd = str(input("Enter a string to add in list : "))
    wordsList.append(wordsToAdd)
    listSize -= 1

print(match_word(wordsList))
