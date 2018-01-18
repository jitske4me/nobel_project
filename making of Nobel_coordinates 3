#full credit to Joska and Teun
import csv

with open("processedcountries1_modified_1.csv") as file:
    countries_content = list(csv.reader(file))

# run through all countries with lat/long info, and store as dict: {'country name' : [lat, long]}
country_location = {} #for running the country list agaist the original file that we wanted to use    
for element in countries_content[1:]: # skip header line
    if len(element[0].split(';')) > 3: # ensure more than 3 elements separated by semicolons
        split_entry = element[0].split(';') # split by semicolons
        country_location[split_entry[0]] = [split_entry[3], split_entry[4]] # country_location[name] = [lat, lon]

#test:
print("The Netherlands has latitude " + country_location['Netherlands'][0] + " and longitude " + country_location['Netherlands'][1])



with open("NobelPrize1810-2000-NULL-v4.csv") as file:
    nobels = list(csv.DictReader(file))

output = []
for nobel in nobels:
    if nobel['nationality_label'] != 'NULL' and nobel['nationality_label'] in country_location:
        country_info = country_location[nobel['nationality_label']]
        output.append([nobel['rdf-schema#label'], nobel['nationality_label'], nobel['nobel_prize']] + country_info)
    
#combining data into new file that is written   
with open("nobel_coordinates_3.csv", "w", newline="", encoding="utf8") as file:
    csvwriter = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
    csvwriter.writerow(['name', 'nationality_label', 'prize', 'lat', 'lon'])
    csvwriter.writerows(output)
