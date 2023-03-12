import string

def simpleencrypt():

    letters = string.ascii_letters #importing string libaries to create a list of characters                         
    numbers = string.digits
    symbols = string.punctuation

    characters = letters + numbers + symbols
    characters = characters + characters #double the list to ensure when the shifting of index values happens an index out of range error does not occur


    print("\n\nWelcome to a simple encryption/decryption program created by Liam Finnie\n\n")

    message = input("\n\nWhat is the message you want to Encode or Decode?\n\n")


    shift = "null"  #declaring variables for while loop
    shiftlist = list(shift)

    while shift.isdigit() == False: #enforce the user only gives a number
        shift = input("\n\nPlease input the number of letters a shift happens in this cipher, only whole numbers are accepted as an answer \n\n")
        
    shift = int(shift)
    shift = shift % (len(characters)/2) #use the mod function so any index shift value the user gives will work


    ok = 0 #declaring variables for while loop
    encrypt = "null"

    while ok != 1: #enforce the user only gives option to decode or encode
        encrypt = input("\n\nDo you want to encode or decode this message? Type 1 for Decode, Type 2 for Encode\n\n")
        if encrypt == "1" or encrypt == "2":
            ok = 1

    if encrypt == "1": #inversing the shift value to move index of message strings backwards if decoding
        shift *= -1


    newmessage = ""

    for char in message:

        if char in characters: #shifting orginal index values to encrypt or decrypt message
            index = characters.index(char)           
            encodedindex = index + shift
            encodedindex = int(encodedindex)
            newmessage += characters[encodedindex]       
        else: #if user gives an element not within the list of characters such as a space " "   
            newmessage += char
    
        
    if encrypt == "1":
        print(f"\n\nAfter Decryption of your message, the message was revealed to be '{newmessage}.'\n\n")
    elif encrypt == "2":
        print(f"\n\nAfter Encryption of your message, the message has become '{newmessage}'.\n\n")    


    restart = input("\n\nWould you like to encrypt or decrypt further messages? y/n\n\n")

    while restart != "n" or "y":    
            if restart.casefold() == "y":
                simpleencrypt()    
            elif restart == "n":
                exit()
            else:
                restart = input("\n\nWould you like to encrypt or decrypt further messages? y/n\n\n")

simpleencrypt()            

#Additional Ideas and Challenges:
#add complexity with randomize function alongside cipher with index shifting