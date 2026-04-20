from db_config import Database_connection
from db_operations import DB_operations

obj2:DB_operations = DB_operations()

while True:
  print("\n", "="*3, " MENU ", "="*3)
  print("1. Insert User:")
  print("2. Display User:")
  print("3. Update User:")
  print("4. Delete User:")
  print("5. Search User:")
  print("6. Exit:")
  print("="*30)
  choice = int(input("Enter your choice: "))
  if choice == 1:
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")
    obj2.insert_user(name, phone, email)
  elif choice == 2:
    obj2.display_all_users()
  elif choice == 3:
    user_id = int(input("Enter user id to update: "))

    confirm = input("Do you want to update the name? (yes/no): ")
    if confirm.lower() == "yes":
        name = input("Enter name: ")
    else:
        print("Name update cancelled.")
        name = None

    confirm = input("Do you want to update the phone? (yes/no): ")
    if confirm.lower() == "yes":
        phone = input("Enter phone: ")
    else:
        print("Phone update cancelled.")
        phone = None

    confirm = input("Do you want to update the email? (yes/no): ")
    if confirm.lower() == "yes":
        email = input("Enter email: ")
    else:
        print("Email update cancelled.")
        email = None
   
    obj2.update_user(user_id, name, phone, email)
  elif choice == 4:
    user_id = int(input("Enter user id to delete: "))
    obj2.delete_user(user_id)
  elif choice == 5:
    search_term = input("Enter name, phone or email to search: ")
    obj2.search_user(search_term)
  elif choice == 6:
    print("Exiting...")
    obj2.close_connection()
    break
  else:
    print("Invalid choice. Please try again.")