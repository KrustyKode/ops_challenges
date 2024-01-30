from re import T
import ssl
import nltk
from nltk.corpus import words

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context


import nltk

def getWords():
    nltk.download('words')
    wordList = words.words()
    return wordList

def check4Word(words):
    answer = input("Enter a word: ")
    if answer in words:
        print("The word is in the dictionary")
    else:
        print("The word is not in the dicrionary")

def loadExtFile():
    passwordList = []
    with open('sample.txt', 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            line = line.rstrip()
            passwordList.append(line)
            print(passwordList)


if __name__ == "__main__":
    extWords = getWords()
    print(extWords)
    # print(wordList)

