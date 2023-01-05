import os
import sys
import pypyodbc as odbc
import sys


def get_cursor(conn):
    try:
        return conn.cursor()
    except Exception as err:
        raise err


def connect_to_db():

    #driver = input('Enter driver: ')
    #server = input('Enter server: ')
    #database = input('Enter database: ')

    print('The argument values are:', str(sys.argv))

    conn_string = f"""
        Driver={{{os.getenv('DRIVER')}}};
        Server={os.getenv('SERVER_NAME')};
        Database={os.getenv('DATABASE_NAME')};
        Trust_Connection=yes;
    """

    try:
        conn = odbc.connect(conn_string)
        print('connection established')
        return conn
    except Exception as e:
        print(e)
        print('task is terminated aaaaa')
        sys.exit()
