"""
Handles movie-related operations and functions in the Movies Library.
"""

from movie import Movie  
from file_operations import write_movies_to_file

def generate_movie_id(movies):
    """
    Generates a new unique movie ID based on the current maximum ID.
    """
    max_id = max((int(mid) for mid in movies.keys()), default=0)
    return str(max_id + 1)

def calculate_average_rating(movies):
    """
    Calculates and returns the average rating of the movies.
    """
    total_rating = 0
    rated_movies = 0
    for movie in movies.values():  # Iteration: for loop
        if movie.rating is not None:  # Only considers movies with ratings
            total_rating += movie.rating  # Adds rating to total
            rated_movies += 1  # Increments count of rated movies
    # Returns the average rating, or 0 if no rated movies are present
    return round(total_rating / rated_movies, 2) if rated_movies > 0 else 0

def display_menu():
    """
    Displays the main menu for the Movies Library.
    """
    print("\nMovies Library Menu:")
    print("1. Add a movie")
    print("2. Edit a movie")
    print("3. Delete a movie")
    print("4. Display all movies")
    print("5. Find movies by genre")
    print("6. Show average rating")
    print("7. Exit the library")
    print("_" * 36)

def add_movie(movies, file_path):
    """
    Handles the process of adding a new movie to the library.
    """
    movie_id = generate_movie_id(movies)
    title = None

    while not title:  # Iteration: while loop
        title = input("Enter movie title (or 'm' to return to menu): ")
        if title.lower() == 'm':
            return  # Returns to the main menu
        title = title.upper()  # Converts title to uppercase

        temp_movie = Movie(None, title, None, None)

        if temp_movie in movies.values():  # Checks for duplicate titles
            print(f"Looks like {title} already exists in your library.")
            return  # Returns to the main menu

    while True:
        try:  # Try block to validate the movie year
            year = input("Enter movie year (or 'm' to return to menu): ")
            if year.lower() == 'm':
                return  # Returns to the main menu
            year = int(year)  # Converts input to integer
            if year < 1888:
                print("\nIs it the first movie ever made? "
                      "Please enter a valid year.")
            elif year > 2024:
                print("\nWe are not yet in the future! "
                      "Please enter a valid year.")
            else:
                break  # Valid year entered, breaks the loop
        except ValueError:  # Handles invalid year input
            print("Please make sure to add a valid year.")

    genres = (  # Container type: Tuple
        "Action", "Adventure", "Comedy", "Drama", "Fantasy", "Horror", 
        "Mystery", "Romance", "Sci-Fi", "Thriller", "Animation", 
        "Biography", "Crime", "Documentary", "Family"
    )
    print(f"\nWhat is the genre of {title}?")
    
    for i in range(5):
        print(f"{i+1:2}. {genres[i]:<18} {i+6:2}. {genres[i+5]:<18} "
              f"{i+11:2}. {genres[i+10]:<18}")

    print("\nm. Return to menu")
    print("_" * 36)

    while True:
        genre_choice = input("\nSelect a genre by number (or 'm' to return): ")
        if genre_choice.lower() == 'm':
            return  # Returns to the main menu
        try:
            genre_choice = int(genre_choice)  # Converts input to integer
            if 1 <= genre_choice <= len(genres):
                genre = genres[genre_choice - 1]  # Selects genre
                break  # Valid genre selected, breaks the loop
            else:
                print(f"Invalid choice. Please select a number between 1 and "
                      f"{len(genres)}.")
        except ValueError:  # Handles invalid genre input
            print("Invalid input. Please enter a valid number or 'm' to return.")

    while True:
        try:  # Try block to validate the movie rating
            rating = round(float(input(f"\nHow would you rate {title} from "
                                       "0 to 10? ")), 2)
            if 0 <= rating <= 10:
                break  # Valid rating entered, breaks the loop
            else:
                print("Rating must be between 0 and 10.")
        except ValueError:  # Handles invalid rating input
            print("Invalid input. Please enter a number between 0 and 10.")

    movie = Movie(movie_id, title, year, genre, rating)
    movies[movie_id] = movie  # Adds the new movie to the dictionary
    write_movies_to_file(movies, file_path)  # Saves changes to the file
    print(f"\nMovie '{title}' added successfully.\n" + "_" * 36)

