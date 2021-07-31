from .users import UserApi, UsersApi

def initialize_routes(api):
    api.add_resource(UserApi, '/users/<int:id>')
    api.add_resource(UsersApi, '/users')