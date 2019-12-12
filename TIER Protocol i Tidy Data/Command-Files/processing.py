import pandas as pd
import datetime
from os import listdir
from os.path import isfile, join
import glob
import re
import openpyxl

df = pd.read_csv("..\Original-Data\original-billboard.csv", encoding="mac_latin2")
id_vars = ["year","artist.inverted","track","time","genre","date.entered","date.peaked"]
df = pd.melt(frame=df,id_vars=id_vars, var_name="week", value_name="rank")
df["week"] = df['week'].str.extract('(\d+)', expand=False).astype(int)
df = df.dropna()
df["rank"] = df["rank"].astype(int)
df['date'] = pd.to_datetime(df['date.entered']) + pd.to_timedelta(df['week'], unit='w') - pd.DateOffset(weeks=1)
df = df[["year", "artist.inverted", "track", "time", "genre", "week","rank", "date"]]
df = df.sort_values(ascending=True, by=["year","artist.inverted","track","week","rank"])
billboard = df
print(billboard)