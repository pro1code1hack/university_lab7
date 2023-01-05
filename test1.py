from connection import connect_to_db, get_cursor
from handlers import main_handlers

#
conn = connect_to_db()
cursor = get_cursor(conn)


def menu(*args, **kwargs):
    print('1. Records')
    print('2. Roles')
    print('3. Users')
    print('4. Exit')
    choice = input('Enter your choice: ')
    if choice in main_handlers:
        main_handlers[choice](*args, **kwargs)
    else:
        print('Invalid choice')
        menu()


menu(cursor=cursor)
