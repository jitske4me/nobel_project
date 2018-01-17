library('tidyverse')
library('data.table')

Country <- rbind(read.csv('processedcountries1_modified.csv'), c("NULL", "NULL", "NULL", "NULL", "NULL"))
Nobel <- read.csv('NobelPrize1830-2000-nationality_v1.csv')
Country$nationality_label <- Country$name
#mytempdata = merge(Country, Nobel, all=FALSE, by.x=Country$nationality_label, by.y=Nobel$nationality_label) #it does not work 
#only select columns with a non NULL value
# Nobel$nationality_label[Nobel$nationality_label != 'NULL'] 

both.attempt <- merge(Country,Nobel,by='nationality_label')

Nobel$nationality_label <- as.character(Nobel$nationality_label)
# Nobel$nationality_label[Nobel$nationality_label=='Russian Federation'] <- 'Russia'
nobel.coor <- Nobel %>%
  filter(
    nationality_label %in% Country$name
  ) %>%
  mutate(
    lat = ifelse(nationality_label %in% Country$name, Country$lat[Country$name == nationality_label], 0)
  ) %>%
  select(nationality_label, lat, everything())

Country$lat[Country$name == "Belgium"]