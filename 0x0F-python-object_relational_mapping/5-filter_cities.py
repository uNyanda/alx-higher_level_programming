#!/usr/bin/python3
"""
This script filters cities by the given state name from the database
hbtn_0e_4_usa.
"""
import sys
import MySQLdb


if __name__ == "__main__":
    # Check correct number of arguments provided
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state>"
              .format(sys.argv[0]))
        sys.exit(1)

    # Gather the arguments
    usr = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state = sys.argv[4]

    # Connect to MySQL database
    try:
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=usr,
            passwd=password,
            db=database
        )

        # Create cursor object
        cursor = db.cursor()

        # Write the SQL query
        query = """
        SELECT GROUP_CONCAT(cities.name ORDER BY cities.id ASC SEPARATOR ', ')
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s;
        """

        # Execute the query
        cursor.execute(query, (state,))

        # Fetch the result
        rows = cursor.fetchone()

        # Print the result if it's not None
        if rows and rows[0] is not None:
            print(rows[0])
        else:
            print("")

        # Close the cursor and connection
        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        print("MySQL Error {}: {}".format(e.args[0], e.args[1]))
        sys.exit(1)
