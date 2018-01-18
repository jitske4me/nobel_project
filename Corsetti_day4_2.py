#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 14:26:30 2018

@author: leacaterinacorsetti
"""

import csv

with open("NobelPrize1810-2000-NULL-v4.csv") as file:
    Country_frequency = list(csv.DictReader(file))
with open("processed_countries_1.csv") as file:
    countries = list(csv.DictReader(file))

country_location = {}
for country in countries:
    country_location[country['name']] = country



output = []

for nationality in Country_frequency:
    if nationality ['nationality_label'] != 'NULL' and nationality ['nationality_label'] in country_location:
        country_info = country_location[nationality['nationality_label']]
        output.append([nationality['rdf-schema#label'], nationality['nationality_label'], nationality['award_label'],
                             country_info['lat'], country_info['lon']])

#        
#with open("nobel_frequency.csv", "w", newline="", encoding="utf8") as file:
#    csvwriter = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
#    csvwriter.writerow(['name', 'nationality_label', 'prize', 'lat', 'lon'])
#    csvwriter.writerows(output)