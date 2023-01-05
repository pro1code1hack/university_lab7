import os
import sys
from db_init import db_instance


class Records:
    db_name = db_instance.db_name

    @classmethod
    def insert_data(cls, *args, **kwargs):
        cursor = kwargs['cursor']
        list_of_new_values, table_name = get_list_of_new_values(cursor=cursor)
        print('Inserting data')

        insert_statement = f"""
            use {cls.db_name};  
            INSERT INTO {table_name}
            VALUES (?, ?, ?)
        
        """
        print(insert_statement)
        cursor.execute(insert_statement, list_of_new_values)
        cursor.commit()
        print('Data inserted')

    @classmethod
    def update_data(cls, *args, **kwargs):
        cursor = kwargs['cursor']
        columns, table_name = get_table_information(cursor)
        columns = [column[0] for column in columns]
        new_values = get_list_of_new_values(cursor=cursor)[0]
        where_condition = input('Enter where condition: ')  # where place_of_origin = 'asfaf'
        sql = f"UPDATE {table_name} SET {columns[0]} = '{new_values[0]}', {columns[1]} = '{new_values[1]}' , {columns[2]} = '{new_values[2]}'{where_condition};"
        cursor.execute(sql)
        cursor.commit()
        print('Data updated')
        pass

    @classmethod
    def delete_data(cls, *args, **kwargs):
        get_all_tables()
        cursor = kwargs['cursor']
        table_name = input('Enter table name: ')
        delete_condition = input('Enter condition for deleting: ')

        delete_statement = f"""
                use {cls.db_name};
                DELETE FROM {table_name}
                {delete_condition}
            """

        cursor.execute(delete_statement)
        cursor.commit()


def get_all_tables():
    db_name = db_instance.db_name
    if db_name == 'charms':
        tables = ['Charms', 'Spheres']  # TODO
    elif db_name == 'potion':
        tables = ['Ingredient', 'Recipe', 'Recipe_Ingredient']
    print("All tables:", tables)
    return tables


def print_dictionary(dictionary):
    print('-' * 50)
    for key, value in dictionary.items():
        print(f'{key} : {value}')
    print('-' * 50)


def get_table_information(cursor):
    tables = get_all_tables()
    table_name = input('Enter table name: ')
    if table_name not in tables:
        print('Table name is not correct')
        sys.exit()

    cursor.execute(f'SELECT * FROM {table_name}')
    columns = [column[0] for column in cursor.description]
    data_types = [column[1] for column in cursor.description]
    processed_data = dict(zip(columns, data_types))
    print_dictionary(processed_data)

    return zip(columns, data_types), table_name


def get_list_of_new_values(cursor):
    table_information, table_name = get_table_information(cursor)
    list_of_data = []
    for column in table_information:
        value = input(f'Enter value for {column}: ')
        list_of_data.append(value)
    return list_of_data, table_name
