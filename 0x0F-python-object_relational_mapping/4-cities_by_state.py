#!/usr/bin/python3
"""
This script lists all cities from the database hbtn_0e_0_usa
"""
import sys
import MySQLdb


if __name__ == "__main__":
    # Check for correct number of arguments
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>"
              .format(sys.argv[0]))
        sys.exit(1)

    # Gather arguments
    usr = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to MySQL
    try:
        db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=usr,
            passwd=password,
            db=database
        )
        cursor = db.cursor()

        # Execute the query with a join to get city and state names
        query = """
        SELECT cities.id, cities.name, states.name FROM cities JOIN states
        ON cities.state_id = states.id ORDER BY cities.id ASC
        """
        cursor.execute(query)

        # Fetch all the rows
        rows = cursor.fetchall()

        # Print each row in required format
        for row in rows:
            print(row)

        # Close cursor and connection
        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        print("MySQL eRROR {}: {}".format(e.args[0], e.args[1]))
        sys.exit(1)
