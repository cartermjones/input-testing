#This is similar to the other input tester, but it uses regular expressions
#in place of checking the name against a list of illegal characters.

#To use regular expressions in Python, we must first import re from the standard library.
import re

#Here is the modified inputTester function.
def inputTester(name):
   #First we load our regular expression into a rule variable.
   #We want to match anything that it alphabetic or whitespace.
   rule = re.compile(r'[A-Za-z ]*')
   #Then we run a fullmatch of the name passed into this function.
   check = rule.fullmatch(name)
   
   #If the name doesn't completely match the input (i.e., contains non-alphabetic and whitespace characters) it won't return
   #a match. This will prompt the function to return False, which will let the script below know what to do.
   if check == None:
       return False
   #If everything matches up with our regular expression, the name gets the all-clear.    
   else:
       return True
   
#Here we have the main script nested in a try/except block. Because who knows?
#This is for all intents and purposes the same as the input_tester.py file in this repo. 
#For an in-depth description of what's going on here... check that. Thanks.
try:
    name = input("What is your name? ")
    if inputTester(name) is False:
        print("That isn't a name.")
    else:
        print("Nice to meet you, " + name + "!")
except TypeError:
    print("Something went quite wrong.")
    raise
