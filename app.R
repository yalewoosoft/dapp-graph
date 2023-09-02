#
# This is a Shiny web application. You can run the application by clicking
# the 'Run App' button above.
#
# Find out more about building applications with Shiny here:
#
#    http://shiny.rstudio.com/
#

library(shiny)
library(dplyr)
library(ggplot2)
# Define UI for application that draws a histogram
ui <- fluidPage(

  # Application title
  titlePanel("Dapp data from github"),

  # Sidebar Control
  sidebarLayout(
    sidebarPanel(
      dateInput("date1", "From:", value="2020-01-01"),
      dateInput("date2", "To:")
    ),
    mainPanel(
      plotOutput("distPlot")
    )
  ),
)

# Define server logic required to draw a histogram
server <- function(input, output) {

  output$distPlot <- renderPlot({
    dappData = read.csv("dataset.csv") %>% filter(date >= input$date1) %>% filter(date <= input$date2)
    dappData$index = seq(1, nrow(dappData))
    g = ggplot(data=dappData, mapping=aes(index,count)) +
      xlab("Date") +
      ylab("Count of Solidity repos") +
      geom_point()
    return(g)
  })
}

# Run the application
shinyApp(ui = ui, server = server)
