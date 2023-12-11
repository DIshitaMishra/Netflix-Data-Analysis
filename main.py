'''
Project Name = Netflix Data Analysis
Created By = Ishita Mishra & Prakhar Tripati
Description = There is a dataset in the form of CSV format and, we have to perform some EDA (Exploratory data analysis)
by which we find some Valuable insights and also solving the problems related to this analysis.
'''
# Importing Packages

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Importing the Dataset
df = pd.read_csv("C:/Users/ishita mishra/Desktop/Netflix/Netflix Dataset.csv")
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)


# Data Processing
#=================

# print(df)

# Top 10 Values
# print(df.head(10))

# Bottom 10 Values
# print(df.tail(10))

# print(df.info())
#
# Stastical Analysis
# print(df.describe())
#Checking the column names

# print(df.columns)

# Fetching the year from Releasing Date
df["Releasing_Year"] = pd.DatetimeIndex(df["Release_Date"]).year
# print(df["Releasing_Year"])

# print(df.dtypes)

# Exploratory Data Analysis -- EDA

# print(df["Category"].value_counts())

# Top 5 Directors Published max Movies

# print(df["Director"].value_counts()[:5])

# Top 5 Cast who get max movies

# print(df["Cast"].value_counts()[:5])

# Top 5 Conturies with max shows

# print(df["Country"].value_counts()[0:5])

# Top 5 counties which have max movies

Movie_df = df[df["Category"] == "Movie"]
# print(Movie_df["Country"].value_counts()[0:5])

# Countries where the top director make movies

Director_df = Movie_df[Movie_df["Director"] == "Raúl Campos, Jan Suter"]
# print(Director_df["Country"].value_counts())

# Ratings For Top Director Raúl Campos, Jan Suter
# print(Director_df["Rating"].value_counts()[:5])

# Top 5 Movies on Netflix

# print(Movie_df["Title"].value_counts()[0:5])

# Top 5 Movies and Shows on Netflix

# print(df["Title"].value_counts()[0:5])

# Top 5 Releasing Year

# print(df["Releasing_Year"].value_counts().head())

Year_df = df[df["Releasing_Year"] == 2019]

# Top countries with max Netflix shows in 2019

# print(Year_df["Country"].value_counts()[:5])

# Top directors with max Netflix shows in 2019
# print(Year_df["Director"].value_counts()[:5])

# Top category with max Netflix shows in 2019
# print(Year_df["Category"].value_counts())

# print(Year_df.head())

# Count of Ratings
# print(df["Rating"].value_counts())

df["Releasing_month"] = pd.DatetimeIndex(df["Release_Date"]).month
df["Releasing_month"] = pd.to_datetime(df["Releasing_month"], format="%m").dt.month_name()
# print(df["Releasing_month"])

# print(df["Releasing_month"].value_counts())

# Top 5 types of shows on netflix
# print(df["Type"].value_counts()[:5])

Documentry_df = df[df["Type"] == "Documentaries"]

# Top 5 Directors who direct Documentaries

# print(Documentry_df["Director"].value_counts()[:5])

# Data Visualization
# plt.figure(figsize=(8,16))
# Category = ["Movie","TV Show"]
# Value = df["Category"].value_counts()
# plt.bar(Category,Value, color = "grey")
# plt.xlabel("Category")
# plt.ylabel("Count")
# plt.title("Category Count")
# plt.show()

# Top 5 Directors on Netflix Shows
# plt.figure(figsize=(10,7))
# plt.title("Top 5 Directors on Netflix Shows")
# Directors = df["Director"].value_counts()[:5]
# plt.pie(Directors,autopct="%.2f", labels=Directors.index)
# plt.show()

# Top 5 Cast on Netflix Shows
# plt.figure(figsize=(10,7))
# plt.title("Top 5 Cast on Netflix Shows")
# Cast = df["Cast"].value_counts()[:5]
# plt.pie(Cast,autopct="%.2f", labels=Cast.index)
# plt.show()

# Top 5 Countries with the Most Shows
# plt.figure(figsize=(10,7))
# top_countries = df["Country"].value_counts()[:5]
# sns.barplot(x=top_countries.index, y=top_countries.values)
# plt.title('Top 5 Countries with the Most Shows')
# plt.xlabel('Country')
# plt.ylabel('Number of Shows')
# plt.show()

# plt.figure(figsize=(10,7))
# plt.title("Top 5 Countries where maximum movies launched")
# top_countries = Movie_df["Country"].value_counts()[:5]
# sns.barplot(x=top_countries.index, y=top_countries.values, color="skyblue")
# plt.show()


#
# plt.figure(figsize=(10,7))
# plt.title("Top 5 Directors on Netflix Shows")
# Directors = df["Director"].value_counts()[:5]
# plt.pie(Directors,autopct="%.2f", labels=Directors.index)
# plt.show()

# Rating of Raul campos Movies on Netflix
#
# plt.figure(figsize=(10,7))
# plt.title("Rating of Raul campos Movies on Netflix")
# Rating = Director_df["Rating"].value_counts()[:5]
# sns.barplot(x = Rating.index, y= Rating.values , color="yellow")
# plt.show()

# Top 5 Movies & TV Shows on Netflix
plt.figure(figsize=(10,7))
plt.title("Top 5 Movies & TV Shows on Netflix")
Movie = df["Title"].value_counts()[:5]
plt.pie(Movie,autopct="%.2f", labels=Movie.index, colors = ["skyblue","orange","green","yellow","purple"])
plt.show()

# Top 5 Years That have most releases
# plt.figure(figsize=(10,7))
# plt.title("Top 5 Years That have most Releases")
# Year= df["Releasing_Year"].value_counts().head()
# sns.barplot(x = Year.index, y= Year.values , color="Red")
# plt.show()

# Top 5 month That have most releases
# plt.figure(figsize=(10,7))
# plt.title("Top 5 Month That have most Releases")
# Month= df["Releasing_month"].value_counts().head()
# sns.barplot(x = Month.index, y= Month.values , color="purple")
# plt.show()

# Count of Ratings
# plt.figure(figsize=(10,7))
# plt.title("Count of Ratings")
# rating= df["Rating"].value_counts().head()
# sns.barplot(x = rating.index, y= rating.values , color="lightgreen")
# plt.show()

# Count of type of shows on Netflix
# plt.figure(figsize=(10,7))
# plt.title("Count of type of shows on Netflix")
# type= df["Type"].value_counts().head()
# label = ["Documentry", "Stand Up", "Drama", "International Movies", "Independent Movies"]
# sns.barplot(x = label, y= type.values , color="seagreen")
# plt.show()








