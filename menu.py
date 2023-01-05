from handlers import records_handlers, users_handlers, roles_handlers


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

    def roles_menu(*args, **kwargs):
        print('1. Create', '2. Update', '3. Delete', sep='\n')
        choice = input('Enter your choice: ')
        if choice in roles_handlers:
            roles_handlers[choice](*args, **kwargs)
        else:
            print('Invalid choice')


