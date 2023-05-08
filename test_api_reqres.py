import pytest
import requests

class TestGetPositive():#Класс позитивных тестов get
    @pytest.mark.parametrize("page_number", [1, 2, 3])
    def test_get_list_users(self, api_url, page_number):
        url = f"{api_url}users?page={page_number}"
        response = requests.get(url)
        assert response.status_code == 200, "Статус кода не равен 200"
        assert "data" in response.json(), "Параметр data не найден в ответе"
        assert response.json().get("page") == page_number, "Значение страницы неверное"


    @pytest.mark.parametrize("id_user", [1, 2, 3])
    def test_get_single_user(self, api_url, id_user):
        url = f"{api_url}users/{id_user}"
        response = requests.get(url)
        assert response.status_code == 200, "Статус кода не равен 200"
        assert "data" in response.json(), "Параметр data не найден в ответе"
        assert response.json().get("data").get("id") == id_user, "Значение id пользователя неверное"


    @pytest.mark.parametrize("page_number", [1, 2, 3])
    def test_get_list_resource(self, api_url, page_number):
        url = f"{api_url}unknown?page={page_number}"
        response = requests.get(url)
        assert response.status_code == 200, "Статус кода не равен 200"
        assert "data" in response.json(), "Параметр data не найден в ответе"
        assert response.json().get("page") == page_number, "Значение страницы неверное"


    @pytest.mark.parametrize("id_resource", [1, 2, 3])
    def test_get_single_resource(self, api_url, id_resource):
        url = f"{api_url}unknown/{id_resource}"
        response = requests.get(url)
        assert response.status_code == 200, "Статус кода не равен 200"
        assert "data" in response.json(), "Параметр data не найден в ответе"
        assert response.json().get("data").get("id") == id_resource, "Значение id ресурса неверное"


    @pytest.mark.parametrize("number", [1, 2, 3])
    def test_get_delayed_response(self, api_url, number):
        url = f"{api_url}users?page={number}?delay={number}"
        response = requests.get(url)
        assert response.status_code == 200, "Статус кода не равен 200"
        assert "data" in response.json(), "Параметр data не найден в ответе"
        assert response.json().get("page") == number, "Значение id ресурса неверное"


class TestGetNegative():#Класс негативных тестов get
    @pytest.mark.parametrize("id_user", [23])
    def test_get_single_user_not_found(self, api_url, id_user):
        url = f"{api_url}users/{id_user}"
        response = requests.get(url)
        assert response.status_code == 404, "Статус кода не равен 404"
        assert "data" not in response.json(), "Параметр data не должен приходить в ответе"


    @pytest.mark.parametrize("id_resource", [23])
    def test_get_single_resource(self, api_url, id_resource):
        url = f"{api_url}unknown/{id_resource}"
        response = requests.get(url)
        assert response.status_code == 404, "Статус кода не равен 200"
        assert "data" not in response.json(), "Параметр data не должен приходить в ответе"


class TestPostPositive():#Класс позитивных тестов post
    @pytest.mark.parametrize("user_id", [1, 2, 3])
    def test_create_user(self,api_url, user_data, user_id):
        url = f"{api_url}users"
        response = requests.post(url, json=user_data)
        assert response.status_code == 201, "Статус кода не равен 201"
        user = response.json()
        assert user["name"] == user_data["name"], "Имя пользователя не соответствует ожидаемому"
        assert user["job"] == user_data["job"], "Job пользователя не соответствует ожидаемому"

    @pytest.mark.parametrize("user_id", [1, 2, 3])
    def test_register_successful(self, api_url, user_register, user_id):
        url = f"{api_url}register"
        response = requests.post(url, json=user_register)
        assert response.status_code == 200, "Статус кода не равен 200"
        user = response.json()
        assert user["id"] == 4, "email пользователя не соответствует ожидаемому"
        assert user["token"] == "QpwL5tke4Pnpja7X4", "password пользователя не соответствует ожидаемому"


    @pytest.mark.parametrize("user_id", [1, 2, 3])
    def test_login_successful(self, api_url, user_login, user_id):
        url = f"{api_url}login"
        response = requests.post(url, json=user_login)
        assert response.status_code == 200, "Статус кода не равен 200"
        user = response.json()
        assert user["token"] == "QpwL5tke4Pnpja7X4", "token пользователя не соответствует ожидаемому"


class TestNegativePost():
    @pytest.mark.parametrize("user_id", [1, 2, 3])
    def test_register_unsuccessful(self, api_url, user_register_unsuccess, user_id):
        url = f"{api_url}register"
        response = requests.post(url, json=user_register_unsuccess)
        assert response.status_code == 400, "Статус кода не равен 400"


    @pytest.mark.parametrize("user_id", [1, 2, 3])
    def test_login_unsuccessful(self, api_url, user_login_unsuccess, user_id):
        url = f"{api_url}login"
        response = requests.post(url, json=user_login_unsuccess)
        assert response.status_code == 400, "Статус кода не равен 400"


class TestPositivePut():
    def test_update(self, api_url, user_update):
        url = f"{api_url}users/2"
        response = requests.put(url, json=user_update)
        assert response.status_code == 200, "Статус кода не равен 200"
        user = response.json()
        assert user["name"] == user_update["name"], "Имя пользователя не соответствует ожидаемому"
        assert user["job"] == user_update["job"], "Job пользователя не соответствует ожидаемому"


class TestPositivePatch():
    def test_update(self, api_url, user_patch):
        url = f"{api_url}users/2"
        response = requests.put(url, json=user_patch)
        assert response.status_code == 200, "Статус кода не равен 200"
        user = response.json()
        assert user["name"] == user_patch["name"], "Имя пользователя не соответствует ожидаемому"
        assert user["job"] == user_patch["job"], "Job пользователя не соответствует ожидаемому"


class TestDelete():
    def test_delete_user(self,api_url):
        url = f"{api_url}users/2"
        response = requests.delete(url)
        # Проверяем, что удаление пользователя выполнено успешно
        assert response.status_code == 204, "Статус кода не равен 204"
        # Проверяем, что ответ пустой
        assert response.text == "", "Текст ответа не пустой"
