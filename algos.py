

from data import load

import numpy as np

# load the biparte graph: np matrix 
user_movie_matrix = load()



print "hi"


def greedy():


    """

       This uses greedy approach for the recommendation
       It traverses the graph based on the greedy approach : pick highest rating while traversing from node to node
    """

    print "2"


    for row in user_movie_matrix:
    # compute for each user

        row = list(row) 
        maxrating = max(row)
        print user_movie_matrix[user_movie_matrix[row] == maxrating]








def user_base_collabertive_filtering(): 

    
    # find euclidian distance of first two  users w.r.t all users
    # note: distance betwee two same vecotrs is zero

    for user in range(2):
        distances = []
        for anotheruser in range(user_movie_matrix.shape[0]):
            
            distance = np.linalg.norm(user_movie_matrix[user] - user_movie_matrix[anotheruser] )
            distances.append(distance) 

            
        # get the similar users 
        # indices of the similar users:

        closest_indices=np.argpartition(distances, -4)[-4:]
        
        print closest_indices
    # now execute the graph search for recommendation
    



user_base_collabertive_filtering()
#greedy()
