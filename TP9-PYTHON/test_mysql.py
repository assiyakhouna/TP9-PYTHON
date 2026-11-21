from mysql_dao import MySQLDAO

db = MySQLDAO()
db.conn.close()

print("Test terminé avec succès !")