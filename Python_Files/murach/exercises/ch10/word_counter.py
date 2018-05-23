#!/usr/bin/env python3
from os import path
def get_words_from_file(filename):
    with open(filename) as file:
        text = file.read()    # read str from file

    # print(text)
    text = text.replace("\n", "")
    text = text.replace(",", "")
    sentences = text.split(".")
    text = text.replace(".", "")
    text = text.lower()
    
    words = text.split(" ")   # convert str to list
    words.sort()
    # print(words)
    return words, sentences

def get_unique_words(words):
    unique_words = []
    unique_words.append(words[0])
    
    for i in range(1, len(words)):
        if words[i] == words[i - 1]:
            continue
        else:
            unique_words.append(words[i])            
    return unique_words


def getDir(file):
    myFile = []
    myFile = path.split(__file__)
    return myFile[0] + "\\" + file

def main():
    filename = getDir("gettysburg_address.txt")
    print("The Word Counter program\n")  

    # get words and unique words
    words, sentences = get_words_from_file(filename) # get list of words
    unique_words = get_unique_words(words)

    # display number of words and unique words   
    print("Number of sentences = ",len(sentences))
    print("Number of words =", len(words))
    print("Number of unique words = ", len(unique_words))

    # display unique words and their word counts
    print("Unique word occurrences:")
    for word in unique_words:
        print("    ", word, "=", words.count(word))
 
if __name__ == "__main__":
    main()
