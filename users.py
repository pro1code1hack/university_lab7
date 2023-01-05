import os

from db_init import db_instance


class Users:
    db_name = db_instance.db_name

    @classmethod
    def add_user(cls, db_name, *args, **kwargs):
        add_user(kwargs['cursor'])

    @classmethod
    def update_user(cls, db_name, *args, **kwargs):
        update_user(kwargs['cursor'])

    @classmethod
    def delete_user(cls, db_name, *args, **kwargs):
        delete_user(kwargs['cursor'])


def add_user(cursor):
    user_name = input('Enter user name: ')
    password = input('Enter password: ')

    sql_statement = f"""
           use {Users.db_name};
           CREATE LOGIN  {user_name} WITH PASSWORD = '{password}';
           CREATE USER {user_name} FOR LOGIN {user_name};
       """

    cursor.execute(sql_statement)
    cursor.commit()


def update_user(cursor):
    user_name = input('Enter old user name: ')
    new_user_name = input('Enter new user name: ')

    update_statement = f"""
             use {Users.db_name};
             ALTER USER {user_name} WITH NAME = {new_user_name};
         """
    cursor.execute(update_statement)
    cursor.commit()


def delete_user(cursor):
    user_name = input('Enter user name you want to delete: ')
    delete_statement = f"""
        use {Users.db_name};
        DROP USER IF EXISTS  {user_name};
    """
    cursor.execute(delete_statement)
    cursor.commit()
