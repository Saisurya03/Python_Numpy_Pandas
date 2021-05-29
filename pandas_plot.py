import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

weather = pd.read_csv('https://raw.githubusercontent.com/alanjones2/dataviz/master/london2018.csv')
weather.plot.bar(y='Tmax', x='Month')
weather.plot.barh(y='Tmax', x='Month')
weather.plot.bar(y=['Tmax', 'Tmin'], x='Month')
weather.plot.bar(y=['Tmax', 'Tmin', 'Rain', 'Sun'], x='Month', subplots=True, layout=(2,2))
a = weather.plot.scatter(x='Tmax', y='Month', color='r')
b = weather.plot.scatter(x='Tmin', y='Month', color='g', ax=a)
plt.show()