def edit_movie(movies, file_path):
    """
    Allows the user to edit existing movie's details.
    """
    print("\nMovies in your library:")
    sorted_movies = sorted(movies.values(), key=lambda movie: movie.title)
    for i, movie in enumerate(sorted_movies, 1):  # Iteration: for loop
        print(f"{i}. {movie}")
    print("\nm. Return to menu")
    print("_" * 36)

    while True:
        try:  # Try block to handle selection of a movie to edit
            movie_choice = input("\nSelect the movie to edit by number"
                                 "(or 'm' to return): ")
            if movie_choice.lower() == 'm':
                return  # Returns to the main menu
            movie_choice = int(movie_choice)  # Converts input to integer
            assert 0 < movie_choice <= len(sorted_movies), "Invalid choice."
            selected_movie = sorted_movies[movie_choice - 1]  # Selects movie
            break  # Valid selection, breaks the loop
        except (ValueError, AssertionError):  # Handles invalid selection
            print("Something went wrong. Please choose a valid number.")

    print("\nWhat would you like to edit?")
    print("1. Name")
    print("2. Year")
    print("3. Genre")
    print("4. Rating")
    print("5. All of the above")
    print("\nm. Return to menu")
    print("_" * 36)

    while True:
        choice = input("Enter your choice: ")
        if choice in {'m', '1', '2', '3', '4', '5'}:
            if choice.lower() == 'm':
                return  # Returns to the main menu
            break  # Valid choice, breaks the loop
        else:
            print("Invalid choice. Please select a valid option.")

    if choice == '1' or choice == '5':
        # Edits the movie title
        new_name = input(f"\nWhat is the correct name for "
                         f"'{selected_movie.title}'? ").upper()
        selected_movie.title = new_name
        print(f"\nName updated to '{new_name}'\n" + "_" * 36)
    if choice == '2' or choice == '5':
        while True:
            try:  # Try block to validate the new year
                new_year = input(f"\nWhat is the correct year for "
                                 f"'{selected_movie.title}'? ")
                if new_year.lower() == 'm':
                    return  # Returns to the main menu
                new_year = int(new_year)  # Converts input to integer
                if new_year < 1888:
                    print("\nIs it the first movie ever made? "
                          "Please enter a valid year.")
                elif new_year > 2024:
                    print("We are not yet in the future! "
                          "Please enter a valid year.")
                else:
                    break  # Valid year, breaks the loop
            except ValueError:  # Handles invalid year input
                print("Please make sure to add a valid year.")
        selected_movie.year = new_year
        print(f"\nYear updated to '{new_year}'\n" + "_" * 36)
    if choice == '3' or choice == '5':
        genres = (  # Container type: Tuple
            "Action", "Adventure", "Comedy", "Drama", "Fantasy", 
            "Horror", "Mystery", "Romance", "Sci-Fi", "Thriller", 
            "Animation", "Biography", "Crime", "Documentary", "Family"
        )
        print(f"\nWhat is the correct genre for '{selected_movie.title}'?")
        for i in range(5):  # Iteration: for loop
            print(f"{i+1}. {genres[i]:<12} {i+6}. {genres[i+5]:<12} "
                  f"{i+11}. {genres[i+10]:<12}")
        print("\nm. Return to menu")
        print("_" * 36)
        
        while True:
            try:  # Try block to validate the genre selection
                genre_choice = input("\nSelect a genre by number (or 'm' to "
                                     "return): ")
                if genre_choice.lower() == 'm':
                    return  # Returns to the main menu
                genre_choice = int(genre_choice)  # Converts input to integer
                if 1 <= genre_choice <= len(genres):
                    # Sets genre:
                    selected_movie.genre = genres[genre_choice - 1]  
                    break  # Valid genre selected, breaks the loop
                else:
                    print(f"Invalid choice. Please select a number between "
                          f"1 and {len(genres)}.")
            except ValueError:  # Handles invalid genre input
                print("Invalid input. Please enter a number.")
        print(f"\nGenre updated to '{selected_movie.genre}'\n" + "_" * 36)
    if choice == '4' or choice == '5':
        while True:
            try:  # Try block to validate the new rating
                new_rating = round(float(input(f"\nWhat is the correct rating "
                                               f"for '{selected_movie.title}'?"
                                               " (0-10): ")), 2)
                if 0 <= new_rating <= 10:
                    selected_movie.add_rating(new_rating)  # Sets rating
                    break  # Valid rating, breaks the loop
                else:
                    print("Rating must be between 0 and 10.")
            except ValueError:  # Handles invalid rating input
                print("Invalid input. Please enter a number between 0 and 10.")
        print(f"\nRating updated to '{new_rating}'\n" + "_" * 36)
    
    write_movies_to_file(movies, file_path)  # Saves changes to the file

