# -*- coding: utf-8 -*-
"""
Created 15-01-2018 to 18-01-2018

@author: Daan Sanders
with additional elements by Teun van Gils and Joska de Lange


This code takes the Nobel dataset as made in the other Python script (by Jitske);
it processes this data to output a .csv file, with all unique combinations of a laureate and one of their 
alma mater universities (i.e. if a laureate has multiple degrees, he/she will appear multiple times in the
output, paired with every degree university once).
The code also corrects for some shortcomings of the dataset.
"""
import csv
with open('NobelPrize1810-2000-NULL-v4.csv','r', encoding="utf8") as nobelfile:
    nobeldata = list(csv.DictReader(nobelfile))
  
      
#check for opening curly brace {
    #if it does have one , it has multiple values 
        #select for only values after { and before }
        #split for '|'
        #put into a table
    #else list under 1st 
   
    
# data entries on the alma maters (values in the almaMater_label column) were structered as follows:
    #{University of Amsterdam|Leiden University}. Hence, the dictionaries needed to be split by the |
output = []
for items in nobeldata:                                 # loops over the persons in the data set
    alma_mater_raw = items['almaMater_label']           # makes a variable of the alma mater values
    if alma_mater_raw != "NULL":                        # removes the empty alma mater entries
        if alma_mater_raw[0] == '{':                    # for names with multiple uni's, starts looking at the beginning of the dictionaries
            alma_maters = alma_mater_raw[1:-1].split('|') # reads values between '{' and '}', splits by the |
            for alma_mater in alma_maters:
                output.append([items['rdf-schema#label'], alma_mater]) #adds  name and split alma maters in lists
        else:                                               
            output.append([items['rdf-schema#label'], alma_mater_raw])  #adds name and mater if there is only 
                                                                        #one alma mater in the data set

# the following lines correct for the subsidiaries in the alma mater data, only for the most recurring uni's                               
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
    if result[1] == 'St Hugh\'s College Oxford':
        result[1] =  'University of Oxford'    

# these lines produce the actual .csv file to be opened in R
# importantly, it includes the 'encoding to uft8' to prevent most character interpretation problems
# it makes a file, writes the headers of 'name' and 'alma mater' on the first row, and the output lists
# on the subsequent rows            
with open('Nobel_alma_mater_Daan_final.csv', 'w', newline='', encoding="utf8") as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
    csvwriter.writerow(['name', 'Alma_mater'])
    csvwriter.writerows(output)