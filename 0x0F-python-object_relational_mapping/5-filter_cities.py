#!/usr/bin/python3
""" script that takes in an argument and displays all values """

if __name__ == '__main__':
    from sys import argv
    import MySQLdb

    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])

    cur = db.cursor()
    cur.execute("""SELECT cities.name FROM states
                JOIN cities ON cities.state_id = states.id
                WHERE states.name = %s""", (argv[4],))
    rows = cur.fetchall()
    city = 0
    for row in rows:
        if city != 0:
            print(end=", ")
        print("%s" % row, end="")
        city += 1
    cur.close()
    db.close()
