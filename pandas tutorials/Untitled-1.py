# %%
import pandas as pd
import matplotlib.pyplot as plt

# %% [markdown]
# # (4) How To Create Plots in pandas?

# %% [markdown]
# ## How to create plots in pandas?

# %% [markdown]
# `index_col=0` defines the first (0th) column as index of the resulting DataFrame
# 
# `parse_dates=True` converts the dates in the column to Timestamp objects

# %%
air_quality = pd.read_csv(r"C:\Users\jovan.djokic\learning_pandas\pandas tutorials\data\air_quality_no2.csv", index_col=0, parse_dates=True)

# %%
air_quality.head()

# %%
air_quality.plot()

# %% [markdown]
# I think that `plt.show()` would trigger showing the plot, if this code weren't being written in a Jupyter notebook

# %%
plt.show()

# %%
air_quality["station_paris"].plot()

# %%
plt.show()

# %%
air_quality.plot.scatter(x="station_london", y="station_paris", alpha=0.5)

# %%
plt.show()

# %% [markdown]
# Listing possible plots:

# %%
[
    method_name
    for method_name in dir(air_quality.plot)
    if not method_name.startswith("_")
]

# %%
air_quality.plot.box()

# %%
plt.show()

# %%
axs = air_quality.plot.area(figsize=(12, 4), subplots=True)

# %%
plt.show()

# %%
fig, axs = plt.subplots(figsize=(12, 4)) #create empty figure & axes

# %%
air_quality.plot.area(ax=axs) #use pandas to put the area plot on the above figure/axes

# %%
axs.set_ylabel("NO$_2$ concentration") #customize the figure

# %%
fig.savefig(r"C:\Users\jovan.djokic\learning_pandas\pandas tutorials\output\no2_concentrations.png") #save the figure

# %%
plt.show() #display the plot


