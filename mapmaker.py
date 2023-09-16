import pandas as pd
import folium

csv_file_path = 'enter/path/to/csv/file.csv'
data = pd.read_csv(csv_file_path)

# Process latitude and longitude values with directions
def process_coordinates(coord_with_direction):
    numeric_part = float(coord_with_direction[:-1])
    direction = coord_with_direction[-1]
    if direction in ['S', 'W']:
        return -numeric_part
    else:
        return numeric_part

# Apply the process_coordinates function only to rows with directions
data['Latitude'] = data['Latitude'].apply(lambda x: process_coordinates(x) if isinstance(x, str) else x)
data['Longitude'] = data['Longitude'].apply(lambda x: process_coordinates(x) if isinstance(x, str) else x)

# Create a base map centered at a certain location
map_center = [data['Latitude'].mean(), data['Longitude'].mean()]
my_map = folium.Map(location=map_center, zoom_start=5)

# Add markers for each point
for index, row in data.iterrows():
    folium.Marker([row['Latitude'], row['Longitude']]).add_to(my_map)

# Save the map as an HTML file
map_file_path = 'output/file/path.html'
my_map.save(map_file_path)