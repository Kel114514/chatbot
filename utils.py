class user():
    def __init__(self, user_id, user_name) -> None:
        self._user_id=user_id
        self._user_name=user_name

    def get_user_id(self) -> str:
        return self._user_id

    def get_user_name(self) -> str:
        return self._user_name

    def get_reply_header(self):
        pass


class private_chat_user(user):
    def __init__(self, user_id, user_name) -> None:
        super().__init__(user_id, user_name)

    def get_reply_header(self, params: dict={}) -> dict:
        if ('message_type' in params.keys() and params['message_type'] != 'private')\
             or ('user_id' in params.keys() and params['user_id'] != self._user_id):
            raise ValueError('header collision', params)
        params['message_type'] = 'private'
        params['user_id'] = self._user_id
        
        return params



class group_chat_user(user):
    def __init__(self, group_id, user_id, user_name) -> None:
        super().__init__(user_id, user_name)
        self._group_id=group_id

    def get_group_id(self) -> str:
        return self._group_id

    def get_reply_header(self, params: dict={}) -> dict:
        if ('message_type' in params.keys() and params['message_type'] != 'private')\
             or ('user_id' in params.keys() and params['user_id'] != self._user_id):
            raise ValueError('header collision', params)
        params['message_type'] = 'private'
        params['user_id'] = self._user_id
        
        return params