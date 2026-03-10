from conf.connection.database import DatabaseConnection
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()


# A function to setup the database
def main():

    print("Trying to connect to the database...")

    # Creates a database instance
    db = DatabaseConnection(
        os.getenv("DATABASE_HOST"),
        os.getenv("DATABASE_PORT"),
        os.getenv("DATABASE_USER"),
        os.getenv("DATABASE_PASSWORD"),
    )

    # Handles errors when setting the database
    try:
        # Creates a database connection
        db.connect()

        # Checks if there is a database connection
        if db.connection:
            cursor = db.connection.cursor()

            print("Creating a database schema and tables...")

            # Fetch commands from Setup.sql
            with open("./conf/sql/setup.sql", 'r', encoding='utf-8') as f:
                sql_commands = f.read().split(';')

            # Executes fetched commands
            for command in sql_commands:
                if command.strip():
                    cursor.execute(command)

            # Commits the changes
            db.connection.commit()
            print("✅ Database schema and tables created successfully!")

            print("Importing books into the database...")

            # Fetch commands from books.sql
            with open('./conf/sql/books.sql', 'r', encoding='utf-8') as f:
                sql_commands = f.read().split(';')

            # Execute fetched commands
            for command in sql_commands:
                if command.strip():
                    cursor.execute(command)

            # Commits the changes
            db.connection.commit()
            print("✅ Books data inserted successfully!")
            cursor.close()

            print("Database has been successfully configured!")
        else:
            print("Something went wrong! Please try again later...")

    except Exception as e:
        print(f"❌ Error during setup: {e}")
        print(e.args)

    finally:
        db.disconnect()
