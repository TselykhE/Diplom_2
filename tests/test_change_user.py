import allure
from methods.change_user_methods import ChangeUserMethods
from data.errors import USER_NOT_AUTH
from data.userdata import CHANGE_DATA
from conftests import*


class TestChangeUser:
    @allure.title("Изменение данных пользователя с авторизацией")
    @pytest.mark.parametrize("change_param", ["email", "password", "name"])
    def test_change_login_user_status_code_200(self, new_user, change_param):
        test_user = ChangeUserMethods(new_user.access_token)
        status_code, json = test_user.change_user_with_auth({change_param: CHANGE_DATA})
        assert status_code == 200 and json["success"] == True, print(status_code, json)

    @allure.title("Изменение данных пользователя без авторизации")
    @pytest.mark.parametrize("change_param", ["email", "password", "name"])
    def test_change_not_login_user_status_code_401(self, new_user, change_param):
        test_user = ChangeUserMethods(new_user.access_token)
        status_code, json = test_user.change_user_without_auth({change_param: CHANGE_DATA})
        assert status_code == 401 and json["message"] == USER_NOT_AUTH, print(status_code, json)
