import sqlite3

# Database connection helper
DB_NAME = "tracker.db"


def get_connection():
  """Connects to the SQLite database and returns the connection and cursor."""
  conn = sqlite3.connect(DB_NAME)
  cursor = conn.cursor()
  return conn, cursor


def initialize_database():
  """TODO: Create the 'games' table if it doesn't already exist.

  Columns needed:
  - id (INTEGER, Primary Key, Auto-increment)
  - title (TEXT, Not Null)
  - genre (TEXT)
  - rating (INTEGER)
  """
  # Write your CREATE TABLE SQL statement and execute it here
  pass


def add_game(title, genre, rating):
  """TODO: Insert a new game record into the 'games' table.

  Parameters:
      title (str): The title of the game
      genre (str): The genre of the game
      rating (int): The rating out of 10
  """
  # Write your INSERT INTO SQL query here using parameterized inputs (?)
  pass


def view_all_games():
  """TODO: Retrieve and print all games stored in the database.

  Should fetch all rows from the 'games' table and display them nicely.
  """
  # Write your SELECT * query here, fetch the results, and loop through them
  pass


def search_by_genre(target_genre):
  """TODO: Search and print all games matching a specific genre.

  Parameters:
      target_genre (str): The genre to filter by
  """
  # Write your SELECT query with a WHERE clause here
  pass


def delete_game(game_id):
  """TODO: Delete a game from the database using its unique ID.

  Parameters:
      game_id (int): The ID of the game to remove
  """
  # Write your DELETE FROM query with a WHERE clause here
  pass


# --- Main program loop to test the functions ---
if __name__ == "__main__":
  # Initialize the database table first
  initialize_database()

  # Example testing area (uncomment as functions are completed):
  # add_game("The Legend of Zelda", "Adventure", 10)
  # add_game("Minecraft", "Sandbox", 9)
  # view_all_games()
