"""
This module introduces a Movie class that includes the information 
about a movie, particularly its title, year of release, genre, and rating. 
The class includes methods for validating the movie's year, formatting 
the rating, and generating a string representation of the movie.
"""

class Movie:
    """
    A class to represent a movie, containing details such as the title, 
    year of release, genre, and rating. 
    """
    
    def __init__(self, movie_id, title, year, genre, rating=None):
        """
        Initializes a Movie object with an ID, title, year, genre, and 
        optional rating.
        """
        self.__id = movie_id  # a private attribute for movie ID
        self.title = title  # a public attribute for the title
        self.year = self.__validate_year(year)  # validates and sets the year
        self.genre = genre  # a public attribute for the genre
        self.rating = self.__format_rating(rating) if rating is not None \
            else None  # formats and sets the rating if provided

    def get_id(self):
        """
        Returns the movie ID.
        """
        return self.__id 

    def __validate_year(self, year):
        """
        Validates the year of the movie. The year must be between 1888 
        and 2024.
        """
        if year is None:
            return None
        if year < 1888 or year > 2024:
            raise ValueError("Year must be between 1888 and 2024")
        return year  # Returns the validated year

    def __format_rating(self, rating):
        """
        Formats the movie rating to two decimal places.
        """
        return round(rating, 2) 

    def add_rating(self, rating):
        """
        Adds or updates the rating of the movie.
        """
        if 0 <= rating <= 10:
            self.rating = self.__format_rating(rating)  # Updates the rating
        else:
            raise ValueError("Rating must be between 0 and 10")

    def __repr__(self):
        """
        Returns a string representation of the Movie object.
        """
        rating_display = f"{self.rating:.2f}" if self.rating is not None \
            else "N/A"  # Determines what to display for the rating
        return f"{self.title} ({self.year}) - Genre: {self.genre}, Rating: " \
               f"{rating_display}"  # Returns the formatted str representation

    def __eq__(self, other): # Magic class method
        """
        Checks if two Movie objects are equal based on the title.
        """
        if isinstance(other, Movie):
            return self.title == other.title  # Compares if titles are equal
        return False  # Returns False if other is not a Movie instance

