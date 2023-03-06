from random_word import Wordnik
from PyDictionary import PyDictionary
from textblob import Word
import string

def hangmangame():

    print("\n\nHello and welcome to HANGMAN, a Program made by Liam Finnie, Please wait while a word is generated, Guess the word correctly and escape The Hangman, guessing incorrect words will bring about your demise, correctly guessed letters in the word are revealed.")

    dictionary=PyDictionary()
    newhangmanword = "-"

    definition_results = None

    wordnik_service = Wordnik()                                                            #defining function of Wordnik which is an online dictionary that a word is selected from when called using the random_word libary

    while definition_results is None or "-" in newhangmanword or " " in newhangmanword:    #loop to select different words from Wordnik Libary until word found Pydictionary can lookup a definition for (PyDictionary does not work with words with spaces etc)
        newhangmanword  = "Africa" #wordnik_service.get_random_word(minLength=5)                     #using random_word libary and Wordnik to select a random word 
        definition_results = (dictionary.meaning(newhangmanword, disable_errors=True))
        

    propernoun = 0

    wordinlist = list(newhangmanword)                                        #creating list from the word to guess for easier variable manipulations

    if wordinlist[0].isupper() is True:
        propernoun = 1


    print(propernoun)    

    print(newhangmanword)
    print(wordinlist)



    wordsize = int(len(newhangmanword))
    revealletterslist = ["_"] * wordsize                                     #creating correctly sized reveallist to populate with letter guesses of user

    #for i in range(wordsize):                                               #revealing hyphens within words to create more fair gameplay experience (only relevant with certain Wordnik words)
        #if wordinlist[i] == '-':
            #revealletterslist[i] = '-'
    
    hangman = (                                                              #hangman art to output with appropiate lives remaining with every user guess

    """
    _________
        |/        
        |              
        |                
        |                 
        |               
        |                   
        |___                 
        """,

    """
    _________
        |/   |      
        |              
        |                
        |                 
        |               
        |                   
        |___                 
        """,

    """
    _________       
        |/   |              
        |   (_)
        |                         
        |                       
        |                         
        |                          
        |___                       
        """,

    """
    ________               
        |/   |                   
        |   (_)                  
        |    |                     
        |    |                    
        |                           
        |                            
        |___                    
        """,


    """
    _________             
        |/   |               
        |   (_)                   
        |   /|                     
        |    |                    
        |                        
        |                          
        |___                          
        """,


    """
    _________              
        |/   |                     
        |   (_)                     
        |   /|\                    
        |    |                       
        |                             
        |                            
        |___                          
        """,



    """
    ________                   
        |/   |                         
        |   (_)                      
        |   /|\                             
        |    |                          
        |   /                            
        |                                  
        |___                              
        """,


    """
    ________
        |/   |     
        |   (_)    
        |   /|\           
        |    |        
        |   / \        
        |               
        |___           
        """)

    lives =  0                                                                       #counter for while loop for how many guesses the user has left
    livesleft = 7                                                                    #counter in while loop to allow user to keep track of guesses the user has left

    usedletterlist = []                                                              #list to be filled with guessed letters, tracked and outputted to user
    usedwordlist = []                                                                #list to be filled with guessed words, tracked and outputted to user

    alphabet = list(string.ascii_letters)                                            #list for if statements checking if letter guesses are appropiate inputs or not
    punctuation = list(string.punctuation)                                           #list for if statements checking if word guesses have inappriopiate punctuation in(the word guess must only be letters)

    while lives < 7: 

        guessedlettersstringconvert = [str(x) for (x) in revealletterslist]          #converting the lists into strings every parse to be outputted for better user experience(i.e. "_ _ _ _" not "[ _, _, _, _ ]")
        guessedletters = ""
        guessedletters = guessedletters.join(guessedlettersstringconvert)
        guessedletters = "  ".join(guessedletters)

        usedlettersstringconvert = [str(x) for (x) in usedletterlist]                
        usedletters = ""
        usedletters = usedletters.join(usedlettersstringconvert)
        usedletters = "  ".join(usedletters)


        pcount = 0
        guessproper = ""


        guess = input(f"{hangman[lives]} \n\nYou have {livesleft} lives left, gusss the word or a letter, choose wisely!\n\n {guessedletters}\n\nThese letters have already been guessed   {usedletters}\n\nThese words have already been guessed {usedwordlist}\n\n ").lower()
        guessinlist = list(guess)
        print(guessinlist[0])       
        if propernoun == 1 and len(guess) > 1:          
            capitalconvert = guessinlist[0]
            capitalconvert = capitalconvert.upper()
            guessinlist[0] = capitalconvert
            guessproper = "".join(guessinlist)
            print(guess)
        elif propernoun == 1 and len(guess) <2:
            guesscapitalletter = guess.upper()     
        
        spellcheck = Word(guess)
        spellingresult = spellcheck.spellcheck()                                    #used in if statement checking if the user spell their guess correctly
        spellcheckstringconvert = [str(x) for (x) in spellingresult[0]]
        spellchecks = ""
        spellchecks = spellchecks.join(spellcheckstringconvert)
        spellchecks = "".join(spellchecks)

        print(spellchecks)
        for i in range (0, len (guess)):                                            #counter for characters in guesses that aren't letters(used in if statements enforcing guesses only use letters and no other characters)
            if guess[i] in punctuation:  
                pcount = pcount + 1  
        if len(guess) < 2 and guess in wordinlist:  #if user guesses singular letter(s) that is(are) in the word
            livesleft = livesleft -1       
            lives = lives +1
            usedletterlist.append(guess)
            indices = [i for i in range(wordsize) if wordinlist[i] == guess]
            while len(indices) > 0:                                                 #seperating Indexes of guessed letters within the correct word and manipulating to allow duplicate letter placement within the reveal letter list    
                revealletterslist[indices[0]] = guess                               #using loop with a created list of the index values that is parsed through deleting items from the list of index values with pop function to make sure letters go to indexes of reveal letter list correctly without overlap
                indices.pop(0)        
        elif guess == newhangmanword or guessproper == newhangmanword:                                               #if user guesses the word
            print(f"\n\n{newhangmanword} is the correct word!, you have escaped the hangman for now...\n\n")
            lives = 8
            exit()
        elif len(guess) == 1 and guess in usedletterlist:                           #if user guesses a letter already guessed
            print("\n\nYou have already guessed this letter") 
        elif len(guess) > 1 and guess in usedwordlist:                              #if user guesses a word already guessed
            print("\n\nYou have already guessed this word")      
        elif guess not in alphabet and len(guess) <2 or pcount > 0:                 #if user gives an inappropiate input (not a letter or a word containing anything besides letters)
            print("\n\nYou have not provided a letter or word, please try again 1")
        elif guess+"1.0" not in spellchecks:                                        #if user gives a word guess that is spelled incorrectly
            print("The word you have guessed is spelled incorectly, please try again")
        elif len(guess) == 1:                                                       #if user guesses a letter not in the word
            livesleft = livesleft -1  
            lives = lives +1        
            usedletterlist.append(guess)
        elif len(guess) >1 and guess not in usedwordlist:                           #if user guesses an incorrect word
            livesleft = livesleft -1  
            lives = lives +1  
            usedwordlist.append(guess)  

    askdef = input(f"\n\n {hangman[7]}\n\nYou could not guess the word, it is you for who the bell tolls, the word was {newhangmanword}\n\n Would you like the definition of the word? y/n").lower()

   


    while askdef != "n": 

        if askdef == "y":
            print(definition_results)
            break            
        else: 
            askdef = input("Would you like the definition of the word? y/n").lower()

    playagain = ""

    while playagain != "n" or "y":    
        if playagain.casefold() == "y":
            hangmangame()    
        elif playagain == "n":
            exit()
        else:
            playagain = input("Would you like to play again? y/n").lower()                                                                                  

hangmangame()

                                                                                    #Things to Add
                                                                                    #Get API Key from Wordnik(to use Wordnik definitions alongside the random word generation -> increase amount of word possibilities including hypenations and Proper Nouns etc)                                                                      
                                                                                    #Proper Nouns Logic? Capital Letters
                                                                                    