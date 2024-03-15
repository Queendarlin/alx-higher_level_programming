#!/usr/bin/python3
"""Script that retrieves and prints all states from the specified database."""

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

    # Prepare SQL query with user input using format
    sql_query = "SELECT * FROM states WHERE name = '{}' " \
                "ORDER BY id ASC".format(state_name)

    # Execute SQL query
    cursor.execute(sql_query)

    # Fetch all rows and print them
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Close the cursor and Database connection
    cursor.close()
    db.close()
