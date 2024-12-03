import sqlite3

# Connect to the database (creates the database if it doesn't exist)
conn = sqlite3.connect('data.db')
cursor = conn.cursor()

# Create the k_line table
cursor.execute('''
CREATE TABLE IF NOT EXISTS k_line (
    timestamp TEXT,
    value REAL
)
''')

# Insert some sample data
cursor.executemany('''
INSERT INTO k_line (timestamp, value) VALUES (?, ?)
''', [
    ('2024-12-01 10:00:00', 100.0),
    ('2024-12-01 10:01:00', 101.5),
    ('2024-12-01 10:02:00', 102.0),
    ('2024-12-01 10:03:00', 103.0),
    ('2024-12-01 10:04:00', 104.0),
    ('2024-12-01 10:06:00', 90.0)
])

# Commit the changes and close the connection
conn.commit()
conn.close()
