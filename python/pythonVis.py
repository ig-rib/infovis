import pandas as pd
import geopandas as gpd
import altair as alt
import json
from vega_datasets import data


# Read 1GB Dataset Excel
df = pd.read_excel('./Costof1GBofData.xlsx')
# Read world countries dataset
worldCountries = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
worldCountries = worldCountries[worldCountries.name != 'Antarctica']
# Merge both datasets, add centroids
worldCountries = worldCountries.merge(df, right_on='Country', left_on='name', how='outer')
worldCountries['centroid_lon'] = worldCountries['geometry'].centroid.x
worldCountries['centroid_lat'] = worldCountries['geometry'].centroid.y

# # Convert to JSON
# choroJson = json.loads(worldCountries.to_json())
# # Convert to altair Data
# choroData = alt.Data(values=choroJson['features'])

countriesWithData = worldCountries.dropna()
choroDataJson = json.loads(countriesWithData.to_json())
choroData = alt.Data(values=choroDataJson['features'])

countriesWithoutData = worldCountries[(worldCountries.Country.isnull()) | (worldCountries['Avg Price of 1GB (USD)'].isnull())]
choroNoDataJson = json.loads(countriesWithoutData.to_json())
choroNoData = alt.Data(values=choroNoDataJson['features'])

base = alt.Chart(
    choroData,
    title='Cost of 1GB in different Countries'
).mark_geoshape(
    stroke='black',
    strokeWidth=1
).encode(
).properties(width=1200, height=1200)

baseNoData = alt.Chart(
    choroNoData).mark_geoshape(
    fill='gray',
    stroke='black',
    strokeWidth=1
).encode(
).properties(width=1200, height=1200)

choro = alt.Chart(choroData
).mark_geoshape(
    # fill='lightgray',
    # stroke='black'
).encode(
    alt.Color("properties['Avg Price of 1GB (USD)']",
    type='quantitative',
    scale=alt.Scale(scheme='bluegreen'),
    title = 'Cost of 1 GB'
    )
)
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

onegb = base + baseNoData + choro + tooltip #+ baseNoData #+ labels
onegb.show()