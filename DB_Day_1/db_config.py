# Import the sqlite3 module, which is used to interact with SQLite databases in Python
import sqlite3

# Define a class to handle database connections and operations
class Database_connection:

  # The constructor method, called when an object of this class is created
  def __init__(self):
    # Establish a connection to the SQLite database file 'mydb.db'.
    # If the file does not exist, it will be created automatically.
    self.con = sqlite3.connect("mydb.db")
  
  # Method to create the USERS table in the database if it does not already exist
  def create_table(self):
    
    # Create a cursor object. The cursor allows us to execute SQL commands.
    cursor = self.con.cursor()

    # Use the cursor to execute a SQL command that creates a table.
    # The '''...''' string contains the SQL for creating a table named USERS, with:
    # - user_id: an integer primary key that auto-increments for each new user
    # - name: a text column that cannot be null
    # - phone: a text column that cannot be null and must be unique
    # - email: a text column that cannot be null and must be unique
    cursor.execute('''

          CREATE TABLE IF NOT EXISTS USERS (
                   user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT NOT NULL,
                   phone TEXT NOT NULL UNIQUE,
                   email TEXT NOT NULL UNIQUE
                   
                   )
     ''')

    # Commit the database transaction to save the table creation
    self.con.commit()
    

# The following code is commented out. If you want to run this file standalone, you could use it to
# create the database and the USERS table:
# def main():
#       obj : Database_connection = Database_connection()
#       obj.create_table()

# main()
