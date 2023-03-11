from bottle import get,template
from bottle import get, template
import sqlite3
import g




############################## MAKES A DICTIONARY FROM SQLITE DATA
def dict_factory(cursor, row):
  col_names = [col[0] for col in cursor.description]
  return {key: value for key, value in zip(col_names, row)}
##############################



@get("/suggestions")
def _():
	try:
		db = g.db()
		users = db.execute("SELECT * FROM users ORDER BY RANDOM()").fetchall()
		trends = db.execute("SELECT * FROM trends LIMIT 5").fetchall()

		return template('to_follow',title="Who To Follow", users=users, name="Malte Skjoldager", trends=trends)
	except Exception as ex:
		print(ex)
		return ex
	finally:
		if("db" in locals()): db.close()