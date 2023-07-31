import json


class User:
    def __init__(self, name, user_id, access_level):
        self.name = name
        self.user_id = user_id
        self.access_level = access_level

    def load_users_json(self):
        users = set()
        with open(self, 'r') as file:
            data = json.load(file)
            for user_data in data:
                name = user_data.get('name')
                user_id = user_data.get('user_id')
                access_level = user_data.get('access_level')
                if name and user_id and access_level:
                    users.add(User(name, user_id, access_level))
        return users
