
import pandas as  pd
import numpy as np

def load_movielens():

    """
         load the three csv files:
             1. movies.csv: movieId,title,genres
             2. ratings.csv: userId,movieId,rating,timestamp
             3. tags.csv: userId,movieId,tag,timestamp   ( This is not needed for now) 

    """
    #movies_csv  = np.genfromtxt('./data/movies.csv', delimeter=',')
    
    #ratings_csv = np.genfromtxt('./data/ratings.csv',delimeter=',')
       
    #tags_csv = np.genfromtxt('./data/tags.csv', delimeter=',')

    movies = pd.read_csv('./data/movies.csv', sep=',')

    ratings = pd.read_csv('./data/ratings.csv', sep=',')

    
 
    return movies, ratings


def biparteMatrix(movies_frame, ratings_frame):

    """

       convert the movies data frame into userid-movies biparte adjacency graph matrix

    """

   
    user_ids = list(ratings_frame.userId.unique()) 
    movie_ids = list(movies_frame.movieId.unique()) 

    numberOfUsers =  len(user_ids)

    numberOfMovies = len(movie_ids)
    
    
    
    # initialize a numpy matrix of of numberOfUsers * numberOfMovies

    user_movie_biparte = np.zeros((numberOfUsers, numberOfMovies))


    for name, group in ratings_frame.groupby(["userId", "movieId"]):

        #print name 
        #print group
        
        # name is a tuple (userId, movieId)
        
        userId, movieId = name

        user_index = user_ids.index(userId)
        movie_index = movie_ids.index(movieId)
        user_movie_biparte[user_index, movie_index] = group[["rating"]].values[0,0]

    return user_movie_biparte


def load():


    """ 
        convert the csv flies into required dataformats

        ratings_csv  : convert into user-moveID biparte sparse adjacency graph matrix

        tags_csv: not requried currently

        movies_csv: convert into clusters of data 
    """
    
    # load csv into dataframes
    movies, ratings  = load_movielens()

      
    #convet the ratings datafrom into user-movieId biparte adjacency matrix
    matrix = biparteMatrix(movies, ratings)

    return matrix


    
    



load()    
