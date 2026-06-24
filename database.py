import sqlite3

# Connect to database
conn = sqlite3.connect("talentvault.db")

cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS candidates (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT,
    mobile TEXT,
    city TEXT,
    designation TEXT,
    experience INTEGER,
    qualification TEXT,
    position TEXT,
    skills TEXT,
    resume_path TEXT
)
""")

conn.commit()

print("TABLES:")
cursor.execute(
    "SELECT name FROM sqlite_master WHERE type='table'"
)
print(cursor.fetchall())

print("\nCANDIDATE DATA:")

try:
    cursor.execute("SELECT * FROM candidates")

    rows = cursor.fetchall()

    if rows:
        for row in rows:
            print(row)
    else:
        print("No records found.")

except Exception as e:
    print("Error:", e)

conn.close()

print("\nDatabase Ready.")