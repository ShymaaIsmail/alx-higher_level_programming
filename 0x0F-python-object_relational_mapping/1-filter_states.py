#!/usr/bin/python3
""" Filter States Module"""
import sys
import MySQLdb


def filter_states():
    """Filter States"""
    host = "localhost"
    port = 3306
    user_name = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    conn = MySQLdb.connect(host=host, port=port, user=user_name,
                           passwd=password, db=database_name, charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name "
                "LIKE BINARY 'N%' ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()


if __name__ == "__main__":
    filter_states()
