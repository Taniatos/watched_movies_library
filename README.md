## Watched Movies Library

### Project Overview
The **Watched Movies Library** is a Python-based command-line application that allows users to manage a CSV-stored collection of movies. Users can add, edit, delete, and display movies, filter by genre, and calculate average ratings. The program is divided into multiple modules for movie operations, file handling, and unit testing.

### Features
- **Add, Edit, Delete, Display Movies**: Allows basic CRUD operations on a movie collection.
- **Filter by Genre**: View movies by genre for easier browsing.
- **Calculate Average Ratings**: Calculate average ratings across the library.

### Core Components
- **Container Types**:  
  - **Dictionary**: Stores movies by unique ID.
  - **Tuple**: Immutable options for genres.
  - **Set**: Manages unique genres.
  - **List**: Handles movie collections for processing.
- **Control Structures**:  
  - **Loops**: `for` and `while` loops for managing movie collections and program flow.
  - **Conditionals**: `if` statements validate inputs and handle scenarios.
- **Error Handling**:  
  - `try-except` blocks validate input and manage file operations.

### `Movie` Class
The `Movie` class is the central structure, with:
- **Attributes**:  
  - Private `__id`, Public `title`, `year`, `genre`, `rating`.
- **Methods**:  
  - Year validation, rating formatting, and string representation.
  - Implements dunder methods `__init__`, `__repr__`, and `__eq__`.

### Core Operations
Each core function (e.g., `add_movie()`, `edit_movie()`) is user-defined, accepting parameters to perform actions and return results or updates.

### File Management
The program reads from and writes to a `movies.csv` file for persistent movie storage.

### Unit Testing
The `test_movie.py` file tests `Movie` class functionality, with `assert` statements verifying:
- Object creation
- Rating updates
- Method functionality

### Usage
This project is a straightforward tool for users to manage their movie library with essential functionalities like genre filtering and average rating calculations.

**Watched Movies Library** is user-friendly and practical, designed to streamline movie management through an intuitive command-line interface.