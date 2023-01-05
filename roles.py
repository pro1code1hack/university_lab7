import os
import sys

from records import get_all_tables


def create_user_roles(cursor):
    role_name = input('Enter role name: ')
    sql_statement = f"""
        use {os.getenv('DATABASE_NAME')};
        CREATE ROLE {role_name}
    """
    cursor.execute(sql_statement)
    cursor.commit()


def delete_user_roles(cursor):
    role_name = input('Enter role name: ')

    sql_statement = f"""
        use {os.getenv('DATABASE_NAME')};
        DROP ROLE IF EXISTS {role_name};
    """
    cursor.execute(sql_statement)
    cursor.commit()


def update_user_roles(cursor):
    role_name = input('Enter role name: ')
    # get all tables
    tables = get_all_tables()
    print('Choose the table to use:', tables)
    table = input('Enter table name: ')
    if table not in tables:
        print('Table name is not correct')
        sys.exit()

    privileges = {
        # GRANT INSERT, UPDATE, SELECT ON Сфери TO ELF;
        "admin": f"GRANT ALL PRIVILEGES ON {table} TO {role_name};",  # TODO  maybe it's solution
        "viewer": f"GRANT SELECT ON {os.getenv('DATABASE_NAME')} TO {role_name} WITH GRANT OPTION;",
        "user": f"GRANT INSERT, SELECT ON {os.getenv('DATABASE_NAME')} TO {role_name} WITH GRANT OPTION;",
        "updater": f"GRANT UPDATE, SELECT ON {os.getenv('DATABASE_NAME')} TO {role_name} WITH GRANT OPTION;"
    }

    prev_type = input(f'Enter privilege type: {list(privileges.keys())}: ')
    if prev_type not in privileges:
        print('Prev type is not correct')
        sys.exit()

    sql_statement = privileges[prev_type]
    query = f"""
     use {os.getenv('DATABASE_NAME')};
     {sql_statement}
        
    """
    cursor.execute(query)
    cursor.commit()

    print('Privileges updated')

    pass
