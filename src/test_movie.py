"""
Unit tests for the Movie class check the basic functionality of creating 
a Movie object and handling its rating.
"""

from movie import Movie

def test_movie_creation():
    """
    A test for creating a Movie object and checking its attributes.
    """
    movie = Movie("1", "TENET", 2020, "Sci-Fi", 7.8)
    
    # Assertions to check movie attributes
    assert movie.get_id() == "1"
    assert movie.title == "TENET"
    assert movie.year == 2020
    assert movie.genre == "Sci-Fi"
    assert movie.rating == 7.8

def test_movie_rating():
    """
    A test for adding and updating the rating of a movie.
    """
    movie = Movie("2", "THE MATRIX", 1999, "Sci-Fi")
    
    # Initially, the rating should be None
    assert movie.rating is None
    
    # Add a rating
    movie.add_rating(9.0)
    assert movie.rating == 9.0
    
    # Update the rating
    movie.add_rating(9.5)
    assert movie.rating == 9.5

def run_tests():
    """
    Runs all the tests and prints a success message if all tests pass.
    """
    # Run tests
    test_movie_creation()
    test_movie_rating()
    
    # Print success message
    print("All tests passed!")

if __name__ == "__main__":
    run_tests()
