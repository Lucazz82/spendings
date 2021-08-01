from .spendings import SpendingApi, SpendingsApi
from .users import UserApi, UsersApi

def initialize_routes(api):
    api.add_resource(UserApi, '/users/<int:id>')
    api.add_resource(UsersApi, '/users')
    api.add_resource(SpendingsApi, '/users/<int:user_id>/spendings')
    api.add_resource(SpendingApi, '/users/<int:user_id>/spendings/<int:spending_id>')