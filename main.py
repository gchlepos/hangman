#from word1 import word

#playersName = input("Welcome to hangman! \nType your name: ")

class Word:

    def __init__(self, full_word, encrypted_word) -> None:
        self.decoded = full_word
        self.encoded = encrypted_word

    def __str__(self) -> str:
        return f"Encrypted Word: {self.encoded}"


wordWePursuit = Word("tabla", "t_b__")
print(wordWePursuit)

while True:
    inputLetter = input("\ntype a letter: ")

    if inputLetter in wordWePursuit.decoded:
        for idx, wordLetter in enumerate(wordWePursuit.decoded):
            if wordLetter == inputLetter:
                wordList = list(wordWePursuit.encoded)
                wordList[idx] = inputLetter
                wordWePursuit.encoded = "".join(wordList)
                print("The letter exists!")
                print(f"The word now: {wordWePursuit.encoded}")
    else:
        print("The letter does not exist!")
        print(wordWePursuit)