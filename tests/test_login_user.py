from methods.login_user_methods import LoginUserMethods
from data.userdata import LOGIN_DATA_WRONG_EMAIL, LOGIN_DATA_WRONG_PASS
from data.errors import LOGIN_ERROR_NOT_VALID_DATA
import allure
from conftests import *

class TestLoginUser:
    @allure.title("Логин под существующим пользователем")
    def test_login_with_valid_user_status_code_200(self, new_user,user_data):
        login_user = LoginUserMethods()
        status_code, json = login_user.login(user_data)
        assert status_code == 200 and json["success"] == True

    @allure.title("Логин с неверным логином и паролем")
    @pytest.mark.parametrize("wrong_logout_data", [LOGIN_DATA_WRONG_EMAIL, LOGIN_DATA_WRONG_PASS])
    def test_login_with_wrong_data_status_code_401(self, wrong_logout_data):
        user = LoginUserMethods()
        status_code, json = user.login(wrong_logout_data)
        assert status_code == 401 and json["message"] == LOGIN_ERROR_NOT_VALID_DATA
