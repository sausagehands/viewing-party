# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):

    #Checks if any of the dictionary keys are None
    if title == None or genre == None or rating == None:
        return None

    movie = {
        "title": title,
        "genre": genre,
        "rating": rating
    }

    return movie

def add_to_watched(data_dict, movie):
    #Adds the movie to the list value of the key watched

    data_dict["watched"].append(movie)

    return data_dict

def add_to_watchlist(data_dict, movie):

    data_dict["watchlist"].append(movie)

    return data_dict

def watch_movie(data_dict, movie_title):
    # Locate list index of movie in dictionary watchlist
    #index = 0
    for movie in data_dict["watchlist"]:
        if movie_title in movie["title"]:
            data_dict["watched"].append(movie)
            data_dict["watchlist"].remove(movie)
    return data_dict

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

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
#Determine which movies the user has watched, but none of their friends have watched.
#Determine which movies at least one of the user's friends have watched, but the user has not watched.

def get_unique_watched(user_data):
    #user_data = {'watched': [{}], 'friends':[{watched:[{'title':}, {'title':}]}]}
    user_watched = user_data.get("watched")
    friends = user_data.get("friends")
    
    #set comprehension to avoid duplicates-- if not it kept failing the test
    friends_watched = {movie["title"] for friend in friends for movie in friend.get("watched")}
    
    unique_movies = [movie for movie in user_watched if movie["title"] not in friends_watched]
    return unique_movies



def get_friends_unique_watched(user_data):
    user_watched = {movie["title"] for movie in user_data.get("watched")}
    friends = user_data.get("friends")

    friends_watched = []
    for friend in friends:
        for movie in friend.get("watched"):
            if movie["title"] not in user_watched and movie not in friends_watched:
                friends_watched.append(movie)

    return friends_watched
    

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    recommendations = []
    for friend in user_data['friends']:
        for movie in friend['watched']:
    #Loops through watched movies for each friend
            if movie in user_data['watched'] or movie in recommendations: #Checks if the movie is already watched
                continue
            elif movie['host'] in user_data['subscriptions']:
                recommendations.append(movie)
            else:
                continue
    return recommendations
# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
def get_new_rec_by_genre(user_data):
    most_watched_genre = get_most_watched_genre(user_data)
    friends_movies = get_friends_unique_watched(user_data)
    
    movie_recs = [movie for movie in friends_movies if movie['genre'] == most_watched_genre ]

    return movie_recs
    

def get_rec_from_favorites(user_data):
    favorite_movies = user_data.get("favorites")
    friends = user_data.get("friends")
    
    friends_watched = {movie['title'] for friend in friends for movie in friend.get("watched")}
    movie_recs = [movie for movie in favorite_movies if movie['title'] not in friends_watched]
    
    return movie_recs


    
    
    