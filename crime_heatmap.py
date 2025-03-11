import folium
from folium import plugins
import pandas as pd


data = pd.read_csv('datasets/crime_data.csv')

# Step 2: Initialize the map centered around the city's average coordinates
city_map = folium.Map(location=[data['latitude'].mean(), data['longitude'].mean()], zoom_start=12)

# Step 3: Add a base heatmap layer for all crimes
heat_data = data[['latitude', 'longitude']].values.tolist()
plugins.HeatMap(heat_data, name='All Crimes').add_to(city_map)

# Step 4: Add separate heatmap layers for each crime type
crime_types = data['crime_type'].unique()
for crime in crime_types:
    crime_data = data[data['crime_type'] == crime]
    heat_data = crime_data[['latitude', 'longitude']].values.tolist()
    heat_layer = plugins.HeatMap(heat_data, name=crime, show=False)
    city_map.add_child(heat_layer)

# Step 5: Add clickable markers with detailed crime information
for idx, row in data.iterrows():
    folium.Marker(
        location=[row['latitude'], row['longitude']],
        popup=f"Type: {row['crime_type']}<br>Date: {row['date']}<br>Description: {row['description']}",
        icon=folium.Icon(color='red', icon='info-sign')
    ).add_to(city_map)

# Step 6: Add layer control to toggle different crime types
folium.LayerControl().add_to(city_map)

# Step 7: Save the map to an HTML file
city_map.save('crime_heatmap.html')

print("Crime heatmap has been saved as 'crime_heatmap.html'. Open this file in a web browser to view the interactive map.")
