from tkinter import *

def createWindow():
    window = Tk()
    window.title("Hangman Game")
    window.configure(bg="black")
    window.geometry("850x600")

    return window

# def click( textentry):
#     inputLetter=textentry.get()
#     print("textentry")
#     if len(inputLetter) == 1: print("YES")

def playGame(window, wordWePursuit):

    Label(window, text=f"Here is your word: {wordWePursuit.encoded}", bg="black", fg="white", font=("courier", 20)) \
        .grid(row=2, column=0, sticky=W)

    L1 = Label(window, text="Type a letter: ", bg="black", fg="white", font=("courier", 20)) \
        .grid(row=3, column=0, sticky=W)

    return window
