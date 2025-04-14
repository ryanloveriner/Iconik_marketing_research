"""
Created on Mon Mar 10 13:30:32 2025

@author: ryanc
"""
#This code is adapted from code produced by ChatGPT o3-mini-high

import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd
import textwrap

# Load US states shapefile (GeoJSON or Shapefile)
# You can download a US states GeoJSON from a trusted source like https://eric.clst.org/tech/usgeojson/
us_map = gpd.read_file(r"C:\Users\ryanc\OneDrive\Documents\Work Stuff\Production Trends\usmap_for_infographics.json")
unwanted = ["Puerto Rico", "District of Columbia", "Hawaii", "Alaska"]
us_map = us_map[~us_map['NAME'].isin(unwanted)]


# Load your key data; here we simulate with sample data
# Assume 'state' column matches the state names/abbreviations in the shapefile and 'value' is the metric
data = pd.DataFrame({
    'state': ['Missouri', 'Michigan', 'Nebraska', 'Virginia', 'Massachusetts', 'Oregon', 'Kansas', 'North Carolina','Louisiana','South Carolina','Wisconsin','Iowa'],
    'value': ["Milk Drinks", "Milk Drinks", "Milk Drinks", "Specialty Coffee", "General", "Specialty Coffee", "Specialty Coffee", "Specialty Coffee", "Specialty Coffee", "Specialty Coffee", "General", "General"]
                    })

# Merge the key data with the geographic data
merged = us_map.merge(data, how='left', left_on='NAME', right_on='state')

# Plotting the map
fig, ax = plt.subplots(1, 1, figsize=(10, 5.6))
merged.plot(column='value', ax=ax, legend=True,
            edgecolor='black',  # Set state borders to black
            linewidth=0.5,  # Set line width of borders
            missing_kwds={"color": "lightgrey", "edgecolor": "black",
                          "hatch": "///", "label": "Not a target state"})
ax.set_title('Preferred Sales Categories for Target States', fontsize=22)
ax.axis('off')  # Remove axes for a cleaner look

# Modify legend size
legend = ax.get_legend()
for text in legend.get_texts():
    text.set_fontsize(9)

citation = textwrap.dedent("""\
                           (Powered by GEOjson and ChatGPT o3-mini-high)
                           """)
plt.figtext(0.7,0.1,citation,horizontalalignment='left',fontsize=6)