# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 2018

@author: Daan
"""

#import json
import csv
with open('NobelPrize1810-2000-NULL-v4.csv','r', encoding="utf8") as nobelfile:
    nobeldata = list(csv.DictReader(nobelfile))
 
    
    
    
# import csv
#     reader = csv.DictReader(csvfile)   
      
 ## for splitting Alma Mater values
   
#check for opening curly brace {
    #if it does have one , it has multiple values 
        #select for only values after { and before }
        #split for '|'
        #put into a table
    #else list under 1st 
    
output = []
for items in nobeldata:
    alma_mater_raw = items['almaMater_label']
    if alma_mater_raw != "NULL":
        if alma_mater_raw[0] == '{':
            alma_maters = alma_mater_raw[1:-1].split('|')
            for alma_mater in alma_maters:
                output.append([items['rdf-schema#label'], alma_mater])
        else: #print item in column 1
            output.append([items['rdf-schema#label'], alma_mater_raw])
                                 
for result in output:
    if result[1] == 'Trinity College Cambridge':
        result[1] = 'University of Cambridge'
for result in output:
    if result[1] == 'St. John\'s College Cambridge':
        result[1] = 'University of Cambridge'       
for result in output:
    if result[1] == 'Jesus College Cambridge':
        result[1] = 'University of Cambridge' 
for result in output:
    if result[1] == 'Harvard College':
        result[1] =  'Harvard University'
for result in output:
    if result[1] == 'Harvard Law School':
        result[1] =  'Harvard University'
for result in output:
    if result[1] == 'Harvard Medical School':
        result[1] =  'Harvard University'
for result in output:
    if result[1] == 'Columbia University College of Physicians and Surgeons':
        result[1] =  'Columbia University'
for result in output:
    if result[1] == 'Columbia Law School':
        result[1] =  'Columbia University'    
for result in output:
    if result[1] == 'Johns Hopkins School of Medicine':
        result[1] =  'Johns Hopkins University'    
for result in output:
    if result[1] == 'Johns Hopkins School of Medicine':
        result[1] =  'Johns Hopkins University'    
for result in output:
    if result[1] == 'Merton College Oxford':
        result[1] =  'University of Oxford'    
for result in output:
    if result[1] == 'St Catherine\'s College Oxford':
        result[1] =  'University of Oxford'    
for result in output:
    if result[1] == 'St Hugh\'s College Oxfordd':
        result[1] =  'University of Oxford'    

                  
with open('Nobel_alma_mater_Daan_final.csv', 'w', newline='', encoding="utf8") as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
    csvwriter.writerow(['name', 'Alma_mater'])
    csvwriter.writerows(output)