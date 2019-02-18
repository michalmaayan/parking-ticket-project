import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)
import folium
from folium import plugins
from folium.plugins import HeatMap

MY_LOCATION = [40.843609, -73.885085]
START_ZOOM = 18 # MAX ZOOM=18 , MIN ZOOM = 1


map = folium.Map(location=MY_LOCATION, zoom_start=START_ZOOM)
folium.Marker(location=MY_LOCATION, popup='I am here').add_to(map)


heat_df = pd.read_csv('data.csv', dtype=object)

# Ensure you're handing it floats
heat_df['Latitude'] = heat_df['Latitude'].astype(float)
heat_df['Longitude'] = heat_df['Longitude'].astype(float)

heat_df = heat_df[['Latitude', 'Longitude']]
heat_df = heat_df.dropna(axis=0, subset=['Latitude', 'Longitude'])

# List comprehension to make out list of lists
heat_data = [[row['Latitude'], row['Longitude']] for index, row in heat_df.iterrows()]

# Plot it on the map
HeatMap(heat_data).add_to(map)

# open the saved map in browser
map.save('index.html')
