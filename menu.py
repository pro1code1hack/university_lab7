from records import Records
from users import add_user, update_user, delete_user

records_handlers = {
    '1': Records.insert_data,
    '2': Records.update_data,
    '3': Records.delete_data,
}

users_handlers = {
    '1': add_user,
    '2': update_user,
    '3': delete_user,
}


class Menu:

    def __init__(self, cursor):
        self.cursor = cursor

    def records_menu(*args, **kwargs):
        print('1. Insert', '2. Update', '3. Delete', sep='\n')
        choice = input('Enter your choice: ')
        if choice in records_handlers:
            records_handlers[choice](*args, **kwargs)
        else:
            print('Invalid choice')

    def users_menu(*args, **kwargs):
        print('1. Add', '2. Update', '3. Delete', sep='\n')
        choice = input('Enter your choice: ')
        if choice in users_handlers:
            users_handlers[choice](*args, **kwargs)
        else:
            print('Invalid choice')


main_handlers = {
    '1': Menu.records_menu,
    '2': Menu.users_menu,
}
