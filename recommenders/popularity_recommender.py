print('Hello, world!')
from recommenders import data_movies, data_ratings, default_poster_url
import pandas as pd

def recommend_popular_movies():
    ######################################################################################################
    # Merge movie data and rating data based on 'movieId'
    movie_ratings = pd.merge(data_movies, data_ratings, on='movieId')

    # Calculate average ratings for each movie
    movie_ratings = movie_ratings.groupby('title')['rating'].mean().reset_index()

    # Sorting movies based on mean ratings in descending order
    movie_ratings = movie_ratings.sort_values(by='rating', ascending=False)

    # Select the top 20 movies
    top_movies = movie_ratings.head(20)

    # Convert the resulting DataFrame to a dictionary
    movie_ratings_dict = top_movies.set_index('title')['rating'].to_dict()
    #######################################################################################################

    response = []

    for movie, rating in movie_ratings_dict.items():
        movie_record = data_movies[data_movies.title == movie].iloc[0]
        movie_poster = None  # You need to fetch the movie poster URL, not provided in the code
        response.append({
            "movieId": int(movie_record.movieId),
            "title": str(movie),
            "image": movie_poster if movie_poster and movie_poster != "nan" else default_poster_url,
            "genres": str(movie_record.genres).split("|"),
            "average_rating": rating
        })

    return {"status": True, "data": {"message": "Here are some of the popular recommendations.", "results": response}}
