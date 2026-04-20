# Import the sqlite3 module, which is needed to talk to SQLite databases in Python
import sqlite3

# Import the Database_connection class from another file called db_config
from db_config import Database_connection

# Define a class called DB_operations, which will have our database functions
class DB_operations:

    # The special __init__ function runs when we make an object from this class
    def __init__(self):
        db = Database_connection()             # Make a new Database_connection object
        db.create_table()                      # Call its method to make sure the USERS table is created
        self.conn = db.con                     # Save the database connection object to self.conn for later
        self.cursor = self.conn.cursor()       # Create a cursor for running SQL commands, and save it to self.cursor

    # Add a new user to the USERS table
    def insert_user(self, name: str, phone: str, email: str):
        try:
            # Try to run the SQL INSERT command to add a new row with the given name, phone, and email
            self.cursor.execute("""
                INSERT INTO USERS (name, phone, email)
                VALUES (?, ?, ?)
            """, (name, phone, email))
            self.conn.commit()                          # Save (commit) this new user to the database
            print("User inserted successfully!")        # Tell the user that it worked
        except sqlite3.IntegrityError:
            print("Phone or email already exists!")     # If something's not unique, show an error

    # Update the info of a user who matches a certain user_id
    def update_user(self, user_id: int, name: str, phone: str, email: str):
        try:
            # Collect columns to update only those which are not None
            fields = []
            params = []
            if name is not None:
                fields.append("name = ?")
                params.append(name)
            if phone is not None:
                fields.append("phone = ?")
                params.append(phone)
            if email is not None:
                fields.append("email = ?")
                params.append(email)
            if not fields:
                print("No fields selected to update!")
                return
            params.append(user_id)
            sql = f"""
                UPDATE USERS
                SET {', '.join(fields)}
                WHERE user_id = ?
            """
            self.cursor.execute(sql, tuple(params))
            self.conn.commit()
            if self.cursor.rowcount > 0:
                print("User updated successfully!")         # Tell the user it worked
            else:
                print("Update failed! User id does not exist.")
        except sqlite3.IntegrityError:
            print("Update failed! Phone or email already exists!")  # If new info isn't unique, show an error

    # Delete a user from the table
    def delete_user(self, user_id: int):
        try:
            # Try to delete the user whose id matches user_id
            self.cursor.execute("""
                DELETE FROM USERS
                WHERE user_id = ?
            """, (user_id,))
            self.conn.commit()                          # Save (commit) this deletion
            print("User deleted successfully!")         # Tell the user it worked
        except sqlite3.IntegrityError:
            print("Delete failed! User id does not exist!") # Show an error if something goes wrong

    # Search for a user by name, phone, or email (fuzzy match)
    def search_user(self, search_term: str):
        # Run an SQL SELECT to find any users whose name, phone, or email contains the search_term
        self.cursor.execute("""
            SELECT * FROM USERS
            WHERE name LIKE ? OR phone LIKE ? OR email LIKE ?
        """, (f'%{search_term}%', f'%{search_term}%', f'%{search_term}%'))
        results = self.cursor.fetchall()    # Get all the found rows into a list called results
        if results:
            for row in results:             # Go through each result row
                print(f"ID: {row[0]}, Name: {row[1]}, Phone: {row[2]}, Email: {row[3]}")
        else:
            print("No matching users found!") # If nothing found, print a message

    # Show all users in the USERS table
    def display_all_users(self):
        try:
            self.cursor.execute("""
                SELECT * FROM USERS
            """)                         # Select all users from the table
            results = self.cursor.fetchall()   # Get all users into a list called results
            if results:
                for row in results:           # Go through each user and print info
                    print(f"ID: {row[0]}, Name: {row[1]}, Phone: {row[2]}, Email: {row[3]}")
            else:
                print("No users found!")      # If table is empty, print a message
        except sqlite3.OperationalError:
            print("No data found!")           # If there is some error (like table missing), show a message

    # Close the database connection when we're done using it
    def close_connection(self):
        print("Connection closed successfully!")    # Print a message
        self.conn.close()                          # Actually close the connection
