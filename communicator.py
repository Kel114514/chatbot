class Communicator():
    def __init__(self, id, name='') -> None:
        self._id=id
        self._name=name

    def get_id(self) -> str:
        return self._id

    def get_user_name(self) -> str:
        return self._name

    def get_reply_header(self):
        pass


class Group(Communicator):
    def __init__(self, group_id, group_name='') -> None:
        super.__init__(group_id, group_name)


    def get_reply_header(self, params: dict={}) -> dict:
        if ('message_type' in params.keys() and params['message_type'] != 'group')\
             or ('group_id' in params.keys() and params['group_id'] != self._id):
            raise ValueError('header collision', params)
        params['message_type'] = 'group'
        params['group_id'] = self._id
        
        return params



class User(Communicator):
    def __init__(self, user_id, user_name='') -> None:
        super.__init__(user_id, user_name)



class Private_chat_user(User):
    def __init__(self, user_id, user_name='') -> None:
        super().__init__(user_id, user_name)

    def get_reply_header(self, params: dict={}) -> dict:
        if ('message_type' in params.keys() and params['message_type'] != 'private')\
             or ('user_id' in params.keys() and params['user_id'] != self._id):
            raise ValueError('header collision', params)
        params['message_type'] = 'private'
        params['user_id'] = self._id
        
        return params



class Group_chat_user(User):
    def __init__(self, group: Group, user_id, user_name='') -> None:
        super().__init__(user_id, user_name)
        self._group=group

    def get_group_id(self) -> str:
        return self._group.get_id()

    def get_reply_header(self, params: dict={}) -> dict:
        if ('message_type' in params.keys() and params['message_type'] != 'private')\
             or ('user_id' in params.keys() and params['user_id'] != self._id):
            raise ValueError('header collision', params)
        params['message_type'] = 'private'
        params['user_id'] = self._id
        
        return params


ME=Private_chat_user(1482516617, 'ケルスゥザド しょごうき')

class Namelist():
    def __init__(self) -> None:
        self._groups=set()
        self._users=set()
        self._group_users=set()
    
    def add_group(self, group: Group):
        self._groups.add(group.get_id())

    def add_user(self, user: User):
        self._users.add(user.get_id())
    
    def add_group_user(self, g_user: Group_chat_user):
        self._group_users.add((g_user.get_group_id, g_user.get_id))
    
    # raises error when the deleting target not in group
    def remove_group(self, group: Group):
        self._groups.remove(group.get_id())

    def remove_user(self, user: User):
        self._users.remove(user.get_id())
    
    def remove_group_user(self, g_user: Group_chat_user):
        self._group_users.remove((g_user.get_group_id, g_user.get_id))

    def check_group(self, group: Group):
        return group.get_id() in self._groups

    def check_user(self, user: User):
        return user.get_id() in self._users

    def check_group_user(self, g_user: Group_chat_user):
        return g_user.get_id() in self._group_users
    
    def export_data(self):
        # exports namelist data for storage
        return (self._groups, self._users, self._group_users)
    
    def import_data(groups, users, group_users) -> 'Namelist':
        nl=Namelist()
        nl._groups=groups
        nl._users=users
        nl._group_users=group_users
        return nl