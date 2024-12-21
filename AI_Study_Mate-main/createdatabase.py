import sqlite3
import csv

def create_table(conn):
    cursor = conn.cursor()

    # Create a single table to store CSV data for all subjects
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS videolink (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            TopicName TEXT,
            link TEXT
        )
    ''')

    return cursor

def create_database(csv_file_path, database_name):
    # Connect to SQLite database
    conn = sqlite3.connect(database_name)
    cursor = create_table(conn)

    # Read data from the CSV file and insert into the database
    with open(csv_file_path, 'r', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)  # Skip the header row if it exists

        for row in csv_reader:
            # Check if the row has the expected number of elements
            if len(row) == 2:
                cursor.execute('''
                    INSERT INTO videolink (TopicName, link)
                    VALUES (?, ?)
                ''', (row[0], row[1]))
            else:
                print(f"Skipping row: {row}. Expected 2 elements, found {len(row)}.")

    # Commit changes
    conn.commit()

    # Close the connection
    conn.close()

    print(f"Database {database_name} creation and data import completed.")

# Example usage for a single CSV file and a single database
csv_file_path = 'videolink.csv'  # Replace with your CSV file path
database_name = 'videolink.db'  # Replace with your desired database name

create_database(csv_file_path, database_name)
