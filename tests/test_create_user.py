import allure

from data.errors import REGISTER_ERROR_NOT_UNIC_USER, REGISTER_ERROR_MISSED_REQUIRED_FIELD
from conftests import *


class TestCreateUser:
    @allure.title("Создание уникального пользователя")
    def test_create_unic_user_status_code_200(self,user_data):
        new_user = Create_User_Methods()
        status_code, json = new_user.create_new_user(user_data)
        assert status_code == 200 and json["success"] == True

    @allure.title("Создание пользователя, который уже зарегистрирован")
    def test_create_not_unic_user_status_code_403(self, new_user, user_data):
        more_new_user = Create_User_Methods()
        status_code, json = more_new_user.create_new_user(user_data)
        assert status_code == 403 and json["message"] == REGISTER_ERROR_NOT_UNIC_USER

    @allure.title("Создание пользователя с незаполненным обязательным полем")
    @pytest.mark.parametrize("not_valid_payload", [{"email": "TselykhE21@yandex.ru", "password": "1234567890"},
                                                   {"email": "TselykhE21@yandex.ru", "name": "TselykhE21"},
                                                   {"password": "1234567890","name": "TselykhE21"}])
    def test_create_user_with_one_not_required_field_status_code_403(self, not_valid_payload):
        new_user = Create_User_Methods()
        status_code, json = new_user.create_new_user(not_valid_payload)
        assert status_code == 403 and json["message"] == REGISTER_ERROR_MISSED_REQUIRED_FIELD
