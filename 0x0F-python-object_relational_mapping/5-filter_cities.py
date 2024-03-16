#!/usr/bin/python3
"""Script that lists all cities from the database"""

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

    # Prepare SQL query with parameterized query for state name
    sql_query = """
    SELECT GROUP_CONCAT(name SEPARATOR ', ')
    FROM cities
    WHERE state_id = (SELECT id FROM states WHERE name = %s)
    """

    # Execute SQL query with state name as parameter
    cursor.execute(sql_query, state_name)

    # Fetch the result and print it
    result = cursor.fetchone()

    if result is not None:
        print(result[0])

    # Close the cursor and Database connection
    cursor.close()
    db.close()
