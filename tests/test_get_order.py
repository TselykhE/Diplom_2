import allure
from methods.get_order_methods import GetOrderMethods
from methods.login_user_methods import LoginUserMethods
from data.userdata import USER_WITH_ORDERS_DATA
from data.errors import GET_ORDER_LIST_WITHOUT_AUTH

class TestGetOrder:

    @allure.title("Получение заказов авторизованного пользователя")
    def test_get_order_list_with_auth_status_code_200(self):
        login_user = LoginUserMethods()
        login_user.login(USER_WITH_ORDERS_DATA)
        status_code, json = GetOrderMethods().get_orders_list_with_auth(login_user.access_token)
        assert status_code == 200 and json["success"], print(json)

    @allure.title("Получение заказов неавторизованного пользователя")
    def test_get_order_list_without_auth_status_code_200(self):
        orders = GetOrderMethods()
        status_code, json = orders.get_orders_list_without_auth()
        assert status_code == 401 and json["message"] == GET_ORDER_LIST_WITHOUT_AUTH, print(json)
