# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 11:22:55 2018

Based on a script written by Joska de Langen 
Modified by Quirine Smit
"""

'''
This script checks whether a country name exists in a list of 
all countries (downloaded from the internet - needs to be loaded in and saved as [list])
If it doesn't exist, it asks you to retype the name until it is found in list of all countries
It links the wrongly typed country names to the correctly spelled ones, and saves this dictionary to a file which is loaded at startup (if it exists)
'''

# Importing relevant packages. Note we imported a package with country names called pycountry
import os, ast, pycountry, json

# countrylist is a list which contains all correct country names
countrylist = []

# Adding the correctly spelled country names form the pycountry package to the country list
for i in range(len(pycountry.countries)):
    countrylist.append(list(pycountry.countries)[i].name)

# If the file countrydictionary.dict exsists, load it in, otherwise start with an empry dictionary 
if os.path.exists('countrydictionary.dict'):
    print("Country dictionary loaded\n")    # Print this to know that this step went well
    with open('countrydictionary.dict', 'r+') as dictfile:
        countrydict = ast.literal_eval(dictfile.readlines()[0])
else: countrydict = {}  

selection_nationality = 'nationality_label'

# Making a function which is called from the rawcsv2json file.
# Input an (incorrect) spelling of a country name. 
def correctname(incountry):
    # If the country name is in the list then return that name:
    if incountry in countrylist:
        return incountry
    # If it is not, but the incorrect spelling is in the dictionary, then return the matched correct spelling:
    elif incountry in countrydict:
        return countrydict[incountry]
    # If it is not in the dictionary, then ask the person to fill in the correct country name. It will check if the country is correctly spelled.
    else:
        newcountryname = "thisisnotacountry" # Reset variable 
        while(newcountryname not in countrylist): # As long as retyped name does not exist in full country list
            newcountryname = input("Country not recognized: " + incountry + ". Please retype: \n") # prompt to enter correct spelling
        countrydict[incountry]=newcountryname # save incorrect spelling and correct spelling of country in dictionary
        return newcountryname
      
# Save dictionary to file        
def savedict():
    with open('countrydictionary.dict', 'w') as dictfile:
        dictfile.write(str(countrydict))