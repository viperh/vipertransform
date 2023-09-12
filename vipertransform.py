import os
import time
import re


small_caps = {
    
    "a": "ᴀ",
    "b": "ʙ",
    "c": "ᴄ",
    "d": "ᴅ",
    "e": "ᴇ",
    "f": "ғ",
    "g": "ɢ",
    "h": "ʜ",
    "i": "ɪ",
    "j": "ᴊ",
    "k": "ᴋ",
    "l": "ʟ",
    "m": "ᴍ",
    "n": "ɴ",
    "o": "ᴏ",
    "p": "ᴘ",
    "q": "ǫ",
    "r": "ʀ",
    "s": "s",
    "t": "ᴛ",
    "u": "ᴜ",
    "v": "ᴠ",
    "w": "ᴡ",
    "x": "x",
    "y": "ʏ",
    "z": "ᴢ"
}


def get_first_index(sentence):
    
    if not sentence:
        print("not sentence!")
        return -1

    
    i = 0
    for a in sentence:
        if a != " ":
            return i
        
        i += 1
    return -1

    

def translate(word):
    ignore_indexes = []

    
    if "%" in word:
        for i in range(len(word)):

            ignoreOn = False

            if word[i] == "%" and not ignoreOn:
                ignoreOn == True
                ignore_indexes.append(i)
            elif word[i] == "%" and ignoreOn:
                
                ignoreOn = False
                ignore_indexes.append(i)
            else:
                if(ignoreOn):
                    ignore_indexes.append(i)




content = []

while True:
    user_input = input()
    
    if user_input == "STOP":
        break

    content.append(user_input)


for sentence in content:
    finalSentence = ""

    

    firstIndex = get_first_index(sentence)


    if sentence[firstIndex] == "#":
        finalSentence = sentence
     
    elif ":" in sentence:
        key, value = sentence.split(":")
        finalSentence += (key + ":")
        
        valueWords = value.split(" ")
        
        for i in range(len(valueWords)):
            newWord = translate(valueWords[i])
            if i == len(valueWords):
                finalSentence += newWord
            else:
                finalSentence += newWord + " "
    
    content.append(finalSentence)


for s in content:
    print(s)
    