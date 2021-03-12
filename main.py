from word import Word

wordWePursuit = Word.getWord()
print(wordWePursuit)

while True:
    inputLetter = input("\ntype a letter: ")

    if inputLetter in wordWePursuit.decoded:

        #an yparxei katw apo pabla alla kai sti leksi den ton afinei na to grapsei
        #
        # if inputLetter in wordWePursuit.encoded and : #if the letter is already found
        #     print("you stupid")
        #     continue

        #Find where the letter is and replace it!
        for idx, wordLetter in enumerate(wordWePursuit.decoded):
            if wordLetter == inputLetter:
                wordList = list(wordWePursuit.encoded)
                wordList[idx] = inputLetter
                wordWePursuit.encoded = "".join(wordList)
        print("The letter exists!")
        print(f"The word now: {wordWePursuit.encoded}")

    else:
        print("The letter does not exist!")

    #If you have found all the hidden letters
    if '_' not in wordWePursuit.encoded:
        print("You have won!!!")
        Word.wordExplanation(wordWePursuit)
        break