import sqlite3

def main():
    # Connect to SQLite database (creates file if it doesn't exist)
    conn = sqlite3.connect("test.db")
    cursor = conn.cursor()

    # Create table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Employee (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL
    );
    """)

    # Insert data (prevent duplicates using INSERT OR IGNORE)
    cursor.execute("INSERT OR IGNORE INTO Employee (name, email) VALUES ('Alice', 'alice@gmail.com')")
    cursor.execute("INSERT OR IGNORE INTO Employee (name, email) VALUES ('Bob', 'bob@gmail.com')")

    # Update data
    cursor.execute("UPDATE Employee SET email = ? WHERE name = ?", ("biswas@gmail.com", "Alice"))

    # Fetch all tables
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    print("\n--- Database Tables and Their Rows ---")
    for table in tables:
        table_name = table[0]
        print(f"\nTable: {table_name}")

        cursor.execute(f"SELECT * FROM {table_name}")
        rows = cursor.fetchall()

        if rows:
            for row in rows:
                print(row)
        else:
            print("No rows found.")

    # Commit changes and close connection
    conn.commit()
    conn.close()

if __name__ == "__main__":
    main()
