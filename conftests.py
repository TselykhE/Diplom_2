import pytest

from methods.change_user_methods import ChangeUserMethods
from methods.create_user_methods import Create_User_Methods
from helper import*

@pytest.fixture()
def user_data():
    return {
        "email": create_data(),
        "password": "tselykh2112345",
        "name": "tselykh21"
    }

@pytest.fixture
def new_user(user_data):
    user = Create_User_Methods()
    user.create_new_user(user_data)
    yield user
    ChangeUserMethods(user.access_token).delete_user()
