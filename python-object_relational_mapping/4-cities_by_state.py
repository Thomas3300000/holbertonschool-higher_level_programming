#!/usr/bin/python3
"""
Script that lists all cities from the database hbtn_0e_4_usa

Arguments:
- username of the MySQL user
- password of the MySQL user
- database name of the MySQL server
"""
if __name__ == "__main__":
    import MySQLdb
    import sys
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cur = db.cursor()
    cities = "SELECT cities.id, cities.name, states.name\
        FROM cities JOIN states ON cities.state_id = states.id\
        ORDER BY cities.id ASC"
    cur.execute(cities)
    states = cur.fetchall()

    for row in states:
        print(row)

    cur.close()
    db.close()
