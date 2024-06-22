#!/usr/bin/python3
"""
Lists all records from the database hbtn_0e_0_usa
name matching the argument

arguments:
- username of the MySQL user
- password of the MySQL user
- database name of the MySQL server
- state name searched: arguments to match
"""
if __name__ == "__main__":
    import MySQLdb
    import sys
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database

    )

    cur = db.cursor()
    arg = """SELECT * FROM states
        WHERE name = '{}' ORDER BY id ASC""".format(state_name)
    cur.execute(arg)
    states = cur.fetchall()

    for row in states:
        print(row)

    cur.close()
    db.close()
