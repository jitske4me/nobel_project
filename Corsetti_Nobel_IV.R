#creating a histogram of nobel laureate birth years
#code for final graph attached at the bottom of this file:

library('tidyverse')
#install.packages('data.table')
library('data.table')

country <- read.csv('processed_countries_1.csv')
require(dbplyr)
colnames(df)[which(colnames(df) == demonym)] <- 'nationality_label'

#colnames(df)(colnames(df)=='denonym') <- 'nationality_label' #this does not work, gives invalid function in complex assingment code


country_official <- read.csv('processed_countries.csv')
Nobel <- read.csv('NobelPrize1830-2000-NULL-v2.csv')

Nobel$birthYear <- as.Date(Nobel$birthYear, format = "%Y-%m-%d")
Nobel$birthYear <- format(Nobel$birthYear, format = "%Y")
Nobel$birthYear

Nobel$birthYear <- as.numeric(Nobel$birthYear)

hist(Nobel$birthYear, #x value
     breaks = 200, #number of cells
     xlab = "Birth Year",  #x-axis label
     main = "Histogram of Laureate's birth years", #plot title
     ylim = c(0, 20))

library('tidyverse')
library('data.table')
Nobel <- read.csv('nobel_coordinates.csv')
install.packages("maptools")
frequency <- read.csv("country_and_frequency.csv")
library(ggthemes)
library(ggmap)
library(maps)
library(mapdata)

#plotting correct final version of map with correct data set
ggplot(data=frequency) + theme_tufte() +
  geom_polygon(data = map_data('world'), mapping = aes(x = long, y = lat, group=group), fill='grey', colour='white') +
  geom_point(data=frequency, mapping = aes(x=lon, y=lat, size= nationality_freq, colour= nationality_label), alpha = 0.9)
