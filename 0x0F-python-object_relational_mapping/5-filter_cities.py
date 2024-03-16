#!/usr/bin/python3
"""
Script that takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    """
    Connect to the database and retrieve cities based on the state name.
    """

    # Extract arguments
    username, password, database, state_name = sys.argv[1:]

    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=database)

    # Create a cursor object using cursor() method
    cursor = db.cursor()

    # Prepare SQL query with parameterized query for state name
    sql_query = """
    SELECT GROUP_CONCAT(cities.name SEPARATOR ', ')
    FROM cities
    JOIN states
    ON cities.state_id = states.id
    WHERE states.name LIKE BINARY %s
    """

    # Execute SQL query with state name as parameter
    cursor.execute(sql_query, (state_name,))

    # Fetch the result and print it
    result = cursor.fetchone()

    if result is not None:
        print(result[0])

    # Close the cursor and Database connection
    cursor.close()
    db.close()
