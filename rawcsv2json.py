#!/usr/bin/env python3
# (c) 2016 David A. van Leeuwen

## This file converts a "raw" tye of csv file from the PoW database into a json.

## Specifically,
## - we use a short label (first line in the general CSV header)
## - "NULL" entries are simply left out
## - numbers are interpreted as numbers, not strings


#####

# Script modified and extended by Jitske Aya Lucretia Koeleman (a.k.a. Jazzy Jitske)
## Modification: David's code worked from commandline, it was edited to work in Spyder 
## Extension: Everything described below

# Goal
## Select Nobel Prize Winners from PoW database 
## Write only the necessary info to csv file 

#Functioning
## The script loops through a specified number of years
## Selects nobel prize laureates through two different ways
## Then writes info to a csv file
## - with only the columns necessary
## - and adds another column coding for which Nobel Prize was won 
## The last part of the script checks some things 

##############################################################################

## input = any country name, corrects it to be in line with the pycountry package
from correctcountryname import correctname, savedict
import json, logging, csv, re, sys, codecs

floatre = re.compile("^\d+\.\d+$")
intre = re.compile("^\d+$")

file = "h.txt"
header=[]
for line in open(file):
    header.append(line.strip())
logging.info("%d lines in header", len(header))

## Function provided by David
def process_csv(file, header):
    out=[]
    stdin = file == "-"
    fd = sys.stdin if stdin else codecs.open(file, 'r', 'UTF-8')
    reader = csv.reader(fd)
    for nr, row in enumerate(reader):
        logging.debug("%d fields in line %d", len(row), nr)
        d = dict()
        out.append(d)
        for i, field in enumerate(row):
            if field != "NULL":
                if floatre.match(field):
                    d[header[i]] = float(field)
                elif intre.match(field):
                    d[header[i]] = int(field)
                else:
                    d[header[i]] = field
    if not stdin:
        fd.close()
    return out

## Specify year range 
year_min = 1810
year_max = 2000

## Specify key & value to select on
key1 = "award_label"
search_term1 = "nobel"
exclude_term1 = "ig nobel prize"

## Select another key & value to select on
key2 = "22-rdf-syntax-ns#type_label"
search_term2 = "nobellaureate"

## Lists to check the award_label later on
award_list1 = []
award_list2 = []

## Lists to check the 22-rdf-syntax-ns#type_label later on
label_info1 = []
label_info2 = []

## List with only Nobel Prize winners
output_Nobel_Winners1 = []
output_Nobel_Winners2 = []
output_Nobel_Winners_both = []

## Go through a range of years specified before 
for year in range(year_min, year_max):

    file = "years\\" + str(year)

    ## Temporarily save year to tmp, only add person to final list if Nobel Prize Winner
    tmp = process_csv(file, header)
    for person in tmp:
        
        ## If the person has an awardlabel, check if it has "Nobel Prize" in it 
        ##(if the value was NULL, the formula before has removed it)
        
        won_Nobel = False
        if key1 in person:
            if search_term1 in person[key1].lower():
                if exclude_term1 not in person[key1].lower():
                
                    ## Add to a list with the Nobel Winners
                    output_Nobel_Winners1.append(person)
                    output_Nobel_Winners_both.append(person)
                    
                    ## Make a list that has the awards won by every person selected, to check later
                    award_list1.append(person[key1])
                    label_info1+=[[person[key2],person['rdf-schema#label']]]
                                   
                    won_Nobel = True
        
        ## The same as above, but for a new search_term     
        if key2 in person:
            if search_term2 in person[key2].lower():
                
                ## Add to a new list 
                output_Nobel_Winners2.append(person)
                
                label_info2+=[[person[key2],person['rdf-schema#label']]]
                if not won_Nobel:
                    output_Nobel_Winners_both.append(person)
                               
                ## Add award label
                if key1 in person:
                    award_list2.append(person[key1])
        

#with open('NobelPrize1830-2000.v2.json', 'w') as file:
#    json.dump(output_Nobel_Winners1, file, indent=4)            
    
desired_keys = [
                'birthName',
                'rdf-schema#label',
                'award_label',
                #'award',
                'birthDate',
                'birthYear',
                'birthPlace_label',
                'deathDate',
                'deathPlace_label',
                'citizenship_label',
                #'country',
                #'ethnicity_label',
                'nationality_label',
                'stateOfOrigin_label',
                #'gender_label',
                #'discipline_label',
                #'instution_label',
                #'profession_label',
                #'university_label',
                'almaMater_label',
                'field_label',
                '22-rdf-syntax-ns#type_label',
                'nobel_prize'
                ]
