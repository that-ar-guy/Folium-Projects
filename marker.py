import folium
import pandas as pd

# Load the dataset
# file_path = "Indian_Monuments.csv"  # Update with the actual file path
data = pd.read_csv("datasets\indian_monuments_coordinates.csv")

# Initialize a Folium map centered on India
india_map = folium.Map(location=[20.5937, 78.9629], zoom_start=5)

# Loop through the dataset and add markers
for index, row in data.iterrows():
    folium.Marker(
        location=[row['Latitude'], row['Longitude']],
        popup=f"{row['Monument']}",
        icon=folium.Icon(color="blue", icon="info-sign")
    ).add_to(india_map)

# Save the map to an HTML file
india_map.save("indian_monuments_map.html")

print("Map has been saved as indian_monuments_map.html. Open it in a browser to view.")
