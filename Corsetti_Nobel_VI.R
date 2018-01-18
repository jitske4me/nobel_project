#drawing the final graphs which includes frequency of nobel laureates in the size of the dot

library('tidyverse')
library('data.table')
Nobel <- read.csv('nobel_coordinates.csv')
install.packages("ggthemes")
frequency <- read.csv("country_and_frequency.csv")
library(ggthemes)
library(ggmap)
library(maps)
library(mapdata)

#plotting correct final version of map with correct data set
ggplot(data=frequency) + theme_tufte() +
  geom_polygon(data = map_data('world'), mapping = aes(x = long, y = lat, group=group), fill='grey', colour='white') +
  geom_point(data=frequency, mapping = aes(x=lon, y=lat, size= nationality_freq, colour= nationality_label), alpha = 0.9)
 
