# Database-connectivity-using-sqlit3
Here we understand how to connection establish between pyhon and sqlit3 database.
# 🗄️ SQLite User Management System (Python)

## 📌 Overview

This project is a simple **User Management System** built using **Python** and **SQLite3**. It demonstrates how to establish a database connection, create tables, and perform basic operations like inserting and displaying user data.

This project is designed for **beginners** to understand how database connectivity works in Python and how to structure code using multiple files.

---

## 🚀 Features

* ✅ Database connection using SQLite3
* ✅ Table creation with constraints (PRIMARY KEY, UNIQUE, NOT NULL)
* ✅ Insert user data
* ✅ Display all users
* ✅ Menu-driven program (CLI-based)
* ✅ Modular code structure (separate files)

---

## 🗂️ Project Structure

```
project/
│── db_config.py        # Database connection & table creation
│── db_operations.py    # Insert & display operations
│── main.py             # Menu-driven user interface
│── mydb.db             # SQLite database file (auto-created)
```

---

## ⚙️ Technologies Used

* Python 🐍
* SQLite3 (built-in database)

---

## 🔧 How It Works

### 1️⃣ Database Connection

* A class `Database_connection` is used to establish a connection with SQLite database.
* The database file (`mydb.db`) is created automatically if it does not exist.

### 2️⃣ Table Creation

* A `USERS` table is created with fields:

  * `user_id` (Primary Key, Auto Increment)
  * `name`
  * `phone` (Unique)
  * `email` (Unique)

### 3️⃣ Database Operations

* Insert new user records
* Display all stored users

### 4️⃣ Main Program

* Provides a menu-driven interface for user interaction

---

## ▶️ How to Run

```bash
python main.py
```

---

## 🧠 Problems I Faced

While building this project, I encountered several issues:

* ❌ Incorrect SQL syntax (e.g., `AUTOINCR` instead of `AUTOINCREMENT`)
* ❌ Connection closed too early (`conn.close()` inside wrong methods)
* ❌ Not creating object instances before calling class methods
* ❌ Syntax errors in Python (extra quotes in SQL query)
* ❌ Confusion between class methods and instance methods

---

## 💡 How I Solved Them

* ✅ Fixed SQL syntax errors carefully
* ✅ Managed database connection properly (open once, close at end)
* ✅ Used object-oriented approach correctly
* ✅ Debugged Python syntax issues
* ✅ Separated logic into multiple files for better structure

---

## 📚 Key Learnings

* How to connect Python with SQLite database
* Importance of connection management
* Writing clean and modular code
* Basics of CRUD operations
* Debugging real-world coding errors

---

## 🔮 Future Improvements

* 🔄 Add Update and Delete functionality
* 🔍 Search users by phone/email
* 🖥️ Build GUI using Tkinter
* 🌐 Convert into web app using Flask/Django

---

## 🙌 Author

**Subham Chakraborty**
💻 Full-Stack Developer (MERN | Python)

---

## ⭐ Support

If you like this project, please ⭐ star the repository!
