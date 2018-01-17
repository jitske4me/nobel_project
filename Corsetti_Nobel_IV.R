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

#mytempdata = merge('country', 'Nobel')

#country(df)[which(country(df)=='denonym')] <-'nationality_label'
#require(dbplyr)
#df=rename(df, nationality_label = denomyn)
