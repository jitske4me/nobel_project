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
search_term1 = "nobel"

## List with only Nobel Prize winners
out_Nobel = []

## Go through a range of years specified before 
for year in range(year_min, year_max):

    file = "years\\" + str(year)

    ## Temporarily save year to tmp, only add person to final list if Nobel Prize Winner
    tmp = process_csv(file, header)
    for person in tmp:
        
        ## If the person has an awardlabel, check if it has "Nobel Prize" in it 
        ##(if the value was NULL, the formula before has removed it)
        if key in person:
            if "nobel prize" in person[key].lower():
                
                ## Add to a new list 
                out_Nobel.append(person)
                
                
#491 "Nobel Prize"
#579 "nobel"
#2510 "nobel" and "prize"


#with open('NobelPrize1830-2000.v2.json', 'w') as file:
#    json.dump(out_Nobel, file, indent=4)
#                      
    
desired_keys = [
                'award_label',
                'award',
                'birthDate',
                'birthName',
                'birthPlace_label',
                'birthYear',
                'citizenship_label',
                'country',
                'deathDate',
                'deathPlace_label',
                'discipline_label',
                'ethnicity_label',
                'gender_label',
                'instution_label',
                'nationality_label',
                'profession_label',
                'university_label'
                ]

        
## Open the output CSV file we want to write to
with open('NobelPrize1830-2000.csv', 'w', newline='',encoding='utf-8') as file:
    csvwriter = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
    csvwriter.writerow(desired_keys)
    
    for dictionaries in out_Nobel:
        tmp = []
        
        for entry in desired_keys:
            if entry in dictionaries:
                tmp.append(dictionaries[entry])
            else:
                tmp.append(None)
    
        csvwriter.writerow(tmp)
    
    

                #print(json.dumps(out, indent=4, ensure_ascii=True))
                #json.dumps(out, indent=4, ensure_ascii=True)

    
    