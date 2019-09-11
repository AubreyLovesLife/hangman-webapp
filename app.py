from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")



def randWord():    
    import requests
    import random
    dictionary = requests.get('http://norvig.com/ngrams/sowpods.txt').text 
    listOfWords = dictionary.split() # create a list of words from dictionary
    choice = random.choice(listOfWords) # chose a random word from the list of words
    return choice
word = randWord()
length = len(word)

# convert the word to a dictionary, where the keys are numbers 0 to length and the values are the 
# letters that correspond to that number
# eg. word = "cats"  ---> wordDict = {0:'c', 1:'a', 2:'t', 3:'s'}
## wordDict = {letter: word[letter] for letter in list(range(length))}

# create list of empty spaces the length of the word to be guessed, 
# this will be the argument that goes into the guessLetter() function
wordGuessBlank = []
for i in list(range(length)): 
    wordGuessBlank.append('_')
    i = i # not necessary, but prevents the unused variable error

# a function that makes the list of letters pretty by removing [] and commas
def prettifyList(wordGuessBlank):
    wordGuessOut = " ".join(wordGuessBlank) # this one has spaces, to make it look nice when printing out hangman word for the game
    return (wordGuessOut) 
blankSpaces = prettifyList(wordGuessBlank)


@app.route("/play", methods=["POST","GET"])
def play():
    username = request.form.get("name")
    if not request.form.get("name"):
        return "failure to enter username"
    else:
        pass

    return render_template("play.html",name=username,word=word,blankSpaces=blankSpaces)


@app.route("/continue", methods=["POST","GET"])
def continuePlay():
    letter = request.form.get("q")
    if not letter:
        return "You must guess a letter."
    else:
        pass
    return render_template("continue.html",letter=letter,blankSpaces=blankSpaces,word=word)



if __name__ == '__main__':
    app.run(debug=True)