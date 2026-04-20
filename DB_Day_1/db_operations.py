import sqlite3
from db_config import Database_connection

class DB_operations:

    def __init__(self):
        db = Database_connection()
        db.create_table()
        self.conn = db.con
        self.cursor = self.conn.cursor()

    def insert_user(self, name: str, phone: str, email: str):
        try:
            self.cursor.execute("""
                INSERT INTO USERS (name, phone, email)
                VALUES (?, ?, ?)
            """, (name, phone, email))
            self.conn.commit()
            print("User inserted successfully!")
        except sqlite3.IntegrityError:
            print("Phone or email already exists!")

    def update_user(self, user_id: int, name: str, phone: str, email: str):
        try:
            self.cursor.execute("""
                UPDATE USERS
                SET name = ?, phone = ?, email = ?
                WHERE user_id = ?
            """, (name, phone, email, user_id))
            self.conn.commit()
            print("User updated successfully!")
        except sqlite3.IntegrityError:
            print("Update failed! Phone or email already exists!")

    def delete_user(self, user_id: int):
        try:
            self.cursor.execute("""
                DELETE FROM USERS
                WHERE user_id = ?
            """, (user_id,))
            self.conn.commit()
            print("User deleted successfully!")
        except sqlite3.IntegrityError:
            print("Delete failed! User id does not exist!")

    def search_user(self, search_term: str):
        self.cursor.execute("""
            SELECT * FROM USERS
            WHERE name LIKE ? OR phone LIKE ? OR email LIKE ?
        """, (f'%{search_term}%', f'%{search_term}%', f'%{search_term}%'))
        results = self.cursor.fetchall()
        if results:
            for row in results:
                print(f"ID: {row[0]}, Name: {row[1]}, Phone: {row[2]}, Email: {row[3]}")
        else:
            print("No matching users found!")

    def display_all_users(self):
        try:
            self.cursor.execute("""
                SELECT * FROM USERS
            """)
            results = self.cursor.fetchall()
            if results:
                for row in results:
                    print(f"ID: {row[0]}, Name: {row[1]}, Phone: {row[2]}, Email: {row[3]}")
            else:
                print("No users found!")
        except sqlite3.OperationalError:
            print("No data found!")

    def close_connection(self):
        print("Connection closed successfully!")
        self.conn.close()
