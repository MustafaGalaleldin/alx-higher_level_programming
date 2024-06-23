#!/usr/bin/python3
"lists all states from the database hbtn_0e_0_usa"

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
        cur.execute("SELECT * FROM states ORDER BY states.id")
        rows = cur.fetchall()
        for row in rows:
            print(row)
        cur.close()
        conn.close()
