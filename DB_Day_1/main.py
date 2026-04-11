from db_config import Database_connection
from db_operations import DB_operations

obj2:DB_operations = DB_operations()

while True:
  print("\n", "="*3, " MENU ", "="*3)
  print("1. Insert User:")
  print("2. Display User:")
  print("3. Exit:")
  print("="*30)
  choice = int(input("Enter your choice: "))
  if choice == 1:
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")
    obj2.insert_user(name, phone, email)
  elif choice == 2:
    obj2.display_user()
  elif choice == 3:
    obj2.close_connection()
    break