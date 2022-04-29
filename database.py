
import pymysql.cursors

class Database:

    def __init__(self):
        self.connection = pymysql.connect(host='sql.endora.cz',
            user='homeuser',
            password='Ab1122334455',
            port=3308,
            database='energydb',
            cursorclass=pymysql.cursors.DictCursor)

    def getEletricityEntries(self):
        with self.connection:
            with self.connection.cursor() as cursor:
                # Read a single record
                sql = "SELECT * FROM `eletricity` "
                cursor.execute(sql)
                result = cursor.fetchall()
                return result

