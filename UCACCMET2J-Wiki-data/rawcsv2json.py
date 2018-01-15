#!/usr/bin/env python3
# (c) 2016 David A. van Leeuwen

## This file converts a "raw" tye of csv file from the PoW database into a json.

## Specifically,
## - we use a short label (first line in the general CSV header)
## - "NULL" entries are simply left out
## - numbers are interpreted as numbers, not strings

import argparse, json, logging, csv, re, sys, codecs

floatre = re.compile("^\d+\.\d+$")
intre = re.compile("^\d+$")

def read_header(file="h.txt"):
    header=[]
    for line in open(file):
        header.append(line.strip())
    logging.info("%d lines in header", len(header))
    return header

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



if __name__ == "__main__":
    header = read_header(args.header)
    out = []
    year_min = 1830
    year_max = 1870
    key = 'award_label'
    out_award = []
    
    for year in range(year_min, year_max):

        count = 0
        for file in ["years\\" + str(year)]: #,"years\\1941","years\\1845"]: #args.raw:
            out += process_csv(file, header)
 
#            
#            if (key in out[count]) == True:
#                if ("Nobel Prize" in out[count][key]) == True:
#                    out_award += [out[count]]
#             
#            count += 1

        
        for person in range(len(out)):
            if (key in out[person]) == True:
                if ("Nobel Prize" in out[person][key]) == True:
                    out_award += [out[person]]    

            

#        with open('theyears.json', 'w') as file:
#            json.dump(out, file, indent=4)
                #print(json.dumps(out, indent=4, ensure_ascii=True))
                #json.dumps(out, indent=4, ensure_ascii=True)

    
workwith = out[1]

#key = 'award_label'
#out_award = []
#
for person in range(len(out)):
    if (key in out[person]) == True:
        if ("Nobel Prize" in out[person][key]) == True:
            out_award += [out[person]]
#        
print(out_award)
    
    
    
    