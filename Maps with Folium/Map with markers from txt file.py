import folium
import pandas

# creating pandas data frame from txt file
df = pandas.read_csv('.\\Maps with Folium\\Volcanoes-USA.txt')

# creating map
# finding the center location for the map using the values from the input file
# it's equal to average latitude and average longitude
map = folium.Map(location=[df['LAT'].mean(), df['LON'].mean()], tiles='stamen terrain', zoom_start=4)


# assinging coordinates, elevation and names from the data frame
# marker color depends on the elevation

def color(elev):
    minimum = int(min(df['ELEV']))
    maximum = int(max(df['ELEV']))
    step = int((maximum - minimum) / 3)

    if elev in range(minimum, minimum + step):
        col = 'green'
    elif elev in range(minimum + step, minimum + step + step):
        col = 'orange'
    else:
        col = 'red'
    return col


for lon, lat, name, elev in zip(df['LON'], df['LAT'], df['NAME'], df['ELEV']):
    map.add_child(folium.Marker(location=[lat, lon], popup=name, icon=folium.Icon(color=color(elev))))

# saving map
map.save('.\\Maps with Folium\\Volcanoes-USA.html')
