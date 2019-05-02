import pandas as pd
import numpy as np
from gmplot import gmplot


class Graph:

    unique_cn = None;
    vancouver_data_cn = None;

    def __init__(self):
        vancouver_file_path = "/Users/jonathan/Downloads/csv_street_trees/StreetTrees_CityWide.csv"
        vancouver_data = pd.read_csv(vancouver_file_path)
        self.vancouver_data_cn = vancouver_data.set_index("COMMON_NAME", drop=False)

        common_names = self.vancouver_data_cn["COMMON_NAME"].values
        self.unique_cn = np.unique(common_names)
        
    def filter(self, event, selection):
        # filter all cherry blossom trees
        cherry_blossom = self.vancouver_data_cn.loc[selection.get(), :]

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

