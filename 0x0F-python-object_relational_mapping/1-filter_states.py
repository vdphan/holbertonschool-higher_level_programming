#!/usr/bin/python3
# lists all states with a name starting with N (upper N)
import MySQLdb


conn = MySQLdb.connect(host="localhost", port=3306,
                       user="root", passwd="root",
                       db="hbtn_0e_0_usa", charset="utf8")
cur = conn.cursor()
cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
conn.close()
