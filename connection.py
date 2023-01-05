import json
import sys
import pypyodbc as odbc


class DBConnection:
    def __init__(self, db_name: str = "charms"):
        self.conn = self.connect_to_db()
        self.cursor = self.get_cursor(self.conn)
        self._db_name = db_name  # Good usage of private variable

    @property
    def db_name(self):
        return self._db_name

    @db_name.setter
    def db_name(self, value):
        self._db_name = value

    @staticmethod
    def connect_to_db():
        # driver = "SQL Server"
        server, driver = sys.argv[1], sys.argv[2]
        print("Received the following arguments: ", sys.argv[1:])

        with open('config.json', 'r+') as file:
            data = json.load(file)
            server, database = data['server'], data['database']

        conn_string = f"""Driver={{{"SQL Server"}}};Server={server};Database={database};Trust_Connection=yes;"""

        try:
            conn = odbc.connect(conn_string)
            print('connection established')
            return conn
        except Exception as e:
            print(e)
            print('HELP')
            sys.exit()

    @staticmethod
    def get_cursor(conn):
        try:
            return conn.cursor()
        except Exception as err:
            raise err

