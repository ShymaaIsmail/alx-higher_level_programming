#!/usr/bin/python3
""" Filter cities By state name Module"""
import sys
import MySQLdb


def filter_cities():
    """Filter cities By state name"""
    host = "localhost"
    port = 3306
    user_name = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]
    conn = MySQLdb.connect(host=host, port=port, user=user_name,
                           passwd=password, db=database_name, charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT cities.name "
                "FROM cities JOIN states ON cities.state_id = states.id "
                "WHERE states.name = %s"
                "ORDER BY cities.id ASC", (state_name,))
    query_rows = cur.fetchall()
    formatted_result = ', '.join([row[0] for row in query_rows])
    print(formatted_result)

    cur.close()
    conn.close()


if __name__ == "__main__":
    filter_cities()
