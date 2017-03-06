import folium

# creating map for a given coordinates

# Map tileset to use. Can choose from this list of built - in tiles:
# - "OpenStreetMap"
# - "MapQuest Open"
# - "MapQuest Open Aerial"
# - "Mapbox Bright"(Limited levels of zoom for free tiles)
# - "Mapbox Control Room"(Limited levels of zoom for free tiles)
# - "Stamen"(Terrain, Toner, and Watercolor)
# - "Cloudmade"(Must pass API key)
# - "Mapbox"(Must pass API key)
# - "CartoDB"(positron and dark_matter)

map = folium.Map(location=[54.5207254,18.5285852], tiles='cartodb positron',zoom_start=13)

# creating markers on the map
map.simple_marker(location=[54.5195714,18.5511835], popup='ORP Blyskawica', marker_color='red')

# creating a HTML file with the map
map.save('my map.html')