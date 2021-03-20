from word import Word
from tkinter import *
import gui

def click():
    inputLetter=textentry.get()
    if len(inputLetter) == 1:
        print(inputLetter)
        if inputLetter in wordWePursuit.decoded:
            Word.fillInTheBlanks( wordWePursuit, inputLetter)
            print(wordWePursuit)

            #TO BE: a function
            window.destroy()
            print("destroyed")
            window1 = gui.createWindow()
            #Label(window, text="The letter exists!", bg="black", fg="white", font=("courier", 20)) \
            #    .grid(row=0, column=0, sticky=W)
            gui.playGame(window1, wordWePursuit)

            return True
        else:
            print("The letter does not exist!")

            return False

wordWePursuit = Word.getWord()
print(wordWePursuit)

window = gui.createWindow()

Label(window, text="Welcome to hangman!", bg="black", fg="white", font=("courier", 23)) \
    .grid(row=1, column=0, sticky=W)

while True:

    window = gui.playGame(window, wordWePursuit)

    textentry = Entry(window, width=5, bg="black", fg="white", font=("courier", 20))
    textentry.grid(row=4, column=0, sticky=W)

    B = Button(window, text="SUBMIT", width=6, command=click) \
        .grid(row=5, column=0, sticky=W)
    print("destroyed?")
    if B == True:
        window.destroy()
        print("destroyed")
        Label(window, text="The letter exists!", bg="black", fg="white", font=("courier", 20)) \
            .grid(row=2, column=0, sticky=W)
        gui.playGame( window, wordWePursuit)

    window.mainloop()
    # if inputLetter in wordWePursuit.decoded:
    #
    #     #an yparxei katw apo pabla alla kai sti leksi den ton afinei na to grapsei
    #     #
    #     # if inputLetter in wordWePursuit.encoded and : #if the letter is already found
    #     #     print("you stupid")
    #     #     continue
    #
    #     #Find where the letter is and replace it!
    #     for idx, wordLetter in enumerate(wordWePursuit.decoded):
    #         if wordLetter == inputLetter:
    #             wordList = list(wordWePursuit.encoded)
    #             wordList[idx] = inputLetter
    #             wordWePursuit.encoded = "".join(wordList)
    #     print("The letter exists!")
    #     print(f"The word now: {wordWePursuit.encoded}")
    #
    # else:
    #     print("The letter does not exist!")
    #
    # #If you have found all the hidden letters
    # if '_' not in wordWePursuit.encoded:
    #     print("You have won!!!")
    #     Word.wordExplanation(wordWePursuit)
    #     break
