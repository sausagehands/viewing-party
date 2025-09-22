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


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

