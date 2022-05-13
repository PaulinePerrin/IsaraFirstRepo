library(tidyverse)
library(knitr)
data(starwars, package = "dplyr")
missing <- which(is.na(starwars$mass))
sw <- starwars[-missing, ]
sw.table <- sw %>% 
  filter(height >190)%>%
  mutate(mass_lb = mass * 2.2)%>%
  group_by(species)%>%
  summarize(Mean_Mass = mean(mass, na.rm = T))
kable(sw.table)

## Tibble vs data.frame

#Data Frame = Visiualiser son tableau de données 
data("iris")
dim(iris)
head(iris)
str(iris)

## tibble
tib_iris <- as_tibble(iris)
tib_iris

iris %>% 
  group_by(Species)%>%
  summarize(Mean_Mass = mean(Sepal.Length))