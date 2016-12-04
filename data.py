
import pandas as  pd


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


def biparteMatrix(movies_frame):

    """

       convert the movies data frame into userid-movies biparte adjacency graph matrix

    """






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
    biparteMatrix(movies)
