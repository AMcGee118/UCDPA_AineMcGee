
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from bokeh.plotting import figure, output_file,show

netflix_tot=pd.read_csv("/Users/Aine/Desktop/netflixData.csv")
netflix_tot=netflix_tot.dropna()
netflix_tot=netflix_tot.reset_index(drop=True)

#print(netflix_tot.count())

netflix_show=netflix_tot[netflix_tot["Content Type"]== "TV Show"]
netflix_show=netflix_show.reset_index(drop=True)
#print(netflix_show.head())
#print(netflix_show.count())

netflix_movie=netflix_tot[netflix_tot["Content Type"]== "Movie"]
netflix_movie=netflix_movie.reset_index(drop=True)
#print(netflix_movie.head())
#print(netflix_movie.count())

plt.figure("Types of Content")
sns.set_style(style="whitegrid")
sns.countplot(x="Content Type", palette= "RdPu",data = netflix_tot).set(title="Content Types")

plt.figure("Score",figsize=(10,5))
netflix_tot["Imdb Score"].value_counts().plot(kind="bar", width=1, color="Red")
plt.xticks(fontsize=7)
plt.title('Imdb Score of Movies')
plt.xlabel ("Score")
plt.ylabel("Count")

for index, row in netflix_tot.head().iterrows():
   print(index,row)

def years_since_release(release):
    sum= 2022 - release
    print(sum)

years_since_release(1996)


countries=netflix_movie["Production Country"].value_counts()
print(countries)


movie_us=netflix_movie[netflix_movie["Production Country"]== "United States"]
movie_us=movie_us.dropna()
movie_us=movie_us.reset_index(drop=True)

plt.figure("US Ratings")
movie_us["Rating"].hist(alpha=0.7, facecolor="#2ab0ff", edgecolor="#00008B")
plt.title("US Movie Appropriate Age Rating")
plt.xlabel("Age Rating")


from bokeh.plotting import figure
from bokeh.io import output_file, show
fig= figure(x_axis_label="US Movie Duration",y_axis_label="US Movie Imdb Score")
fig.circle(x=movie_us["Duration"],y=movie_us["Imdb Score"])
output_file(filename= "Bokeh_Vis_Netflix.html")
show(fig)

years_released= {2021, 2020, 2019, 2018, 2017, 2016, 2015, 2014, 2013, 2012, 2011, 2010, 2009, 2008, 2007, 2006, 2005, 2004, 2003, 2002, 2001, 2000, 1999, 1998, 1997, 1996, 1995, 1994, 1993, 1992, 1991, 1990, 1989, 1988, 1987, 1986, 1985, 1984, 1983, 1982, 1981, 1980, 1979, 1978, 1977, 1976, 1975, 1974, 1973, 1972, 1971, 1966, 1958, 1956, 1945}

np.years_released=np.array(years_released)
years_released_sorted=np.sort(np.years_released, axis=None)
print("Netflix Content Release Year", years_released_sorted)


plt.show()


