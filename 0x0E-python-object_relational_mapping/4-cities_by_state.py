#!/usr/bin/python3
'''
This is the '4-cities_by_state' module

4-cities_by_state lists all cities from the db hbtn_0e_4_usa 
'''
if __name__ == "__main__":
    import MySQLdb
    import sys

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    cur = db.cursor()
    cur.execute("SELECT * FROM cities\
            ORDER BY cities.id ASC")

    for info in cur.fetchall():
        print(info)

    cur.close()
    db.close()
