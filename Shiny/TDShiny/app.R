## Pauline M. Perrin
## 16/05/2022

# This is a Shiny web application. You can run the application by clicking
# the 'Run App' button above.
#
# Find out more about building applications with Shiny here:
#    http://shiny.rstudio.com/
#

library(shiny)

# On construit une interface utilisateur qui permette de construire un histogramme en fonction
# du nombre choisi par l'utilisateur

ui <- fluidPage(
    sliderInput(inputId = "num", label = "Choisir un nombre", 
                value = 25, min = 1, max = 100),
    plotOutput("hist") 
    )
    server <- function(input, output) { 
        output$hist <- renderPlot({
            hist(rnorm(input$num)) 
        })
}
shinyApp(ui = ui, server = server)

