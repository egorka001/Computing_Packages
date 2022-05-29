import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

normal_s = np.random.normal(loc = 0.0, scale = 1.0, size = 10000)
random_s = np.random.random(size = 10000)
gamma_s = np.random.gamma(2, size = 10000)

df = pd.DataFrame({"normal" : normal_s,
                   "random" : random_s,
                   "gamma" : gamma_s})

fig = plt.figure("box plot's")
ax = fig.add_subplot(131)
ax.set_title("normal")
ax.boxplot(df["normal"])

ax = fig.add_subplot(132)
ax.set_title("random")
ax.boxplot(df["random"])

ax = fig.add_subplot(133)
ax.set_title("gamma")
ax.boxplot(df["gamma"])

plt.show()

