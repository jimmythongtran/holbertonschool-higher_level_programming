#!/usr/bin/python3
'''
This is the '0-select_states' module

0-select_states connects to the hbtn_0e_0_usa database and
retrieves a specified MySQL query via Python script

'''
import MySQLdb
import sys

db = MySQLdb.connect(host="localhost", port=3306,
                     user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

cur = db.cursor()
cur.execute("SELECT * FROM states ORDER BY states.id ASC")

for info in cur.fetchall():
    print(info)

cur.close()
db.close()
