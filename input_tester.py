#This is a simple script that asks a user for a name,
#and if the name contains non-alphabetic symbols, 
#it chastises the user and terminates.
#Basic exception handling is included. (Just in case.)

#First we define the inputTester function, which will (naturally) do our input testing.
#Its only parameter is a name, which it will check to see contains only alphabetic symbols.
def inputTester(name):
    #This line breaks the name into a list of characters.
    nameList = list(name)
    #This line generates a list of non-alphabetic characters and passes them into a list.
    notLetters = list("01234567890!@#$%^&*()-_+=:;\"\'{}[],./<>?~\\`")
    
    #This is a Python-style for loop which uses the zip function to check the letters in name against the list of notLetters.
    for letter, notLetter in zip(nameList, notLetters):
        #If any symbol is not a letter, the function will return False.
        if letter in notLetters:
            return False
        #Otherwise it just continues looping.
        else:
            continue
    #Finally, if no non-Letters are caught, the function returns True.        
    return True
#Here we see our code nested in a lovely try/except block.    
try: 
    #The script prompts the user for input, in this case a name.
    name = input("What is your name? ")
    #Here we pass the name into the inputTester function to see if that bad boy is really a name.
    #If inputTester has returned False, the script chastises the user for their transgression.
    if inputTester(name) is False:
        print(name + " isn't a real name, you know.")
    #If the user has actually provided a name, the script is polite and greets them.
    else:
        print("Nice to meet you, " + name + ".")
#If anything should happen to go horribly wrong, the except block will raise the exception so that we can blast that bug 
#with the Holy Hand Grenade of Antioch.
except:
    raise
