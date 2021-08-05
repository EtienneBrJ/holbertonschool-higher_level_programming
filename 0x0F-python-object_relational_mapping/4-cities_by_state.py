#!/usr/bin/python3
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT cities.id, cities.name, states.name\
            FROM cities JOIN states\
            ON states.id = cities.state_id\
            ORDER BY cities.id")
    [print(cities) for cities in c.fetchall()]
