import MySQLdb

class BaseDao:
    def __init__(self):
        # conectando BD
        self.conn = MySQLdb.connect(
            host='mysql.topskills.study', database='topskills04', user='topskills04', passwd='Elenice2019')
        self.cursor = self.conn.cursor()

  