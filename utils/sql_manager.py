import pymysql

class SqlManager():

    def __init__(self):
        self.conn = pymysql.connect(host='localhost',
                                    user='root',
                                    password='123456',
                                    port=3306,
                                    database='test',
                                    )


        def get_data_from_table(self, tag_value='*',table='',column='',limit=''):
            if limit:
                query = f"select {tag_value} from {table} where {column}='{limit}'"
            else:
                query = f'select {tag_value} from  {table};'
            cursor = self.conn.cursor()
            cursor.execute(query)
            result=cursor.fetchall()
            return result



sql_manager = SqlManager()
