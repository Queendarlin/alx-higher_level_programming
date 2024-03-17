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

    # Connect to MySQL server
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3]))

    # Create a cursor object using cursor() method
    cursor = db.cursor()

    # Prepare SQL query with parameterized query for state name
    cursor.execute("""
            SELECT
                cities.id, cities.name
            FROM
                cities
            JOIN
                states
            ON
                cities.state_id = states.id
            WHERE
                states.name LIKE BINARY %(state_name)s
            ORDER BY
                cities.id ASC
        """, {
            'state_name': argv[4]
        })
    result = cursor.fetchall()

    if result is not None:
        print(", ".join([row[1] for row in result]))

    # Close the cursor and Database connection
    cursor.close()
    db.close()
