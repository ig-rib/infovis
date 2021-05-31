library("ggplot2")
# Esta librería se usa para abrir archivos .xlsx
library("readxl")
# Esta librería se usa para manipular los datos de países del mundo
library("sf")
# Esta librería se usa para obtener datos de los países del mundo
library("rnaturalearth")
# Esta librería se usa para hacer htmls a partir de plots gg, permite usar tooltips
library("ggiraph")

# Leer el excel (hubo que modificarlo para que los nombres de los países matchearan)
excel <- read_excel('./r/Costof1GBofData.xlsx')

# Fetchear datos de países del mundo
world <- ne_countries(scale = "medium", returnclass = "sf")

# Se combinan los datos del excel y los del mundo según el numbre del país, left outer join
worldExcel <- merge(world, excel, by.x="name", by.y="Country", all.x=TRUE)

# Se crea el mapa
worldmap2 <- ggplot(data=worldExcel) + # Se cargan los datos a ggplot
    geom_sf_interactive(aes( #Se crea un mapa interactivo. Los países se rellenan según el campo AP (avg price of 1GB (USD))
        fill=AP,
        tooltip = paste0("Country = ", name, "\n Price of 1GB (USD) = ", AP)), # Se crea el tooltip para mostrar info cuando se hace hover sobre los países
        lwd=0.1) +  # Se baja el grosor de las fronteras
    # Se agrega un gradiente con los colores y breaks siguientes (bastante intuitivo)
    scale_fill_gradientn(colours = c("lightblue", "lightgreen", "green", "blue", "darkblue", "black"),
                       breaks=c(0,1,2,5, 10, 20, 30),
                       na.value = "grey") +
    ggtitle("Averge Price of 1GB in the World (USD)")

wm4 <- girafe(
ggobj=worldmap2
,
# opts_zoom para poder hacer zoom (aparecen unos botones en la esq superior derecha)
options = list(opts_tooltip(use_fill = FALSE),
                                   opts_zoom(min = 1, max = 5))
)

show(wm4)