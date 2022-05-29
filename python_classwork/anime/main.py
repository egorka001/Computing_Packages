import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

db = pd.read_csv("anime.csv")
db = db.dropna()

print(db.info())
print(db.head(10))

db.Genre = db.Genre.str.lower()
db.Genre = db.Genre.str.replace(' ', '_')
db.Genre = db.Genre.str.replace(',', ' ')

g_set = set()
for i in db.Genre.str.split():
    for gen in i:
        g_set.add(gen)

g_dct = dict()
r_dct = dict()
for i in g_set:
    g_dct[i] = 0 
    r_dct[i] = 0

for i in db.Genre.str.split():
    for gen in i:
        g_dct[gen] += 1
print(g_dct)

for i in range(0,989):
    for gen in db.iloc[i].Genre.split():
        r_dct[gen] += db.iloc[i].Rating

for key in r_dct.keys():
    r_dct[key] = r_dct[key] / g_dct[key]
print(r_dct)
        
plt.rcParams["font.size"] = '7'
fig, ax = plt.subplots(2, 1)
fig = plt.figure("anime")

ax[0].bar(g_dct.keys(), g_dct.values())
ax[0].set_title("Genre")

ax[1].bar(r_dct.keys(), r_dct.values())
ax[1].set_title("Rating")

plt.show()
