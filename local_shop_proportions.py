"""
Created on Mon Mar 10 10:19:37 2025

@author: ryanc
"""

import matplotlib.pyplot as plt
import pandas as pd
#import numpy as np
#import matplotlib.ticker as ticker
import matplotlib.patches as mpatches
import textwrap

local_owner_proportions_data = pd.read_csv(r*****INSERT FILE AS PATH HERE!!!*****)

color1 = 'dimgray'
color2 = 'slateblue'
colors = [color1 if cat in ['Kansas','Louisiana','South Carolina','Ohio']
          else color2 for cat in local_owner_proportions_data['State']]

plt.figure(figsize=(10, 5.6))                                                        
chart = local_owner_proportions_data.plot(kind='bar', x='State', 
                                          y='% Local/Single Owner Shops', 
                                          color=colors)
plt.title("Proportion of Local/Single-Owner Shops", fontsize=20)
plt.ylabel("% Locally Owned",fontsize=12)
plt.xticks(rotation=45)

patch1 = mpatches.Patch(color=color2, label='Top ten coffee drinking state')
chart.legend(handles=[patch1], loc='upper left', bbox_to_anchor=(1, 1))

caption = textwrap.dedent("""\
                          Among the states with the
                          highest proportion of locally
                          owned coffee shops, Missouri,
                          North Carolina, Michigan,
                          Virginia, and Delaware are
                          among our top ten subset.
                          """)

citation = textwrap.dedent("""\
                           (Data from: Rentech Digital, Coventry Direct)
                           """)

plt.figtext(0.91,0.3,caption,fontsize=11)
plt.figtext(0.99,0.01,citation,horizontalalignment='left',fontsize=6)
