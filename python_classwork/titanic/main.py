import pandas as pd
import numpy as np

df = pd.read_csv("titanic.csv", delimiter = ",")

"""
print(f"Size of data base is {len(df)}")

print("First five passengers:")
print(df.head(5))
print("Last five passengers:")
print(df.tail(5))
print(df.info())
print(df.describe())
"""

print(df["Age"].head(5), end="\n------\n")

print(df[["Age", "Sex"]].head(5), end="\n------\n")
df["Realtives"] = df["SibSp"] + df["Parch"] 
print(len(df[~df["Realtives"].isin([0])]), end="\n------\n")
print(len(df[df["Embarked"].isin(["S"])]), end="\n------\n")
surv = len(df[df["Survived"].isin([1])])
not_surv = len(df[df["Survived"].isin([0])])
print(f"Survived: {surv}", end="\n------\n")
print(f"Not survived: {not_surv}", end="\n------\n")

dct = {1 : "Elite", 2 : "Middle", 3 : "Prol"}

df = df.replace({"Pclass" : dct})

df["Fare_bin"] = "Expensive"
df.loc[(df.Fare < 20), "Fare_bin"] = "Cheap"

df = df.dropna()
df = df.reset_index()

print(df)

