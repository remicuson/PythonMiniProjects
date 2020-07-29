import folium
import pandas as pd

# Read in the Volcanoes text which has the locations
df = pd.read_csv("Volcanoes.txt")
lat = df["LAT"].values
lon = df["LON"].values
elevations = df["ELEV"].values
status = df["STATUS"].values

coordinates = []
for i in range(len(lat)):
    coordinates.append([lat[i], lon[i]])

current_status = []
for i in range(len(elevations)):
    info = str(elevations[i]) + "\n" + status[i]
    current_status.append(info)

map = folium.Map(location=[38.58, -99.09], zoom_start=4, tiles="Stamen Terrain")

# Adding a marker to the map
fg = folium.FeatureGroup(name="My Map")
for coordinate, info in zip(coordinates, current_status):
    fg.add_child(folium.Marker(location=coordinate, popup=info, icon=folium.Icon(color='green')))
map.add_child(fg)
map.save("Map1.html")

