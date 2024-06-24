#!/usr/bin/python3
"""takes in the name of a state as an argument and lists
all cities of thatstate, using the database hbtn_0e_4_usa"""

if __name__ == '__main__':
    "check if executed"
    import MySQLdb
    import sys

    argv = sys.argv
    if len(argv) == 5:
        name = argv[1]
        password = argv[2]
        db = argv[3]
        search = argv[4]
        conn = MySQLdb.connect(host='localhost', port=3306, user=name,
                                    passwd=password, db=db, charset='utf8')
        cur = conn.cursor()
        cur.execute("SELECT cities.name FROM cities JOIN states ON\
                    cities.state_id = states.id WHERE states.name = '{}'\
                    ORDER BY cities.id".format(search))
        rows = cur.fetchall()
        i = 0
        for row in rows:
            if i:
                print(', ', end='')
            i = 1
            print(row[0], end='')
        print()
        cur.close()
        conn.close()
