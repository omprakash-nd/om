import MySQLdb
db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="root",db="test")
cur = db.cursor()
cur.execute("SELECT * FROM examples")

rows = cur.fetchall()

for row in rows:
    print row
    
