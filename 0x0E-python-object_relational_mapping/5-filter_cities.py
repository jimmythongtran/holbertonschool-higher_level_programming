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
    cur.execute("SELECT * FROM cities JOIN states\
            ON states.id = cities.state_id  ORDER BY id ASC")

    states = list()
    for info in cur.fetchall():
        if data[4] == injection[0]:
            state.append(data[2])

    print(", ".join(state))
    cur.close()
    db.close()
