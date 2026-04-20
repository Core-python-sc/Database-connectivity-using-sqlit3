# Import the Database_connection class from db_config.py for database setup (not used directly in this file)
from db_config import Database_connection
# Import the DB_operations class from db_operations.py to interact with the USERS table
from db_operations import DB_operations

# Create an instance (object) of DB_operations, which gives us methods to manage user records
obj2:DB_operations = DB_operations()

# Start an infinite loop to keep showing the menu until the user chooses to exit
while True:
    # Print a menu header
    print("\n", "="*3, " MENU ", "="*3)
    # Print the menu options for the user to choose from
    print("1. Insert User:")
    print("2. Display User:")
    print("3. Update User:")
    print("4. Delete User:")
    print("5. Search User:")
    print("6. Exit:")
    print("="*30)
    # Take the user's menu choice as an integer input
    choice = int(input("Enter your choice: "))
    # If the user chooses to insert a new user
    if choice == 1:
        # Prompt for the new user's name, phone, and email
        name = input("Enter name: ")
        phone = input("Enter phone: ")
        email = input("Enter email: ")
        # Call the insert_user method to add the user to the database
        obj2.insert_user(name, phone, email)
    # If the user chooses to display all users
    elif choice == 2:
        # Call the display_all_users method to print all users from the database
        obj2.display_all_users()
    # If the user wants to update information of a user
    elif choice == 3:
        # Prompt for user id of the user to update
        user_id = int(input("Enter user id to update: "))

        # Ask if the user wants to update the name field
        confirm = input("Do you want to update the name? (yes/no): ")
        if confirm.lower() == "yes":
            # Prompt for the new name
            name = input("Enter name: ")
        else:
            # Print a message if name update is skipped and set name as None
            print("Name update cancelled.")
            name = None

        # Ask if the user wants to update the phone field
        confirm = input("Do you want to update the phone? (yes/no): ")
        if confirm.lower() == "yes":
            # Prompt for the new phone number
            phone = input("Enter phone: ")
        else:
            # Print a message if phone update is skipped and set phone as None
            print("Phone update cancelled.")
            phone = None

        # Ask if the user wants to update the email field
        confirm = input("Do you want to update the email? (yes/no): ")
        if confirm.lower() == "yes":
            # Prompt for the new email
            email = input("Enter email: ")
        else:
            # Print a message if email update is skipped and set email as None
            print("Email update cancelled.")
            email = None

        # Call the update_user method to change user data with the new or unchanged (None) values
        obj2.update_user(user_id, name, phone, email)
    # If the user wants to delete a user
    elif choice == 4:
        # Prompt for user id to delete
        user_id = int(input("Enter user id to delete: "))
        # Call the delete_user method to remove the user from the database
        obj2.delete_user(user_id)
    # If the user wants to search for a user
    elif choice == 5:
        # Prompt for the search term (can be name, phone, or email)
        search_term = input("Enter name, phone or email to search: ")
        # Call the search_user method to find and display matching users
        obj2.search_user(search_term)
    # If the user wants to exit the program
    elif choice == 6:
        # Announce exit and close the database connection
        print("Exiting...")
        obj2.close_connection()
        break   # Exit the while True loop to end the program
    # If the user enters an invalid choice
    else:
        print("Invalid choice. Please try again.")