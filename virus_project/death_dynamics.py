import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

from datetime import date
import matplotlib.dates as mdates

#import & work with base structure
death_db = pd.read_csv('data/time_series_covid19_deaths_global.csv')
death_db = death_db.drop(columns = ['Province/State', 'Lat', 'Long'])
death_db = death_db.dropna()

#list of dates
date_lst = death_db.columns.tolist()
date_lst = date_lst[1:]
print(f"first day: {date_lst[0]}\nlast_day: {date_lst[-1]}")
days = np.arange(1, len(date_lst) + 1, 1)

date1 = date(2020, 1, 22)
date2 = date(2022, 5, 28)
datelist = pd.date_range(date1, date2).tolist()

#list of deaths
country = 'Russia'
print(death_db)
death = death_db.loc[death_db['Country/Region']==country].values.tolist()[0]
death = death[1:]

count = 0
death_reg = list()
death_reg.append(death[count])
while count != len(death) - 1:
    death_reg.append(death[count + 1] - death[count])
    count += 1

#plots
fig = plt.figure(f"virus in {country}")

ax = fig.add_subplot(211)
ax.plot(datelist, death)
ax.set(title='Total Deaths',
       xlabel='Date',
       ylabel='Deaths')
ax.plot(date1, death[0], '-bo', date2, death[-1], 'bo')
ax.text(datelist[0], death[0] + 100, f"{date1}")
ax.text(datelist[-50], death[-1] - 300, f"{date2}")
ax.text(datelist[-50], 100, f"sum: {max(death)}")
ax.grid()

ax = fig.add_subplot(212)
ax.plot(datelist, death_reg)
ax.set(title='Deaths per Day',
       xlabel='Date',
       ylabel='Deaths')
ax.grid()
ax.text(datelist[-50], 10, f"max: {max(death_reg)}")

plt.show()
