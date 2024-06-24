#!/usr/bin/python3
"""takes in arguments and displays all values in the states table of
hbtn_0e_0_usa where name matches the argument. But this time,
write one that is safe from MySQL injections!"""

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
        query = "SELECT * FROM states WHERE name = %s"
        uinput = search
        cur.execute(query, (uinput,))
        rows = cur.fetchall()
        for row in rows:
            print(row)
        cur.close()
        conn.close()
