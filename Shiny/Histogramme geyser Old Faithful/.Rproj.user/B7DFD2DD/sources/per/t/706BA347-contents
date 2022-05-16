## Pauline M. Perrin
## 16/05/2022

# This is a Shiny web application. You can run the application by clicking
# the 'Run App' button above.
#
# Find out more about building applications with Shiny here:
#    http://shiny.rstudio.com/
#

library(shiny)

# On définit une interface utilisateur pour l'application qui permette de dessiner un histogramme
# qui affiche les durées entre deux éruptions du geyser Old Faithful
ui <- fluidPage(

    # On donne un titre à l'application
    titlePanel(textOutput("title")),

    sidebarLayout(
        sidebarPanel(
          textInput("title",
                    "Main title :",
                    "Durées entre deux éruptions du geyser Old Faithful"),
         
          uiOutput("dataVariables"),
          
          # On entre le nombre de bins c'est-à-dire la taille d'une classe
          sliderInput("bins",
                        "Nombre de bins:",
                        min = 1,
                        max = 50,
                        value = 30),
          
          # On donne à l'utilisateur la possibilité de personnaliser la couleur des classes
          radioButtons("color",
                       "Color of bins:",
                       choices = c("Lavender" = "lavender",
                                   "Light blue" = "lightblue",
                                   "Light pink" = "lightpink"))
        ),

        # On affiche un graphique de la répartition ainsi générée : 
        mainPanel(
           plotOutput("distPlot"),
           textOutput("textBins")
        )
    )
)

# On definit le serveur logique qui est requis pour dessiner un histogramme
server <- function(input, output) {
    # On demande à l'utilisateur de donner un titre à l'histogramme 
    output$title <- renderText({
    input$title
})
    
    output$distPlot <- renderPlot({
        # génère des classes suivant la taille de classe indiquée par l'utilisateur à 
        # l'étape précédente
        x    <- faithful[, 2]
        bins <- seq(min(x), max(x), length.out = input$bins + 1)

        # dessine l'histogramme avec le nombre spécifique de bins
        hist(x, breaks = bins, col  = input$color, border = 'white')
    })

# On précise sous l'histogramme la taille des classes : 
    output$textBins <- renderText({
      c("Il y a actuellement", input$bins,input$color, "bins.")
    })


## Si on utilise maintenant ggplot : 
library(tidyverse)

datasetInput <- reactive({
  switch(input$data,
         "faithful" = faithful)
  })

output$histogram <- renderPlot({
  ggplot(data = datasetInput(), aes_string(x = input$variable)) + 
    geom_histogram(bins = input$bins, fill = input$color, color = "white")
  })

}

# Run the application 
shinyApp(ui = ui, server = server)




