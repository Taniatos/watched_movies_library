"""
The Main file manages a Watched Movies Library using a CSV file. 

It allows a user to add, edit, delete, and view movies, filter movies by 
genre and calculate the average rating of movies in the library.
"""

from file_operations import create_initial_csv, read_movies_from_file, \
    write_movies_to_file
from movie_operations import add_movie, edit_movie, delete_movie, \
    display_movies, display_movies_by_genre, display_menu, \
    calculate_average_rating
from test_movie import run_tests

def main():
    """
    The main function that drives the Movies Library program.
    """
    input_file = "movies.csv"  
    create_initial_csv(input_file)  # Ensures CSV file exists
    movies = read_movies_from_file(input_file)  # Loads movies from file

    while True:  # Iteration type: while loop
        display_menu()  # Shows the main menu
        choice = input("Enter your choice: ") # Asks the user to make a choice

        if choice == '1':
            add_movie(movies, input_file)  # Adds a new movie
        elif choice == '2':
            edit_movie(movies, input_file)  # Edits an existing movie
        elif choice == '3':
            delete_movie(movies, input_file)  # Deletes a movie
        elif choice == '4':
            display_movies(movies)  # Displays all movies
        elif choice == '5':
            display_movies_by_genre(movies)  # Displays movies by genre
        elif choice == '6':
            avg_rating = calculate_average_rating(movies)  # Calculates avg rat
            print(f"\nAverage rating: {avg_rating:.2f}\n" + "_" * 36)
        elif choice == '7':
            write_movies_to_file(movies, input_file)  # Saves movies to file
            print("\nFarewell! See you next time in your movie library!")
            break  # Exits the while loop and program
        else:
            # If the choice is invalid
            print("\nInvalid choice. Please select a valid option.\n" 
                  + "_" * 36)

if __name__ == "__main__":
    run_tests()  # Runs unit tests
    main()  # Starts the main function to launch the program
