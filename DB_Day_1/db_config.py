import sqlite3

class Database_connection:

  def __init__(self):
    self.con = sqlite3.connect("mydb.db")
  
  def create_table(self):
    
    cursor = self.con.cursor()

    cursor.execute('''

          CREATE TABLE IF NOT EXISTS USERS (
                   user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT NOT NULL,
                   phone TEXT NOT NULL UNIQUE,
                   email TEXT NOT NULL UNIQUE
                   
                   )






     ''')
    self.con.commit()
    self.con.close()
    

# def main():
#       obj : Database_connection = Database_connection()
#       obj.create_table()


  
# main()
