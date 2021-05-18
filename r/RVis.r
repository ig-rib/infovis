library("ggplot2")
library("readxl")
library("rworldmap")

# https://stackoverflow.com/questions/22625119/choropleth-world-map

excel <- read_excel('./infovis/r/Costof1GBofData.xlsx')
print(excel)

excelMap <- joinCountryData2Map(
    excel,
    nameJoinColumn='Country',
    joinCode="NAME")

mapDevice("x11")

mapCountryData(excelMap,
nameColumnToPlot='Avg Price of 1GB (USD)',
catMethod='fixedWidth',
numCats=100)