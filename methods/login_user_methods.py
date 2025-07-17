import allure
import requests
from data.urls import LOGIN_URL

class LoginUserMethods:
    def __init__(self):
        self.access_token = None
        self.refresh_token = None

    @allure.step('Авторизация')
    def login(self, user_data):
        response = requests.post(LOGIN_URL, user_data)
        if response.status_code == 200:
            self.refresh_token = response.json()["refreshToken"]
            self.access_token = response.json()["accessToken"]
        return response.status_code, response.json()
