import allure
import requests
from data.urls import REGISTER_URL


class Create_User_Methods:

    def __init__(self):
        self.access_token = None
        self.refresh_token = None

    @allure.step('Создание нового пользователя')
    def create_new_user(self, user_data):
        response = requests.post(REGISTER_URL, user_data)
        if response.status_code == 200:
            self.refresh_token = response.json()["refreshToken"]
            self.access_token = response.json()["accessToken"]
        return response.status_code, response.json()