def delete_movie(movies, file_path):
    """
    Allows the user to delete a movie from the library.
    """
    print("\nMovies in your library:")
    sorted_movies = sorted(movies.values(), key=lambda movie: movie.title)
    for i, movie in enumerate(sorted_movies, 1):  # Iteration: for loop
        print(f"{i}. {movie}")
    print("\nm. Return to menu")
    print("_" * 36)

    while True:
        try:  # Try block to handle user selection of a movie to delete
            movie_choice = input("\nSelect the movie to delete by number (or "
                                 "'m' to return): ")
            if movie_choice.lower() == 'm':
                return  # Returns to the main menu
            movie_choice = int(movie_choice)  # Converts input to integer
            assert 0 < movie_choice <= len(sorted_movies), "Invalid choice."
            selected_movie = sorted_movies[movie_choice - 1]  # Selects movie
            del movies[selected_movie.get_id()]  # Deletes the movie
            print(f"\nMovie '{selected_movie.title}' deleted successfully.\n" 
                  + "_" * 36)
            break  # Valid selection, breaks the loop
        except (ValueError, AssertionError):  # Handles invalid selection
            print("Something went wrong. Please choose a valid number.")
    
    write_movies_to_file(movies, file_path)  # Saves changes to the file

def display_movies(movies):
    """
    Displays all movies in the library.
    """
    if not movies:  # Conditional if-statement
        print("\nNo movies in the library.\n" + "_" * 36)
        return
    
    sorted_movie_list = sorted(movies.values(), key=lambda movie: movie.title)
    print("\nMovies in your library:")
    for i, movie in enumerate(sorted_movie_list, 1):  # Iteration: for loop
        print(f"{i}. {movie}")
    print("_" * 36)

def display_movies_by_genre(movies):
    """
    Displays movies filtered by genre.
    """
    if not movies:  # Conditional if-statement
        print("\nNo movies in the library.\n" + "_" * 36)
        return
    
    genre_set = {movie.genre for movie in movies.values()}  # Container: Set
    print("\nGenres available:")
    sorted_genres = sorted(genre_set)  # Sorts genres alphabetically
    for i, genre in enumerate(sorted_genres, 1):  # Iteration: for loop
        print(f"{i}. {genre}")
    print("\nm. Return to menu")
    print("_" * 36)
    
    while True:
        try:  # Try block to handle user selection of genre
            genre_choice = input("\nEnter genre number to filter by (or 'm' "
                                 "to return): ")
            if genre_choice.lower() == 'm':
                return  # Returns to the main menu
            genre_choice = int(genre_choice)  # Converts input to integer
            assert 0 < genre_choice <= len(sorted_genres), "Invalid choice."
            selected_genre = sorted_genres[genre_choice - 1]  # Selects genre
            break  # Valid selection, breaks the loop
        except (ValueError, AssertionError):  # Handles invalid selection
            print("Something went wrong. Please choose a valid number.")

    filtered_movies = [  # Container: List
        movie for movie in movies.values() if movie.genre == selected_genre
    ]
    if not filtered_movies:  # Conditional if-statement
        print(f"\nNo movies found in the genre: {selected_genre}\n" + "_" * 36)
    else:
        print(f"\nMovies in the genre '{selected_genre}':")
        sorted_filtered_movies = sorted(filtered_movies, 
                                        key=lambda movie: movie.title)
        # Iteration: for loop:
        for i, movie in enumerate(sorted_filtered_movies, 1):  
            print(f"{i}. {movie}")
        print("_" * 36)
