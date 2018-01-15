#!/usr/bin/env python3
# (c) 2016 David A. van Leeuwen

## This file converts a "raw" tye of csv file from the PoW database into a json.

## Specifically,
## - we use a short label (first line in the general CSV header)
## - "NULL" entries are simply left out
## - numbers are interpreted as numbers, not strings

import json, logging, csv, re, sys, codecs

floatre = re.compile("^\d+\.\d+$")
intre = re.compile("^\d+$")

file = "h.txt"
header=[]
for line in open(file):
    header.append(line.strip())
logging.info("%d lines in header", len(header))

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


out = []

## Specify year range 
year_min = 1830
year_max = 2000

## Specify key & value to select on
key = "award_label"
search_term = "Nobel prize"

## List with only Nobel Prize winners
out_Nobel = []

## Go through a range of years specified before 
for year in range(year_min, year_max):

    count = 0
        #for file in ["years\\" + str(year)]: #,"years\\1941","years\\1845"]: #args.raw:
    file = "years\\" + str(year)
        #current_output = process_csv(file, header)
    tmp = process_csv(file, header)
    for person in tmp:
        
        ## If the person has an awardlabel, check if it has "Nobel Prize" in it 
        ##(if the value was NULL, the formula before has removed it)
        if key in person:
            if "Nobel Prize" in person[key]:
                
                ## Add to a new list 
                out_Nobel.append(person)


## For person in out        
#for person in range(len(out)):
#    
#    ## If the person has an awardlabel, check if it has "Nobel Prize" in it 
#    ##(if the value was NULL, the formula before has removed it)
#    if key in out[person]:
#        if "Nobel Prize" in out[person][key]:
#            
#            ## Add to a new list 
#            out_Nobel += [out[person]]

with open('NobelPrize1830-2000.v2.json', 'w') as file:
    json.dump(out_Nobel, file, indent=4)
              
            
            
#desired_keys = [
#                'award_label',
#                'award',
#                'birthDate',
#                'birthName',
#                'birthPlace_label',
#                'birthYear',
#                'citizenship_label',
#                'country',
#                'deathDate',
#                'deathPlace_label',
#                'discipline_label',
#                'ethnicity_label',
#                'gender_label',
#                'instution_label',
#                'nationality_label',
#                'profession_label',
#                'university_label'
#                ]
#            
            
#            for the_key_of_desire in desired_keys:
#                if (the_key_of_desire in out[person]) == True:
#                    out_award += [out[person][the_key_of_desire]]
#            
          
            
#            
#            out_award += [out[person]['award_label'],
#                          out[person]['award'],
#                          out[person]['birthDate'],
#                          out[person]['birthName'],
#                          out[person]['birthPlace_label'],
#                          out[person]['birthYear'],
#                          out[person]['citizenship_label'],
#                          out[person]['country'],
#                          out[person]['deathDate'],
#                          out[person]['deathPlace_label'],
#                          out[person]['discipline_label'],
#                          out[person]['ethnicity_label'],
#                          out[person]['gender_label'],
#                          out[person]['instution_label'],
#                          out[person]['nationality_label'],
#                          out[person]['profession_label'],
#                          out[person]['university_label']
#                        ]    


            

                #print(json.dumps(out, indent=4, ensure_ascii=True))
                #json.dumps(out, indent=4, ensure_ascii=True)

    
    