

from data import load, load_movielens

import numpy as np

# load the biparte graph: np matrix 
user_movie_matrix = load()





def greedy():


    """

       This uses greedy approach for the recommendation
       It traverses the graph based on the greedy approach : pick highest rating while traversing from node to node
    """



    for row in user_movie_matrix:
    # compute for each user

        row = list(row) 
        maxrating = max(row)
        print user_movie_matrix[user_movie_matrix[row] == maxrating]







def bfs_paths(graph, start, goal):
    print "hi 2"
    flag = "product"
    queue = [(start, [start])]
    nonzero_indices = []
    while queue:
       (vertex, path) = queue.pop(0)
       if flag == "product":
           # the children nodes are the vertical of biparte matrix(nonzero)
           column = graph[:, [vertex]]
           nonzero_indices =  column.nonzero()
           nonzero_indices =  nonzero_indices[0]
           print "thisisinside" 
           for child_index in nonzero_indices:
               row = graph[child_index]
               nonzero_row_indices = row.nonzero()[0]

               for row_index in nonzero_row_indices:
                   if goal == row_index:
                       path = path + [child_index]
                       print path 
                   else:
                       queue.append((row_index, path + [row_index]))

                    

      


          
def graph_search(biparte_matrix):

    """
       the first row of the biparte matrix is : targetUser

       the second to last row is the closest neighbors 

       Now using graph search we have to find recommend a movie

       Since its a biparte graph:
           1. First move from customer to movie
           2. move from movie to customer


    """



    # the user who is being recommeneded
    target_vector = biparte_matrix[0]
    
    # get indices of all /some of the indices of the watched movies of the target user
    
    #bfs_roots = [i for i, e in enumerate(target_vector) if e != 0]

    bfs_all_roots = np.argpartition(target_vector, -10 )[-10:]
    bfs_roots = []

    for root in bfs_all_roots:
        if target_vector[root] != 0 :
            bfs_roots.append(root)

  
    for item_index in range(biparte_matrix.shape[0]):
        
        if target_vector[item_index] == 0:
            
            for root in bfs_roots:
                bfs_paths(biparte_matrix,  root, item_index )

def user_base_collabertive_filtering(): 

    
    # find euclidian distance of first two  users w.r.t all users
    # note: distance betwee two same vecotrs is zero

    for user in range(2):
        distances = []
        for anotheruser in range(user_movie_matrix.shape[0]):
            
            distance = np.linalg.norm(user_movie_matrix[user] - user_movie_matrix[anotheruser] )
            distances.append(distance) 

            
        # get the similar users 
        # indices of the similar users: closest 20
        # non zero too
        closest_all_indices=np.argpartition(distances, -20)[-20:]
        closest_indices = []
        for index in closest_all_indices:
            if distances[index] != 0:
                closest_indices.append(index)
        
        
        
         
        # consider the first five closest neighbors for the recommendation

        closest_indices.insert(0, user) 
        biparte_matrix = user_movie_matrix[closest_indices[0:4]] 
        # now execute the graph search for recommendation
        
        graph_search(biparte_matrix)
        print biparte_matrix
        


def get_movie_avg_rating(id, ratings):
    """
    return avg rating of the movie

    """

   
   #df = ratings.movieId == id

    rating =  0
    for index, row in ratings.iterrows():
        if row["movieId"] == id:
            rating = rating + row["rating"]    
    return rating

def content_based_filtering():
    """
       For content based filtering we wont directly use the biparte graph. We will be directly querying the file that is loaded
       using the pandas dataframe.

       The idea behind content based filtering is : when a user likes certain movies, using the meta informaton of the movies that the user watched we 
       will suggest similar movies which may have the same properties.


       meta-properties: genre
       user-given-properties: rating
       Algorithm:
           choose  all the movies that the user watched and arrange in descending order of ratings
           obtain genre of all the movies that user watched
           
           sum all the ratings for each genre 
           Now pick the top three generes and suggest based on that 


    """
    
    

    movies, ratings = load_movielens()


    # considerng customer 1
    target_user =  1
    
    movie_ids = []
    # list of movies watched by user
    for index, row in ratings.iterrows():
        if row["userId"] == 1 :
            movie_ids.append(row["movieId"])
    
    

    genre_dict = {}
    genre_count_dict = {}
    genre_ratio = {}
    for id in movie_ids:
        df = movies[movies.movieId == id]
        genres = []
        for index, row in df.iterrows():
             genres = row["genres"]
             genres = genres.lower()
             genres = genres.split('|')
        
        rating = get_movie_avg_rating(id, ratings)

        for genre in genres:
            if genre in genre_dict.keys():
                genre_dict[genre] = genre_dict[genre] + rating
                genre_count_dict = genre_count_dict + 1
            else:
                genre_dict[genre] = rating 
                genre_count_dict[genre] = rating
   
    for key in genre_dict.keys():
        ratio  = genre_dict[key] / float(genre_count_dict[key])
        genre_dict[key] = ratio
 
    import operator
    fav_genre = max(genre_dict.iteritems(), key=operator.itemgetter(1))[0]
     
     # get the best movies from that genre:

     # get all the movies that belong to the genre:
     
    genres_ids = []
    fav_movie_id = 0
    for index, row in movies:
        genres = row['genres']
        genres = genres.lower()
        genres = genres.split('|')
        if fav_genre in genres:
            movie_rating = get_movie_avg_rating(row["movieId"], ratings )
            if movie_rating > rating:
               fav_movie_id = row["id"] 


    print "content based recommended movie is:"
    print movies[movies.movieId == fav_movie_id]

         
         


#user_base_collabertive_filtering()

content_based_filtering()
