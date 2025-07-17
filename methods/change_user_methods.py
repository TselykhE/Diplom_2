import allure

from data.urls import USER_URL
import requests


class ChangeUserMethods:
    def __init__(self, access_token):
        self.access_token = access_token
        self.access_token_payload = {"authorization": self.access_token}

    @allure.step('Удаление пользователя')
    def delete_user(self):
        response = requests.delete(url=USER_URL, headers=self.access_token_payload)
        return response.status_code, response.json()

    @allure.step('Смена пользователя с авторизацией')
    def change_user_with_auth(self, new_data):
        response = requests.patch(url=USER_URL, headers=self.access_token_payload, data=new_data)
        return response.status_code, response.json()

    @allure.step('Смена пользователя без авторизации')
    def change_user_without_auth(self, new_data):
        response = requests.patch(url=USER_URL, data=new_data)
        return response.status_code, response.json()
