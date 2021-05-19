import pandas as pd
import geopandas as gpd
import altair as alt
import json
from vega_datasets import data


# Leer excel del dataset (lo voy a llamar '1GB') a representar
df = pd.read_excel('./infovis/python/Costof1GBofData.xlsx')
# Read world countries dataset
# Hubo que modificar un par de entradas del dataset 1GB para que los nombres de los países matchearan
# los nombres de los países en el dataset que se usa para representar países (naturalearth_lowres)
worldCountries = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

# Acá saqué a la Antártida porque era demasiado grande y no importaba
worldCountries = worldCountries[worldCountries.name != 'Antarctica']
# Mergeando los datasets 1GB y naturalearth_lowres. Se usa outer para mantener los datos geográficos de los países que
# no aparecen en el dataset 1GB. Como se ve, se busca que la columan "Country" del ds de 1GB matchee con la columna
# "name" del ds de naturalearth_lowres
worldCountries = worldCountries.merge(df, right_on='Country', left_on='name', how='outer')

# Se añaden los centroides, al principio era para agregar texto en el centro del país
worldCountries['centroid_lon'] = worldCountries['geometry'].centroid.x
worldCountries['centroid_lat'] = worldCountries['geometry'].centroid.y

# Ahora lo que se hace es dividir el df en dos: los países que tienen datos y los que no
# Para cada uno, se toman los datos en json y se los convierte a un elemento altair.Data, para su representación
# Creo que se puede hacer directo con dataframes pero así funcionó primero y no tuve la necesidad de cambiarlo

# Para los que tienen datos se eliminan las filas que tienen NaNs, que son, en este caso, sólo las que 
# no tienen datos en el field "Country" o en el field "Avg Price of 1GB (USD)"
countriesWithData = worldCountries.dropna()
choroDataJson = json.loads(countriesWithData.to_json())
choroData = alt.Data(values=choroDataJson['features'])

# Esto es el complemento del conjunto anterior
countriesWithoutData = worldCountries[(worldCountries.Country.isnull()) | (worldCountries['Avg Price of 1GB (USD)'].isnull())]
choroNoDataJson = json.loads(countriesWithoutData.to_json())
choroNoData = alt.Data(values=choroNoDataJson['features'])

# A continuación se van creando las capas

# base = alt.Chart(
#     choroData,
#     title='Cost of 1GB in different Countries'
# ).mark_geoshape(
#     stroke='black',
#     strokeWidth=1
# ).encode(
# ).properties(width=1200, height=1200)

# baseNoData: tiene los bordes de los países que no tienen datos.
# Para estos países, elo fondo es gris.

baseNoData = alt.Chart(
    choroNoData).mark_geoshape(
    fill='gray',
    stroke='black',
    strokeWidth=0.2
).encode(
).properties(width=1200, height=1200)

# choro: llena los países con colores según las escala establecida (en encode)
# Como se ve, esta escala está basada en el precio promedio de 1GB

choro = alt.Chart(choroData,
    title='Cost of 1GB in different Countries'
).mark_geoshape(
    # fill='lightgray',
    stroke='black',
    strokeWidth=1
).encode(
    alt.Color("properties['Avg Price of 1GB (USD)']",
    type='quantitative',
    scale=alt.Scale(scheme='bluegreen', type='log'),
    title = 'Cost of 1 GB'
    )
)

# tooltip: es lo que permite que se muestre el tooltip cuando se hace hover over.
# Se muestra nombre del país y precio del GB. Hay que hacerlo por separado porque
# si lo hacía en choro tiraba error como si no lo estuviera haciendo sobre ningún dataset
# Asumo que es porque no se puede hacer las 2 features (coloreo según esquema y tooltips) en una
# misma sentencia

tooltip = alt.Chart(choroData
).mark_geoshape(
    fill='transparent',
    stroke='black'
).encode(
    tooltip=[alt.Tooltip('properties.Country:O', title="Country"), alt.Tooltip("properties['Avg Price of 1GB (USD)']:Q", title="1GB Price (USD)")],
)
# labels = alt.Chart(countriesWithData).mark_text(baseline='top').properties(width=1200, height=1200).encode(
#     longitude='properties.centroid_lon:Q',
#     latitude='properties.centroid_lat:Q',
#     text="properties['Avg Price of 1GB (USD)']:Q",
#     size=alt.value(8),
#     opacity=alt.value(5)
# )

# Al final se superpone todo. Importa el orden o para definir posiciones relativas (más adelante/atrás)
# se pasa el parámetro baseline='[la posición que se quiera según las opciones de altair, p. ej=top]'

onegb = baseNoData + choro + tooltip #+ baseNoData #+ labels
onegb.show()