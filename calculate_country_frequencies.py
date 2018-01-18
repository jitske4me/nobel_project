# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 15:00:33 2018

@author: Jitske Aya Lucretia Koeleman (a.k.a. Jazzy Jitske)
"""
# Goal
## The goal of this code is to create a csv file containing the frequency of 
## Nobel Prize winners per country, including lat and lon  
## output form is ['nationality_label', 'nationality_freq', 'lat', 'lon']

# Functioning 
## This code opens a file in which only Nobel Laureates that have a nationality_label are listed
## Creates a list with all the info for the countries, with frequency = 0
## Goes through the entries in the nobels list and calculates the country frequencies
## Writes to csv file


import csv

## Open a file which has ['name', 'nationality_label', 'prize', 'lat', 'lon']
## For only the laureates that have a nationality label
with open("nobel_coordinates_3.csv", encoding = 'utf-8') as file:
    nobels = list(csv.reader(file))


## Create empty list, which will eventually contain the final output file
output_with_country_and_freq = []
## Create empty set, to see which countries were already added to the output file
unique_nationalities = set()
for person in range(1, len(nobels)):
    
    ## check if the country is in the set, if not add the information for that 
    ## country to the output list
    if nobels[person][1] not in unique_nationalities:
        output_with_country_and_freq.append([nobels[person][1], 0, nobels[person][3], nobels[person][4]])
    
    unique_nationalities.add(nobels[person][1])


## Calculates the nationality frequency for each country
for entry in range(1, len(nobels)):
   
    for country in range(len(output_with_country_and_freq)):
        if nobels[entry][1] == output_with_country_and_freq[country][0]:
            output_with_country_and_freq[country][1]+=1
        
## Write to csv file
with open("country_and_frequency.csv", "w", newline="", encoding="utf8") as file:
    csvwriter = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
    csvwriter.writerow(['nationality_label', 'nationality_freq', 'lat', 'lon'])
    csvwriter.writerows(output_with_country_and_freq)    
    
## This piece below is not necessary for the code, it is just to check the 
## number of Nobel prize winners that have their nationality coded, to check 
## if the code works correctly
total_nat = 0        
for line in range(len(output_with_country_and_freq)):
    total_nat += output_with_country_and_freq[line][1]
        