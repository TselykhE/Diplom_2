import requests
from data.urls import ORDERS_URL

class CreateOrderMethods:
    def __init__(self):
        self.url = ORDERS_URL

    def create_order_without_auth(self, ingredients):
        response = requests.post(url=self.url, data={"ingredients": ingredients})
        return response.status_code, response.json()

    def create_order_with_auth(self, access_token, ingredients):
        response = requests.post(url=self.url, headers={"authorization": access_token}, data={"ingredients": ingredients})
        return response.status_code, response.json()
