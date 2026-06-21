# Smart Contact Book 📱

A modern, desktop-based contact management application built with Python. This project transitions from a simple flat-file storage system to a robust, relational database architecture using SQLite, implementing full **CRUD** (Create, Read, Update, Delete) operations.

## 🚀 Features
- **Modern UI:** Built using `CustomTkinter` for a clean, platform-adaptive design featuring automated dark/light mode synchronization.
- **Data Persistence:** Integrated with an `SQLite3` relational database for efficient, structural data storage.
- **Robust Validation:** Implements defensive programming blocks to handle empty inputs, non-digit inputs, and strict 10-digit phone number validations.
- **Fail-Safe Operations:** Includes user-confirmation safety pop-ups for destructive events like permanent contact deletions.

## 🏗️ Architecture & Core Concepts
This application serves as a foundational software engineering project demonstrating:
- **Relational Databases:** Designing structured tables, utilizing primary keys, and writing sanitized parameterized SQL queries to prevent SQL injection.
- **Event-Driven Programming:** Handling asynchronous user interactions and dynamic UI switching using Tkinter's frame allocation layout.
- **Defensive Design:** Catching user input errors at the boundary layer before they interact with the storage engine.

## 🛠️ Tech Stack
- **Language:** Python 3
- **GUI Framework:** CustomTkinter / Tkinter
- **Database Engine:** SQLite3 (Built-in Relational DBMS)

## 🔧 How To Run

1. Clone the repository:
```bash
   git clone https://github.com/zainastanley/Smart-contact-book.git

# 2. Navigate into the project folder
cd Smart-contact-book

# 3. Install the required modern GUI library
pip install customtkinter

# 4. Run the application
python app.py
```

Developed as a core technical project during my B.tech 2nd year