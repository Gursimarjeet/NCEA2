import sqlite3

db = sqlite3.connect('Graphics')
cursor = db.cursor()
sql = "SELECT * FROM GraphicCardInfo;"
cursor.execute(sql)
results = cursor.fetchall()
print(results)
db.close()