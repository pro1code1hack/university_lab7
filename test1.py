from connection import connect_to_db, get_cursor
from menu import main_handlers

#
conn = connect_to_db()
cursor = get_cursor(conn)


def main(*args, **kwargs):
    print('1. Records')
    print('2. Users')
    print('3. Exit')
    choice = input('Enter your choice   : ')
    if choice in main_handlers:
        main_handlers[choice](*args, **kwargs)
    else:
        print('Invalid choice')
        main(*args, **kwargs)


main(cursor=cursor)
