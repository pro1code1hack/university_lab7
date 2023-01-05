import os
import sys


def get_all_tables():
    db_name = os.getenv('DATABASE_NAME')
    if db_name == 'charms':
        tables = ['Charms', 'Spheres']  # TODO
    elif db_name == 'potion':
        tables = ['Ingredient', 'Recipe', 'Recipe_Ingredient']
    else:
        raise Exception('No such database')
    print("All tables:", tables)
    return tables


def get_table_information(cursor):
    tables = get_all_tables()
    table_name = input('Enter table name: ')
    if table_name not in tables:
        print('Table name is not correct')
        sys.exit()

    cursor.execute(f'SELECT * FROM {table_name}')
    columns = [column[0] for column in cursor.description]
    data_types = [column[1] for column in cursor.description]
    print(columns)
    print(data_types)
    return zip(columns, data_types), table_name


def get_list_of_new_values(cursor):
    table_information, table_name = get_table_information(cursor)
    list_of_data = []
    for column in table_information:
        print(column)
        value = input(f'Enter value for {column}: ')
        list_of_data.append(value)
    return list_of_data, table_name


def insert_data(cursor):
    list_of_new_values, table_name = get_list_of_new_values(cursor)
    print('Inserting data')

    # TODO
    insert_statement = f"""
        use {os.getenv('DATABASE_NAME')};  
        INSERT INTO {table_name}
        VALUES (?, ?, ?)
    """
    cursor.execute(insert_statement, list_of_new_values)
    cursor.commit()
    print('Data inserted')


def update_data(cursor):
    columns, table_name = get_table_information(cursor)
    columns = [column[0] for column in columns]
    new_values = get_list_of_new_values(cursor=cursor)[0]
    where_condition = input('Enter where condition: ')  # where place_of_origin = 'asfaf'
    sql = f"UPDATE {table_name} SET {columns[0]} = '{new_values[0]}', {columns[1]} = '{new_values[1]}' , {columns[2]} = '{new_values[2]}'{where_condition};"
    cursor.execute(sql)
    cursor.commit()
    print('Data updated')
    pass


def delete_data(cursor):
    get_all_tables()
    table_name = input('Enter table name: ')
    delete_condition = input('Enter condition for deleting: ')

    delete_statement = f"""
        use {os.getenv('DATABASE_NAME')};
        DELETE FROM {table_name}
        {delete_condition}
    """

    cursor.execute(delete_statement)
    cursor.commit()
