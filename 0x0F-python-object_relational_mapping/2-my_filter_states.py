#!/usr/bin/python3
"""takes in an argument and displays all values in the states table of
    hbtn_0e_0_usa where name matches the argument"""

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
        cur.execute("SELECT * FROM states WHERE states.name\
                    LIKE BINARY '{}' ORDER BY states.id".format(search))
        rows = cur.fetchall()
        for row in rows:
            print(row)
        cur.close()
        conn.close()
