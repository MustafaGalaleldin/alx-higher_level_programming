#!/usr/bin/python3
"lists all cities from the database"

if __name__ == '__main__':
    "check if executed"
    import MySQLdb
    import sys

    argv = sys.argv
    if len(argv) == 4:
        name = argv[1]
        password = argv[2]
        db = argv[3]
        conn = MySQLdb.connect(host='localhost', port=3306, user=name,
                                    passwd=password, db=db, charset='utf8')
        cur = conn.cursor()
        cur.execute("SELECT cities.id, cities.name, states.name FROM cities\
                    JOIN states ON cities.state_id = states.id\
                    ORDER BY cities.id")
        rows = cur.fetchall()
        for row in rows:
            print(row)
        cur.close()
        conn.close()
