"""
Created on Mon Mar 10 10:19:37 2025

@author: ryanc
"""

import matplotlib.pyplot as plt
import textwrap
import pandas as pd
#import numpy as np
#import matplotlib.ticker as ticker
import matplotlib.patches as mpatches

shop_density_data = pd.read_csv(r"C:\Users\ryanc\OneDrive\Documents\Work Stuff\Production Trends\Capita per shop data.csv")

plt.figure(figsize=(10,5.6))
plt.hlines(y=shop_density_data['State'], xmin=2000, xmax=shop_density_data['Capita per Coffee Shop'], 
           color='darksalmon', linewidth=4)
plt.plot(shop_density_data['Capita per Coffee Shop'], shop_density_data['State'], "o", color='saddlebrown', markersize=12)

plt.title("People per Coffee Shop", fontsize=24)
plt.grid(True, axis='x', color='dimgray', linestyle='--', linewidth=0.5, 
         alpha=0.75)

caption= textwrap.dedent("""\
                         Among our top ten coffee drinking states,
                         Maine has the highest coffee shop density
                         and Iowa has the lowest. Kansas, Missouri,
                         Ohio, North Carolina, Michigan, Delaware,
                         and Virginia compose a nice median group.
                         """)

citation = textwrap.dedent("""\
                           (Data from: IBISWorld, Coventry Direct)
                           """)
                           
plt.figtext(0.55, 0.68, caption, wrap= True, horizontalalignment="left", fontsize=11)
plt.figtext(0.73,0.01,citation,horizontalalignment='left',fontsize=6)