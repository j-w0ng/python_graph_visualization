
import pandas as pd
from gmplot import gmplot

vancouver_file_path = "/Users/jonathan/Downloads/csv_street_trees/StreetTrees_CityWide.csv"

vancouver_data = pd.read_csv(vancouver_file_path)

vancouver_data_cn = vancouver_data.set_index("COMMON_NAME", drop=False)

# filter all cherry blossom trees
cherry_blossom = vancouver_data_cn.loc["KWANZAN FLOWERING CHERRY", :]

# extracting latitude and longitude
cherry_blossom_location = cherry_blossom[["LATITUDE", "LONGITUDE"]]

# removing all trees without location
cherry_blossom_location_final = cherry_blossom_location.loc[cherry_blossom_location["LATITUDE"] > 0]

locations = cherry_blossom_location_final.to_numpy()

lats = []
longs = []
for l in locations:
    lats.append(l[0])
    longs.append(l[1])

# center location near QE park
gmap = gmplot.GoogleMapPlotter(49.238680, -123.139569, 13)

gmap.heatmap(lats, longs)

gmap.draw("cherry_blossoms.html")

