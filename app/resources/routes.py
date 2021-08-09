from resources.autentication import RegisterApi

from .autentication import LoginApi, RegisterApi
from .spendings import SpendingApi, SpendingsApi
from .users import UserApi


def initialize_routes(api):
    api.add_resource(UserApi, '/users/<int:id>')
    api.add_resource(SpendingsApi, '/users/<int:user_id>/spendings')
    api.add_resource(SpendingApi, '/users/<int:user_id>/spendings/<int:spending_id>')
    api.add_resource(RegisterApi, '/register')
    api.add_resource(LoginApi, '/login')
