#!/usr/bin/python3
""" Safe Filter States Module"""
import sys
import MySQLdb


def safe_filter_states():
    """Safe Filter States"""
    host = "localhost"
    port = 3306
    user_name = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    name = sys.argv[4]
    conn = MySQLdb.connect(host=host, port=port, user=user_name,
                           passwd=password, db=database_name, charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name = %s ORDER BY id ASC",
                (name,))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()


if __name__ == "__main__":
    safe_filter_states()
