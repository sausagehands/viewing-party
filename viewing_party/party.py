# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    pass

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
    # watched = [
    #     {
    #         "title": "title", 
    #         "rating": 0,
    #         "genre": "horror"
    #         }
    #     ]
    # user_data = {
    #     "watched": [{dict1...key1:v1, k2:v2}] 
    # }


def get_watched_avg_rating(user_data):
    watched = user_data["watched"]
    total_ratings = 0.0
    
    if not watched:
        return 0.0
    for movie in watched:
        total_ratings += movie["rating"]
    avg_rating = total_ratings/len(watched)
    return avg_rating
        
def get_most_watched_genre(user_data):
    
    watched = user_data["watched"]
    most_watched_genre = None
    highest_count = 0
    genre_count = {}
    
    
    if not watched:
        return None
    
    for movie in watched:
        genre = movie['genre']
        genre_count[genre] = genre_count.get(genre,0) + 1
        
    for genre, count in genre_count.items():
        if count > highest_count:
            highest_count = count
            most_watched_genre = genre
 
    return most_watched_genre
    
    

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------