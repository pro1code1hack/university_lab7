from menu import Menu
from records import insert_data, update_data, delete_data
from roles import create_user_roles, update_user_roles, delete_user_roles
from users import add_user, update_user, delete_user

records_handlers = {
    '1': insert_data,
    '2': update_data,
    '3': delete_data,
}

roles_handlers = {
    '1': create_user_roles,
    '2': update_user_roles,
    '3': delete_user_roles,
}

users_handlers = {
    '1': add_user,
    '2': update_user,
    '3': delete_user,
}


main_handlers = {
    '1': Menu.records_menu,
    '2': Menu.roles_menu,
    '3': Menu.users_menu,
}
