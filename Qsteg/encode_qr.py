#! /usr/bin/python
# Joey Hommel and Tyler Harding
# CSEC-464 Final Project
# Prof Pan

from PIL import Image
from random import randint

width = 25
height = 25
#Make an empty array filled with 2's to later be substituted out for 1s and 0s.
img = [2] * (height * width)
#These are hard coded arrays to make sure the picture resembles are QR code with the boxes in the top left, top right, bottom left, and close to bottom right are correct.
mustBeBlack = [0,1,2,3,4,5,6,18,19,20,21,22,23,24,25,31,43,49,50,52,53,54,56,68,70,71,72,74,75,77,78,79,81,93,95,96,97,99,100,102,103,104,106,118,120,121,122,124,125,131,143,149,150,151,152,153,154,155,156,168,169,170,171,172,173,174,416,417,418,419,420,441,445,450,451,452,453,454,455,456,466,468,470,475,481,491,495,500,502,503,504,506,516,517,518,519,520,525,527,528,529,531,550,552,553,554,556,575,581,600,601,602,603,604,605,606]
mustBeWhite = [26,27,28,29,30,44,45,46,47,48,51,55,69,73,76,80,94,98,101,105,119,123,126,127,128,129,130,144,145,146,147,148,442,443,444,467,469,476,477,478,479,480,492,493,494,501,505,526,530,551,555,576,577,578,579,580]
def getInput():
    print("----------------------------------------")
    print("---------Fake QR Code Generator---------")
    print("----------------------------------------")
    userIn = input("Please input the message you would like to encode\n> ")
    return userIn

def convertText(msg):
    #This will convert the given msg to binary and return it
    text = ''.join(format(ord(i), '08b') for i in msg)
    print("\""+msg+"\"" + " In binary evaluated to be "+ text)
    return text
    
def generatePng(arr):
    cmap = {0: (255,255,255),
            1: (0,0,0),}
    data = [cmap[letter] for letter in arr]
    img = Image.new('RGB', (height, len(arr)//width), "white")
    img.putdata(data)
    img.save("output.png", "PNG") 
    
def createQRTemplate(arr):
    #This will apply the QR code template boxes to the array in the proper positions.
    for i in mustBeBlack:
        arr[i] = 1
    for j in mustBeWhite:
        arr[j] = 0
    return arr
        
def encodeMessage(msgArr, imgArr):
    #msgArr is the user data
    #baseArr is the QR template (THE ONE WITH 2S)
    msgCounter = 0
    for i in range(len(imgArr)):
        if msgCounter == len(msgArr):
            return imgArr
        if imgArr[i] == 2:
            imgArr[i] = msgArr[msgCounter]
            msgCounter += 1
    return imgArr

def makeArr(userInput):
    arr = []
    userList = list(userInput)
    for i in range(len(userList)):
        arr.append(int(userList[i]))
    return arr  

def addFiller(arr):
    for i in range(len(arr)):
        if arr[i] == 2:
            arr[i] = randint(0,1)
    return arr
             
def main():
    userMessage = getInput()
    userBinary = convertText(userMessage)
    userArr = makeArr(userBinary)
    tempArr = createQRTemplate(img)
    newImg = encodeMessage(userArr, tempArr)
    finalArr = addFiller(newImg)
    print("QR Code Output to output.png")
    
    generatePng(finalArr)
    
if __name__ == "__main__":
    main()
    


