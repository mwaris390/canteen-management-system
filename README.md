# Canteen Management System 🍔📊

Welcome to the **Canteen Management System** – your solution for efficient management of sales, food items, and transactions. This modern system empowers users to perform CRUD operations on both Salesmen and Food lists, along with handling transactions akin to any other Point of Sale (POS) system. Notably, the system stores critical data such as salesman commissions and sales records for streamlined monitoring.

## Overview 📋

The **Canteen Management System** is a comprehensive platform that offers the following features:

- **CRUD Operations:** Seamlessly Create, Read, Update, and Delete entries for Salesmen and Food items.
- **Point of Sale:** Conduct transactions with ease, just like in a traditional POS system.
- **Data Storage:** The system employs an SQLite database powered by Django's Object-Relational Mapping (ORM) capabilities.
- **Session Management:** Leveraging Django Sessions, user interactions are secure and personalized.

## Technologies Used 🛠️

The **Canteen Management System** harnesses the power of the following technologies:

- Python 🐍
- Django 🌐
- ORM SQLite 🗄️
- Django Sessions 🔐

## Installation Instructions 🚀

To get started with the **Canteen Management System**, follow these steps:

1. **Clone the Repository:** Start by cloning this repository to your local machine using the following command:
   ```git clone https://github.com/yourusername/canteen-management-system.git```
3. **Navigate to Directory:** Move into the project directory:
   ```cd canteen-management-system```
5. **Create a Virtual Environment:** Set up a virtual environment to isolate project dependencies:
   ```python -m venv venv```
7. **Activate the Virtual Environment:** Activate the virtual environment you just created:
- On Windows:
  ```
  venv\Scripts\activate
  ```
- On macOS and Linux:
  ```
  source venv/bin/activate
  ```
5. **Install Dependencies:** Install the required dependencies using pip:
   ```pip install -r requirements.txt```
6. **Apply Migrations:** Apply the database migrations:
   ```python manage.py migrate```
7. **Run the Server:** Launch the development server:
   ```python manage.py runserver```
8. **Access the App:** Open your web browser and go to `http://127.0.0.1:8000/` to access the Canteen Management System.
