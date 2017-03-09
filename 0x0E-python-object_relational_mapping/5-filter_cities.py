#!/usr/bin/python3
'''
This is the '5-filter_states' module

5-filter_states takes in name of state as an argument and lists
all cities of that state
'''
if __name__ == "__main__":
    import MySQLdb
    import sys

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    injection = sys.argv[4].split(";")
    cur = db.cursor()
    cur.execute("SELECT * FROM states\
            WHERE name = %s ORDER BY id ASC", (injection[0],))

    for info in cur.fetchall():
        print(info)

    cur.close()
    db.close()
