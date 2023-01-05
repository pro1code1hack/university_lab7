import os


def add_user(cursor):
    user_name = input('Enter user name: ')
    password = input('Enter password: ')

    sql_statement = f"""
           use {os.getenv('DATABASE_NAME')};
           CREATE LOGIN  {user_name} WITH PASSWORD = '{password}';
           CREATE USER {user_name} FOR LOGIN {user_name};
       """

    cursor.execute(sql_statement)
    cursor.commit()


def update_user(cursor):
    user_name = input('Enter old user name: ')
    new_user_name = input('Enter new user name: ')

    update_statement = f"""
             use {os.getenv('DATABASE_NAME')};
             ALTER USER {user_name} WITH NAME = {new_user_name};
         """
    cursor.execute(update_statement)
    cursor.commit()


def delete_user(cursor):
    user_name = input('Enter user name you want to delete: ')
    delete_statement = f"""
        use {os.getenv('DATABASE_NAME')};
        DROP USER IF EXISTS  {user_name};
    """
    cursor.execute(delete_statement)
    cursor.commit()
