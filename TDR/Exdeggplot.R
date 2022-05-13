## Pauline M. PERRIN

library(tidyverse)

data(starwars, package = "dplyr")
starwars

hist(starwars$height)

sw <- starwars %>% filter(mass<600)

plot(sw$mass~sw$height)

#mettre un + pour ajouter des étapes avec ggplot 

ggplot(data = sw)+
  aes(x=height, y=mass, colour=species)+
  geom_point()+
  geom_smooth(method = "lm")+
  theme_bw()#fond du graphique 