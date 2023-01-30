class User:
    def __init__(self, name, role):
        self.name = name
        self.role = role


class Access:
    __access_list = ['admin', 'developer']

    @staticmethod
    def __check_access(role):
        return role in Access.__access_list

    @staticmethod
    def get_access(user):
        if not isinstance(user, User):
            print('AccessTypeError')
        elif Access.__check_access(user.role):
            print(f'User {user.name}: success')
        else:
            print("AccessDenied")


user1 = User('batya99', 'admin')
Access.get_access(user1)  # печатает "User batya99: success"

zaya = User('milaya_zaya999', 'user')
Access.get_access(zaya)  # печатает AccessDenied

Access.get_access(5)  # печатает AccessTypeError
