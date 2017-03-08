#!/usr/bin/python3
'''
This is the '1-filter_states' module

1-filter_states connects to the hbtn_0e_0_usa database and
retrieves state names beginning with 'N' via Python script
'''

import MySQLdb
import sys

db = MySQLdb.connect(host="localhost", port=3306,
                     user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

cur = db.cursor()
cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY states.id ASC")

for info in cur.fetchall():
    print(info)

cur.close()
db.close()
