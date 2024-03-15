#!/usr/bin/python3

import MySQLdb

"""Retrieves and prints all states from the specified database."""


def get_all_states(username, password, database_name):
    """Connects to the database and fetches all states sorted by ID."""
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database_name
    )

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    db.close()


if __name__ == "__main__":
    """Executes the script when run directly."""
    import sys
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    get_all_states(username, password, database_name)
