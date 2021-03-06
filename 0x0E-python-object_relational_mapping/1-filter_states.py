#!/usr/bin/python3
"""This is the '1-filter_states' module
USAGE: ./1-filter_states mysqlname mysqlpw db_name
"""
if __name__ == '__main__':
    import MySQLdb
    import sys

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    cur = db.cursor()
    cur.execute("""SELECT * FROM states\
            WHERE name LIKE 'N%' ORDER BY states.id ASC""")

    for info in cur.fetchall():
        if info[1][0] == 'N':
            print(info)

    cur.close()
    db.close()
