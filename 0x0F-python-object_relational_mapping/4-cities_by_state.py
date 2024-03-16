#!/usr/bin/python3
"""Script that lists all cities from the database"""

import MySQLdb
import sys

if __name__ == "__main__":
    """Executes the script when run directly."""
    # Extract arguments
    username, password, database = sys.argv[1:]

    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=database)

    # Create a cursor object using cursor() method
    cursor = db.cursor()

    # Execute SQL query to fetch all cities with state name
    cursor.execute("""
    SELECT cities.id, cities.name, states.name
    FROM cities
    JOIN states
    ON cities.state_id = states.id
    ORDER BY cities.id ASC
    """)

    # Fetch all rows and print them
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Close the cursor and Database connection
    cursor.close()
    db.close()
