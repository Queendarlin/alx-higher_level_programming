#!/usr/bin/python3
"""Script that takes in the name of a state as an argument
and lists all cities of that state"""

import MySQLdb
import sys

if __name__ == "__main__":
    """Executes the script when run directly."""
    # Extract arguments
    username, password, database, state_name = sys.argv[1:]

    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=database)

    # Create a cursor object using cursor() method
    cursor = db.cursor()

    # Execute SQL query with state name as parameter
    cursor.execute("""
    SELECT cities.id, cities.name
    FROM cities
    JOIN states
    ON cities.state_id = states.id
    WHERE states.name LIKE BINARY %(state_name)s
    ORDER BY cities.id ASC
    """, {state_name})

    # Fetch the result and print it
    result = cursor.fetchall()

    if result is not None:
        print(", ".join([row[1] for row in result]))

    # Close the cursor and Database connection
    cursor.close()
    db.close()
