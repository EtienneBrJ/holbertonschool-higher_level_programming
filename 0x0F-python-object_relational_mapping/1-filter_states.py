#!/usr/bin/python3
import sys
import MySQLdb

db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                     passwd=sys.argv[2], db=sys.argv[3])
c = db.cursor()
c.execute("SELECT * FROM states WHERE name LIKE 'N%'")
[print(state) for state in c.fetchall()]
