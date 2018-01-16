library('tidyverse')
library('lubridate')
Nobel <- read.csv('NobelPrize1830-2000.csv')

summary(Nobel)

#http://rstudio-pubs-static.s3.amazonaws.com/7953_4e3efd5b9415444ca065b1167862c349.html

Nobel$birthYear <- as.Date(Nobel$birthYear, format = "%Y-%m-%d")
Nobel$birthYear <- format(Nobel$birthYear, format = "%Y")
Nobel$birthYear

Nobel$birthYear <- as.numeric(Nobel$birthYear)

hist(Nobel$birthYear, #x value
     breaks = 150, #number of cells
     xlab = "Birth Year",  #x-axis label
     main = "Histogram of Laureate's birth years", #plot title
     ylim = c(0, 20))


