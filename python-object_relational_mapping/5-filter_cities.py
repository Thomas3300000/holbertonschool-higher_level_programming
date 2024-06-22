#!/usr/bin/python3
"""
 script that takes in the name of a state as an argument and lists all cities
 of that state, using the database hbtn_0e_4_usa

Arguments:
- username of the MySQL user
- password of the MySQL user
- database name of the MySQL server
- state name
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
    sel = """SELECT cities.name
        FROM cities INNER JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC"""
    cur.execute(sel, (state_name,))
    cities = cur.fetchall()

    city_names = []
    for city in cities:
        city_names.append(city[0])
    print(", ".join(city_names))

    cur.close()
    db.close()
