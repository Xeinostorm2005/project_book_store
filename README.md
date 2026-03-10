# Book Store Project
---

## About
A Python Project requested by the university as a project assignment. 
The project is subjected to Databases and Data modelling. The assigment is to create an application that will be linked to MYSQL. The application must have these requirments:
- Login/Register system
- Books Browsing
- Add To Cart
- View Cart
- View Recipet
- Export Recipt

## Repository Details
- Author: Xeinostorm
- Created: 2026-03-08
- Published: UNKNOWN
- Last Updated: 2026-03-08

## Requirements
Before running the application you need to install the required dependencies:
```bash
pip install python-dotenv bcrypt mysql-connector-python
```

You need also to create a file called `.env`, that's the file where you will be storing the database information. The content of the file must be like this:
```bash
DATABASE_HOST="ENTER_HOST_IP"
DATABASE_PORT="3306"
DATABASE_USER="ENTER_DATABASE_USER"
DATABASE_PASSWORD="ENTER_DATABASE_PASSWORD"
DATABASE_NAME="ENTER_DATABASE_NAME"
```

## Run The Application
To start the application you need to enter this command in the terminal:
```bash
python main.py
```