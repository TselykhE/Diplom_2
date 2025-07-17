import allure

from methods.create_order_methods import CreateOrderMethods
from data.ingredients_id import *
from data.errors import ORDER_WITH_WRONG_INGREDIENT, ORDER_WITHOUT_INGREDIENTS
from conftests import *

class TestCreateOrders:
    @allure.title("Создание заказа c авторизацией + создание заказа с ингредиентами")
    @pytest.mark.parametrize("ingredients_list", [BUN, MAIN, SAUCE, [BUN, MAIN, SAUCE]])
    def test_create_order_with_auth_status_code_200(self, new_user, ingredients_list):
        order = CreateOrderMethods()
        status_code, json = order.create_order_with_auth(new_user.access_token, ingredients_list)
        assert status_code == 200 and json["success"] == True

    @allure.title("Создание заказа без авторизации")
    def test_create_order_without_auth_status_code_200(self):
        order = CreateOrderMethods()
        status_code, json = order.create_order_without_auth([BUN, MAIN])
        assert status_code == 200 and json["success"] == True

    @allure.title("Создание заказа без ингредиентов")
    def test_create_order_without_ingredients_status_code_400(self):
        order = CreateOrderMethods()
        status_code, json = order.create_order_without_auth([])
        assert status_code == 400 and json["message"] == ORDER_WITHOUT_INGREDIENTS

    @allure.title("Создание заказа с невалидным ингредиентом")
    def test_create_order_with_wrong_id_ingredient_status_code_400(self):
        order = CreateOrderMethods()
        status_code, json = order.create_order_without_auth([WRONG])
        assert status_code == 400 and json["message"] == ORDER_WITH_WRONG_INGREDIENT
