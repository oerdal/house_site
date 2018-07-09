# class which retrieves table data from csv
from collectList import activeListCollector
# python postgresql package
import psycopg2
# host, db, user fields for db connection
from constants import host, db, user
# get table data as list of lists
table = activeListCollector('activehouse.csv').getList()
# hostname - the host where the db is running
# dbname - name of the databse
# user - user accessing database
conn = psycopg2.connect("host=" + host + " dbname=" + db + " user=" + user)
cur = conn.cursor()
# remove table if exists
cur.execute("DROP TABLE IF EXISTS roster")
# recreate table
cur.execute("""
CREATE TABLE roster(
    name text PRIMARY KEY,
    status text,
    class text,
    quarter text
)
""")
# iterate through rows of table, insert each row into database
for row in table:
    cur.execute("INSERT INTO roster VALUES (%s, %s, %s, %s)", (row["name"], row["status"], row["class"], row["quarter"]))
# commit current transaction to db 
conn.commit()