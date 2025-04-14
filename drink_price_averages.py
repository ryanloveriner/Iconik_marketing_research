"""
Created on Thu Mar  6 16:22:05 2025

@author: ryanc
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib.ticker as ticker
import textwrap

ten_states_data = pd.read_csv("C:/Users/ryanc/OneDrive/Documents/Work Stuff/Production Trends/Top_ten_coffee_drinking_states.csv")

plt.figure(figsize=(10, 5.6))                                                        
ten_states_data.plot(kind='bar', x='State', y=['Brewed Coffee', 'Cold Brew',    #Bar chart of average beverage prices
                                               'Latte', 'Tea'])

plt.title("Average beverage prices in the top ten coffee drinking states", fontsize=16)      #Title, axis labels, grid lines
plt.ylabel("USD")
plt.grid(True, axis='y', color='black', linestyle='-', linewidth=0.5, 
         alpha=0.75)

plt.xticks(rotation=45)                                                         #Rotate x tick labels for legibility

plt.yticks(np.arange(0,6,0.5))                                                  #Insert minor ticks for clarity
ax = plt.gca()
ax.yaxis.set_major_locator(ticker.MultipleLocator(1.0))                         #AI assistance on this code chunk
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.5))

hline = plt.axhline(y=3.08, color='maroon', linestyle="--", linewidth=0.75,     #Horizontal lines marking national averages
                    label="Average Price of Brewed Coffee")
hline = plt.axhline(y=5.14, color='lightseagreen', linestyle="--", 
                    linewidth=0.75, label="Average Price of Cold Brew Coffee")
hline = plt.axhline(y=5.46, color='mediumorchid', linestyle="--", 
                    linewidth=0.75, label="Average Price of Lattes")
hline = plt.axhline(y=3.74, color='mediumblue', linestyle="--", 
                    linewidth=0.75, label="Average price of Tea")

plt.legend(loc="upper left", bbox_to_anchor=(1, 1))                             #Move legend to margin

caption1 = textwrap.dedent("""\
                           Massachusetts, Oregon, and Virginia
                           have average brewed coffee prices at
                           or above the national average.
                           """)

caption2 = textwrap.dedent("""\
                           Virginia, North Carolina, Michigan,
                           Missouri, and Nebraska have average
                           latte prices at or above the national
                           average.
                           """)

citation = textwrap.dedent("""\
                           (Data from: toast, Conventry Direct)
                           """)
plt.figtext(0.91,0.28,caption1,horizontalalignment='left',fontsize=11)
plt.figtext(0.91,0.1,caption2,horizontalalignment='left',fontsize=11)
plt.figtext(0.99,0.01,citation,horizontalalignment='left',fontsize=6)