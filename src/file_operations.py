"""
Handles file operations for the Movies Library.
"""

import os
from movie import Movie

# Container type 1: Dictionary
def create_initial_csv(file_path):
    """
    Creates a CSV file with headers if it does not exist. 
    If the file exists, it welcomes the user back.
    """
    if os.path.exists(file_path):  # Conditional if-statement
        # Notifies the user that the file exists, no need to create a new one
        print(f"Welcome back to your Watched Movies Library! The file "
              f"'{file_path}' is open and ready for inputs.")
    else:
        try:  # Try block to handle file creation
            with open(file_path, 'w') as file:
                # Writes CSV headers to the new file
                file.write("movie_id,title,year,genre,rating\n")
        except IOError as e:  # Handles any input/output errors
            # Outputs an error message if file creation fails
            print(f"An error occurred while creating {file_path}: {e}")
        else:  
            # Informs the user that a new file was successfully created
            print(f"Welcome to your Watched Movies Library! File '{file_path}'"
                  " was created successfully and is ready for your inputs!")


def read_movies_from_file(file_path):
    """
    Reads movies from the CSV file and returns them as a dictionary 
    with movie_id as the key.
    """
    movies = {}  # Container type: Dictionary
    try:  # Try block to handle file reading
        with open(file_path, 'r') as file:
            next(file)  # Skips header line
            for line in file:  # Iteration: for loop
                parts = line.strip().split(',') 
                if len(parts) == 4 or len(parts) == 5:
                    movie_id, title, year, genre = parts[:4]
                    rating = float(parts[4]) if len(parts) == 5 and \
                        parts[4] else None  # Handles optional rating
                    try:
                        int(movie_id)  # Validates movie_id as an integer
                    except ValueError:
                        continue  # Skips invalid movie_id
                    # Adds the movie to the dictionary
                    movies[movie_id] = Movie(movie_id, title.upper(), 
                                             int(year), genre, rating)
    except FileNotFoundError:  # Handles file not found error
        # Notifies the user that the file does not exist
        print(f"File {file_path} not found.")
    return movies  # Returns the dictionary of movies

def write_movies_to_file(movies, file_path):
    """
    Writes the current movies dictionary to the CSV file.
    """
    try:  # Try block to handle file writing
        with open(file_path, 'w') as file:
            # Writes CSV headers to the file
            file.write("movie_id,title,year,genre,rating\n")
            for movie_id, movie in movies.items():  # Iteration: for loop
                # Formats the rating if it exists, otherwise leaves blank
                rating_str = (
                    f"{format(movie.rating, '.2f')}" 
                    if movie.rating is not None else ''
                )
                # Uses movie.get_id()
                file.write(f"{movie.get_id()},{movie.title},{movie.year},"
                           f"{movie.genre},{rating_str}\n")
        # Notifies the user that changes have been saved
        print("Changes saved!")
    except IOError as e:  # Handles any input/output errors during file writing
        # Outputs an error message if writing to the file fails
        print(f"An error occurred while writing to {file_path}: {e}")
