#!/usr/bin/python3
"""
This script takes in arguments and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument (MySQL injection safe)
"""
import sys
import MySQLdb


if __name__ == "__main__":
    # Check for correct number of arguments
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state>"
              .format(sys.argv[0]))
        sys.exit(1)

    # Gather the arguments
    usr = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state = sys.argv[4]

    # Connect to MySQL
    try:
        db = MySQLdb.connect(
            host='localhost',
            port=3306,
            passwd=password,
            db=database
        )
        cursor = db.cursor()

        # Execute the query
        query = "SELECT * FROM states WHERE BINARY name = %s ORDER BY id ASC"
        cursor.execute(query, (state,))

        # Fetch all the rows
        rows = cursor.fetchall()

        # Print each row in the required format
        for row in rows:
            print(row)

        # Close cursor and connection
        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        print("MySQL Error {}: {}".format(e.args[0], e.args[1]))
        sys.exit(1)
