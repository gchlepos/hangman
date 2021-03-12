from urllib import request
import json
import random

class Word:

    def __init__(self, full_word, encrypted_word, definition) -> None:
        self.decoded = full_word
        self.encoded = encrypted_word
        self.definition = definition


    def __str__(self) -> str:
        return f"Full Word: {self.decoded} \nEncrypted Word: {self.encoded}"

    def getWord():
        url = "https://random-words-api.vercel.app/word"
        wordDecoded = "g"

        while len(wordDecoded) < 6:
            # loading word
            r = request.urlopen(url)
            data = r.read()
            jsonData = json.loads(data)

            wordDecoded = jsonData[0]["word"]
            wordDecoded = wordDecoded.lower()

            # puttin '_'
            inds = [i for i, _ in enumerate(wordDecoded) if not wordDecoded.isspace()]
            sam = random.sample(inds, 3)
            lst = list(wordDecoded)
            for ind in sam:
                lst[ind] = "_"

            wordEncoded = "".join(lst)

        definition = jsonData[0]["definition"]
        word = Word( wordDecoded, wordEncoded, definition)
        return word

    def wordExplanation(theWord):
        print("Congratulations, you have won!")
        print(f"The word was: {theWord.decoded}")
        print(f"The definition of the word is: {theWord.definition}")
