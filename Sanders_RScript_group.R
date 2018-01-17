library('tidyverse')
library('lubridate')


nobeldata = read.csv('NobelPrize1830-2000-NULL-v2.csv')
#summary(nobeldata)

#plan on the years:filter for the birthDate, Lea will filter for birthYear
#nobeldata$birthDate[0] date data is read as factor, change it to dates to be able to isolate the year
nobeldata$birthDateTemp = as.Date(nobeldata$birthDate, format="%Y-%m-%d")
birthDateYear = format(nobeldata$birthDateTemp, format("%Y"))
nobeldata$birthDateYear =  birthDateYear

nobeldata$birthDateYearNum = as.numeric(nobeldata$birthDateYear)
hist(nobeldata$birthDateYearNum, #x value
     breaks = 150, #number of cells
     xlab = "Birth Year",  #x-axis label
     main = "Histogram of Laureate's birth years from $birthDate", #plot title
     ylim = c(0, 20))

#alma mater data
alma_mater_data = read.csv('Nobel_alma_mater_Daan.csv')

#unique(alma_mater_data$Alma_mater)

mater.count <- alma_mater_data %>%
  group_by(Alma_mater) %>%     
  summarise(n()) %>%
  arrange(desc(`n()`))
#mater.count.15 = mater.count %>%
#  filter(Alma_mater == 'Harvard University')
#mater.count.15 = mater.count %>%
# filter(n0 > 8)
# mater.count.15

mater.count.15 = mater.count[1:15,]


install.packages('xtable')
library('xtable')
print(xtable(mater.count.15, type = "latex"), file = "alma_mater_table_15.tex")
#use xtable to export the product into Latex

mater.count.15$frequency <- mater.count.15$`n()` 
#mater.count.15$frequency rm

ggplot(data = mater.count.15) + 
  geom_bar(mapping = aes(x = Alma_mater, fill = Alma_mater), show.legend = FALSE)+
  coord_flip()
  