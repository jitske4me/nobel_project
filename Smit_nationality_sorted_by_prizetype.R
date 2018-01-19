library('tidyverse')
library('lubridate')
library('xtable')
library('ggthemes')
nationality_data = read.csv('NobelPrize1810-2000-NULL-v4.csv')
# summary(nationality_data) #Browsing around in data

#Making a table with a only the necessary columns
nationality.table.2 <- nationality_data %>%
  select(rdf.schema.label, nationality_label, nobel_prize)

# Making a table of the nationalites and frequencies
nationality.count.2 <- nationality.table.2 %>%
  group_by(nationality_label) %>%            # Grouping by nationality
  filter(nationality_label != 'NULL') %>%    # Selecting only the onces with the nationality filled in
  summarise(n()) %>% 
  arrange(desc(`n()`)) %>%
  top_n(15)

nobel.top15nationality <- nationality.table.2 %>%
  filter(nationality_label %in% nationality.count.2$nationality_label)

# Barplot of the most frequent nationalities, showing the different categories of the prizes
ggplot() +
  geom_bar(data=nobel.top15nationality,      # Choosing the data of the top 15 nationalities
           mapping=aes(x=nationality_label, fill=nobel_prize)) +    # The x axis has the nationalities and the filling is based on Prize
  ggtitle("Top 15 nationalities sorted by type of Nobel Prize") +   # Graph title
  xlab("Nationality") + ylab("Frequency") +  # Labeling axis
  theme_tufte() +                            # Formatting of text and axis, using the packet 'ggthemes'
  scale_fill_brewer(palette="Spectral") +    # Nice colour scheme
  labs(fill = "Nobel Prize") +               # Legend title
  coord_flip()                               # Flip the x and y axis

# Giving the columns sensible names
names(nationality.count.2) <- c('Nationality','Frequency')

# Print to Latex
print(xtable(nationality.count.2, type = "latex"), file = "nationality_count_15_prizes_set2.tex")