## Official Prize Names as found in key-value pair 1 and  
prize_names = [
               "Nobel Memorial Prize in Economic Sciences", 
               "Nobel Prize in Chemistry", 
               "Nobel Prize in Physics",
               "Nobel Peace Prize",
               "Nobel Prize in Physiology or Medicine",
               "Nobel Prize in Literature"
               ]

not_prize_names = ["Ig Nobel Prize"]

## Prize labels in key-value pair 2
nobel_22ref_label_names = [
                           "NobelLaureatesInEconomics",
                           "NobelLaureatesInChemistry",
                           "NobelLaureatesInPhysics",
                           "NobelPeacePrizeLaureates",
                           "NobelLaureatesInPhysiologyOrMedicine",
                           "NobelLaureatesInLiterature"                           
                           ]

## Open the output CSV file we want to write to
with open('NobelPrize1830-2000-NULL-v4.csv', 'w', newline='',encoding='utf-8') as file:
    csvwriter = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
    csvwriter.writerow(desired_keys)
    
    ## Loop through the dictionaries belonging to eaech Nobel Laureate 
    for person_dictionary in output_Nobel_Winners_both:
        tmp = []
        
        ## Add the value belonging to the key that we want to our tmp list,
        ## if there's no value: "NULL"
        for key_entry in desired_keys:
            
            won_prize = False
            
            ## If the column-name is in the dictionary, append the value
            if key_entry in person_dictionary:
                if key_entry == 'nationality_label':
                    tmp.append(correctname(person_dictionary[key_entry]))
                else: tmp.append(person_dictionary[key_entry])
                    
            
            ## When we get to the column-name nobel_prize, add Nobel Prize Name
            elif key_entry == 'nobel_prize': # and key1 in person_dictionary:
                
                ## Look at the award_label column
                if key1 in person_dictionary:
                    
                    
                    ## There are a couple coded "{Nobel Prize|Physiology}" 
                    if not won_prize and "{Nobel Prize|Physiology}" in person_dictionary[key1]:
                        tmp.append("Nobel Prize in Physiology or Medicine")
                        won_prize = True
                        
                    ## Check which prize name is in there    
                    for prize in prize_names:
                        
                        ## Append the prize name
                        if not won_prize and prize in person_dictionary[key1]:
                            tmp.append(prize)
                            won_prize = True
                            
                ## Look at the "22-rdf-syntax-ns#type_label" column, if the last column is still empty
                if key2 in person_dictionary and tmp[-1] not in prize_names:
                    
                    
                    for label in range(len(nobel_22ref_label_names)): 
                        
                        ## Check if the labels are in the "22-rdf-syntax-ns#type_label"
                        ## and then assign the corresponding prize name to the nobel_prize column
                        if not won_prize and nobel_22ref_label_names[label] in person_dictionary[key2]:
                            tmp.append(prize_names[label])
                            won_prize = True
                            
                ## If there is no prize identified, make it "NULL"
                if not won_prize:
                    tmp.append("NULL")
                            
            
            ## If there is no info available, write "NULL"
            else:
                tmp.append("NULL")       
            
        csvwriter.writerow(tmp)
    
## Save the dictionary of countries that have been inputted into the correctname function    
savedict()

                #print(json.dumps(out, indent=4, ensure_ascii=True))
                #json.dumps(out, indent=4, ensure_ascii=True)


### The code below checks if the above Nobel Prizes are in the award labels 
### and else prints something else in there
### This is not essential to write the dataset

check_if_nobel_prize1 = []
check_if_nobel_prize2 = []

for entry in award_list1:
    
    count = 0
    
    
    for prize in range(len(prize_names)):
        if prize_names[prize] in entry:
            count += 1
    if count == 0:
        check_if_nobel_prize1.append(entry)
        
#print(check_if_nobel_prize1)
   

 
for entry in award_list2:
    
    count = 0
    for prize in range(len(prize_names)):
        if prize_names[prize] in entry:
            count += 1
    if count == 0:
        check_if_nobel_prize2.append(entry)
            
#print(check_if_nobel_prize2)


## Code below checks which new persons are added by using search_term2 (vs search_term1)
## to see if it outputted Nobel Laureautes and to see the info that belongs to them
not_in_outNobel1 = []
not_in_Nobel1_names = []
for label2 in range(len(label_info2)):
    duplicate = False
    for label1 in range(len(label_info1)):
        if label_info1[label1][0] == label_info2[label2][0]:
            duplicate = True 
    
    if not duplicate:
        not_in_outNobel1.append(label_info2[label2])
        not_in_Nobel1_names.append(label_info2[label2][1])
        
        
#print(not_in_Nobel1_names)


with open('checkout.json', 'w') as file:
    json.dump(not_in_outNobel1, file, indent=4)          
    
#with open('POI.json', 'w') as file:
#    json.dump(POI_info, file, indent=4)       
