# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 11:22:55 2018

@author: Joska de Langen
Please credit author, and explain functioning of the script in report
"""

'''
This script checks whether a country name exists in a list of 
all countries (downloaded from the internet - needs to be loaded in and saved as [list])
If it doesn't exist, it asks you to retype the name until it is found in list of all countries
It links the wrongly typed country names to the correctly spelled ones, and saves this dictionary to a file which is loaded at startup (if it exists)
'''


import os, ast, pycountry, json

# countrylist contains all correct country names
countrylist = []

for i in range(len(pycountry.countries)):
    countrylist.append(list(pycountry.countries)[i].name)
   
list(pycountry.countries)[0].name

# incoming countries is a list of all country names encountered in succession by your script
#incomingcountries = []

# countrydict links all incorrectly spelled country names to correct spellings
# countrydict = {} # should be loaded in from file at start

if os.path.exists('countrydictionary.dict'):
    print("Country dictionary loaded\n")
    with open('countrydictionary.dict', 'r+') as dictfile:
        #print(dictfile.readlines()[0])
        countrydict = ast.literal_eval(dictfile.readlines()[0])
        #print(countrydict)
#else: countrydict = {}  

selection_nationality = 'nationality_label'

#with open('NobelPrize1830-2000.json') as my_file:
#    data = json.load(my_file)
#    for entry in data:
#        if selection_nationality in entry:
#            incomingcountries.append(entry[selection_nationality]) 
#print(incomingcountries)

def correctname(incountry):
    if incountry in countrylist:
        return incountry
    elif incountry in countrydict: # if incorrect spelling already in dictionary
        return countrydict[incountry]
    else:
        newcountryname = "thisisnotacountry" # Reset variable 
        while(newcountryname not in countrylist): # As long as retyped name does not exist in full country list
            newcountryname = input("Country not recognized: " + incountry + ". Please retype: \n") # prompt to enter correct spelling
        countrydict[incountry]=newcountryname # save incorrect spelling and correct spelling of country in dictionary
        return newcountryname
    

#for item in incomingcountries:
#    print(correctname(item))    

# Save dictionary to file        
def savedict():
    with open('countrydictionary.dict', 'w') as dictfile:
        dictfile.write(str(countrydict))