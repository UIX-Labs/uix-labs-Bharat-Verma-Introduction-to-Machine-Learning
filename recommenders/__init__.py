print('Hello, world!')
import pandas as pd
import os

#print(os.getcwd())

default_poster_url = "https://gurukul-be.s3.ap-south-1.amazonaws.com/0c3df9f4dc56471d88bb88255bb79548.jpg"

####################################################################################################################################

'''
Complete the code below

Things to do: load csv in dataframes

data_ratings => file path: 'data_files/ratings.csv'
data_movies => file path: 'data_files/movies.csv'
data_posters => file path: 'data_files/movie_poster.csv'

'''
data_ratings_path = 'data_files/ratings.csv'
data_movies_path = 'data_files/movies.csv'
data_posters_path = 'data_files/movie_poster.csv'

data_ratings = pd.read_csv(data_ratings_path)
data_movies = pd.read_csv(data_movies_path)
data_posters = pd.read_csv(data_posters_path)

'''
Uncomment the below line after you complete the code above.
'''
# data_movies = pd.merge(data_movies, data_posters, how="left", on="movieId")

#####################################################################################################################################
