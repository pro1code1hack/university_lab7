import json

import pypyodbc as odbc
import sys


def get_cursor(conn):
    try:
        return conn.cursor()
    except Exception as err:
        raise err


def write_to_file(data):
    with open('config.json', 'w') as file:
        json.dump(data, file)


def connect_to_db():
    # DRIVER={SQL Server};SERVER=localhost,58420;DATABASE=charms;UID=kvmi;PWD=kozura1337
    # driver = input('Enter driver: ')
    # server = input('Enter server: ')
    # database = input('Enter database: ')

    # TODO parse data from the command line
    driver = "SQL Server"
    server = 'DESKTOP-2K4F8IK\SQLEXPRESS'
    database = 'charms'

    write_to_file({"driver": driver, "server": server, "database": database})

    print('The argument values are:', driver, server, database)

    conn_string = f"""
        Driver= {driver};
        Server= {server};
        Database= {database};
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
