#! /usr/bin/python
# Joey Hommel and Tyler Harding
# CSEC-464 Final Project
# Prof Pan

from PIL import Image


filename = input("Enter the filename of the QR Code you wish to decode\n> ")
image = Image.open(filename)
width, height = image.size

#These lists define the indicies of the "boxes" of a 25x25 QR Code
mustBeBlack = [0,1,2,3,4,5,6,18,19,20,21,22,23,24,25,31,43,49,50,52,53,54,56,68,70,71,72,74,75,77,78,79,81,93,95,96,97,99,100,102,103,104,106,118,120,121,122,124,125,131,143,149,150,151,152,153,154,155,156,168,169,170,171,172,173,174,416,417,418,419,420,441,445,450,451,452,453,454,455,456,466,468,470,475,481,491,495,500,502,503,504,506,516,517,518,519,520,525,527,528,529,531,550,552,553,554,556,575,581,600,601,602,603,604,605,606]
mustBeWhite = [26,27,28,29,30,44,45,46,47,48,51,55,69,73,76,80,94,98,101,105,119,123,126,127,128,129,130,144,145,146,147,148,442,443,444,467,469,476,477,478,479,480,492,493,494,501,505,526,530,551,555,576,577,578,579,580]

pixval = list(image.getdata())

def convert_to_binary():
    for i in range(len(pixval)):
        if pixval[i] == (0,0,0):
            pixval[i] = 1
        elif pixval[i] == (255,255,255):
            pixval[i] = 0
        else:
            raise Exception("Error in QR Code")

def carve_boxes():
    '''
    This function carves out the typical QR Code boxes from being interpreted as the message.
    '''
    new_binary = list()
    for i in range(len(pixval)):
        #if not (pixval[i] == 1 and i in mustBeBlack):
        if i not in mustBeBlack and i not in mustBeWhite:
            new_binary.append(pixval[i])
    return new_binary
            
def bits_to_bytes(bit_list):
    bytes_list = [bit_list[i:i+8] for i in range(0, len(bit_list), 8)]
    return bytes_list

def bytes_to_chars(byte_list):
    result_string = ''
    for byte in byte_list:
        try:
            binary_string = ''.join(map(str, byte))
            decimal_value = int(binary_string, 2)
            if decimal_value == 13 or decimal_value not in range(32, 128):
                break
            character_representation = chr(decimal_value)
            result_string += character_representation
        except:
            break
    return result_string


def main():
    convert_to_binary()
    carved = carve_boxes()
    bytes_list = bits_to_bytes(carved)
    result = bytes_to_chars(bytes_list)
    print(result)

if __name__ == "__main__":
    main()
