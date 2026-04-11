import sqlite3
from db_config import Database_connection

class DB_operations:

   def __init__(self):
      
      db = Database_connection()
      self.conn = db.con
      self.cursor = self.conn.cursor()
      
   
   def insert_user(self,name:str,phone:str,email:str):
      
      try:
           self.cursor.execute("""
     
                       INSERT INTO USERS (name,phone,email)
                       VALUES(?,?,?)
     
                           """,(name,phone,email))
           self.conn.commit()
           print("User insertd succesfully!!")

      except sqlite3.IntegrityError:
         print("Phone or email alrady exit!!!")

   def close_connection(self):
      print("Connection closed successfully!!")
      self.conn.close()
      
   
   def display_user(self):
      pass
   





