import folium
import pandas as pd

# Function to give different color such as green, :
def color_producer(elevations):
    colors = []
    for i in range(len(elevations)):
        if elevations[i] < 1000:
            colors.append('green')
        elif 1000 <= elevations[i] < 3000:
            colors.append('orange')
        else:
            colors.append('red')

    return colors

# Read in the Volcanoes text which has the locations
df = pd.read_csv("Volcanoes.txt")
lat = df["LAT"].values
lon = df["LON"].values
elevations = df["ELEV"].values
status = df["STATUS"].values
colors = color_producer(elevations)
coordinates = []
for i in range(len(lat)):
    coordinates.append((lat[i], lon[i]))

current_status = []
for i in range(len(elevations)):
    info = str(elevations[i]) + "m" + "\n" + status[i]
    current_status.append(info)

map = folium.Map(location=[38.58, -99.09], zoom_start=4, tiles="Stamen Terrain")

# Adding a marker to the map
fg = folium.FeatureGroup(name="My Map")
for coordinate, info, color in zip(coordinates, current_status, colors):
    fg.add_child(folium.CircleMarker(location=coordinate, radius=10.0, popup=info, color='grey', weight=1, opacity=3, fill=True, fill_color=color, fill_opacity=0.7))
map.add_child(fg)
map.save("Map1.html")
help(folium.CircleMarker)

