library("ggplot2")
library("readxl")
library("rnaturalearth")
library("rnaturalearthhires")
library("sp")
library("sf")
library("ggiraph")

excel <- read_excel('./infovis/r/Costof1GBofData.xlsx')

world <- ne_countries(scale = "medium", returnclass = "sf") 
worldExcel <- merge(world, excel, by.x="name", by.y="Country", all.x=TRUE)

worldmap2 <- ggplot(data=worldExcel) +
    geom_sf_interactive(aes(
        fill=AP,
        tooltip = paste0("Country = ", name, "\n Price of 1GB (USD) = ", AP)), lwd=0.1) +
    scale_fill_gradientn(colours = c("lightblue", "lightgreen", "green", "orange", "red", "black"),
                       breaks=c(0,1,2,10, 20, 30),
                       na.value = "grey")

wm4 <- girafe(code,
ggobj=worldmap2,
options = list(opts_tooltip(use_fill = TRUE),
                                   opts_zoom(min = 1, max = 5)))

show(wm4)