import string
import random 

print("Welcome to the Password Generator Program made by Liam Finnie\n\n")

howmanyletters = input("how many letters do you want in your password? ")
howmanysymbols = input("how many symbols do you want in your password? ")
howmanynumbers = input("how many numbers do you want in your password? ")

#converting to integers to allow easier variable manipulation

howmanyletters = int(howmanyletters)
howmanysymbols = int(howmanysymbols)
howmanynumbers = int(howmanynumbers)

pwsize = howmanyletters + howmanysymbols + howmanynumbers

#importing Lists from string Libary for random generation of variables from said lists (not hardcoding every possible letter,symbol,number)

alphabet = list(string.ascii_letters)
numbers = list(range(0, 10))
symbol = list(string.punctuation)

#newletter = alphabet[random.randint(0, len(alphabet)-1)]     Code that pulls random item out of appropiate list that will be in while loops
#newsymbol = symbol[random.randint(0, len(symbol)-1)]
#newnumber = numbers[random.randint(0, len(numbers)-1)]

password = ["null"] * pwsize #creating a list of null values with length of the asked for password to allow randomized placement of new variables replacing null values


l = 0                        #defining variables used in appropiate while loops
s = 0
n = 0

while l < howmanyletters: #generating amount of random letters required in password and randomizing positioning within password length, this is why a populated list of null values is created, so items in the list already have a predetermined placement to replace
    newletter = alphabet[random.randint(0, len(alphabet)-1)]
    placement = random.randint(0, pwsize-1)  
    if password[placement] == "null":
        password[placement] = newletter
        l = l +1 
    
while s < howmanysymbols:
    newsymbol = symbol[random.randint(0, len(symbol)-1)]
    placement = random.randint(0, pwsize-1)  
    if password[placement] == "null": 
        password[placement] = newsymbol
        s = s +1

while n < howmanynumbers:
    newnumber = numbers[random.randint(0, len(numbers)-1)]
    placement = random.randint(0, pwsize-1)  
    if password[placement] == "null": 
        password[placement] = newnumber
        n = n +1     

pwstringconvert = [str(x) for (x) in password]   #converting list back to string
newpassword = ""
newpassword = newpassword.join(pwstringconvert)

print("\n\nYour Password is \n\n"+newpassword+ "\n\n")