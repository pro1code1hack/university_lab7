import db_init
from menu import main_handlers


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


main(cursor=db_init.db_instance.cursor)
