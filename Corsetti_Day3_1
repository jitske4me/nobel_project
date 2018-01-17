#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 14:51:23 2018

@author: leacaterinacorsetti
"""

import csv
import os

with open("processed_countries_1.csv") as file:
    countries = list(csv.DictReader(file))

country_location = {}
for country in countries:
    country_location[country['name']] = country

with open("NobelPrize1830-2000-nationality_v1.csv") as file:
    nobels = list(csv.DictReader(file))

output = []
for nobel in nobels:
    if nobel['nationality_label'] != 'NULL' and nobel['nationality_label'] in country_location:
        country_info = country_location[nobel['nationality_label']]
        output.append([nobel['rdf-schema#label'], nobel['nationality_label'], nobel['award_label'],
                             country_info['lat'], country_info['lon']])
        
with open("nobel_coordinates.csv", "w", newline="", encoding="utf8") as file:
    csvwriter = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
    csvwriter.writerow(['name', 'nationality_label', 'prize', 'lat', 'lon'])
    csvwriter.writerows(output)