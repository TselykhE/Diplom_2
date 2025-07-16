import requests
from data.urls import ORDERS_URL

class GetOrderMethods:
    def __init__(self):
        self.url = ORDERS_URL

    def get_orders_list_with_auth(self, access_token):
        response = requests.get(url=self.url, headers={"authorization": access_token})
        return response.status_code, response.json()

    def get_orders_list_without_auth(self):
        response = requests.get(url=self.url)
        return response.status_code, response.json()