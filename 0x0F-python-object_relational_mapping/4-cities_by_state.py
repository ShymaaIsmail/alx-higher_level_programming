#!/usr/bin/python3
""" SELECT ALL cities Module"""
import sys
import MySQLdb


def select_cities():
    """SELECT ALL cities"""
    host = "localhost"
    port = 3306
    user_name = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    conn = MySQLdb.connect(host=host, port=port, user=user_name,
                           passwd=password, db=database_name, charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name "
                "FROM cities JOIN states ON cities.state_id = states.id "
                "ORDER BY cities.id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()


if __name__ == "__main__":
    select_cities()
