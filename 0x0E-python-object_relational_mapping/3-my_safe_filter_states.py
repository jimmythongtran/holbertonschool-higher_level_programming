#!/usr/bin/python3
'''
This is the '3-my_safe_filter_states' module

3-my_safe_filter_states connects retrieves the name when specified by
the argument passed through that's safe from MySQL injection!
'''
if __name__ == "__main__":
    import MySQLdb
    import sys

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    cur = db.cursor()
    cur.execute("SELECT * FROM states\
        WHERE name = '{:s}' ORDER BY\
        states.id ASC".format(sys.argv[4],))

    for info in cur.fetchall():
        print(info)

    cur.close()
    db.close()
