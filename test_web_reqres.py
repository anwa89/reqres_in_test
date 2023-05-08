import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestWeb():
    def test_list_users(self, driver, link):
        driver.find_element(By.CSS_SELECTOR, ".active").click()
        status_code = driver.find_element(By.CSS_SELECTOR, ".response-code").text
        response_text = driver.find_element(By.CSS_SELECTOR, ".response > pre").text
        assert status_code == "200", 'Статус код не 200'
        assert "data" in response_text, "Параметр data не найден в ответе"



    def test_single_user(self, driver, link):
        driver.find_element(By.CSS_SELECTOR, ".endpoints li:nth-child(2)").click()
        status_code = driver.find_element(By.CSS_SELECTOR, ".response-code").text
        response_text = driver.find_element(By.CSS_SELECTOR, ".response > pre").text
        assert status_code == "200", 'Статус код не 200'
        assert "data" in response_text, "Параметр data не найден в ответе"


    def test_single_user_not_found(self, driver, link):
        driver.find_element(By.CSS_SELECTOR, ".endpoints li:nth-child(3)").click()
        status_code = driver.find_element(By.CSS_SELECTOR, ".response-code").text
        response_text = driver.find_element(By.CSS_SELECTOR, ".response > pre").text
        assert status_code == "404", 'Статус код не 404'
        assert "data" not in response_text, "Параметр data найден в ответе"


    def test_list_resource(self, driver, link):
        driver.find_element(By.CSS_SELECTOR, "li:nth-child(4)").click()
        status_code = driver.find_element(By.CSS_SELECTOR, ".response-code").text
        response_text = driver.find_element(By.CSS_SELECTOR, ".response > pre").text
        assert status_code == "200", 'Статус код не 200'
        assert "data" in response_text, "Параметр data не найден в ответе"


    def test_single_resource(self, driver, link):
        driver.find_element(By.CSS_SELECTOR, "li:nth-child(5)").click()
        status_code = driver.find_element(By.CSS_SELECTOR, ".response-code").text
        response_text = driver.find_element(By.CSS_SELECTOR, ".response > pre").text
        assert status_code == "200", 'Статус код не 200'
        assert "data" in response_text, "Параметр data не найден в ответе"


    def test_single_resource_not_found(self, driver, link):
        driver.find_element(By.CSS_SELECTOR, "li:nth-child(6)").click()
        status_code = driver.find_element(By.CSS_SELECTOR, ".response-code").text
        response_text = driver.find_element(By.CSS_SELECTOR, ".response > pre").text
        assert status_code == "404", 'Статус код не 404'
        assert "data" not in response_text, "Параметр data найден в ответе"


    def test_create(self, driver, link):
        driver.find_element(By.CSS_SELECTOR, "li:nth-child(7)").click()
        status_code = driver.find_element(By.CSS_SELECTOR, ".response-code").text
        response_text = driver.find_element(By.CSS_SELECTOR, ".response > pre").text
        assert status_code == "201", 'Статус код не 201'
        assert "name" in response_text, "Параметр name не найден в ответе"


    def test_update(self, driver, link):
        driver.find_element(By.CSS_SELECTOR, "li:nth-child(8)").click()
        status_code = driver.find_element(By.CSS_SELECTOR, ".response-code").text
        response_text = driver.find_element(By.CSS_SELECTOR, ".response > pre").text
        assert status_code == "200", 'Статус код не 200'
        assert "name" in response_text, "Параметр name не найден в ответе"


    def test_path_update(self, driver, link):
        driver.find_element(By.CSS_SELECTOR, "li:nth-child(9)").click()
        status_code = driver.find_element(By.CSS_SELECTOR, ".response-code").text
        response_text = driver.find_element(By.CSS_SELECTOR, ".response > pre").text
        assert status_code == "200", 'Статус код не 200'
        assert "name" in response_text, "Параметр name не найден в ответе"


    def test_delete(self, driver, link):
        driver.find_element(By.CSS_SELECTOR, "li:nth-child(10)").click()
        status_code = driver.find_element(By.CSS_SELECTOR, ".response-code").text
        response_text = driver.find_element(By.CSS_SELECTOR, ".response > pre").text
        assert status_code == "204", 'Статус код не 204'
        assert "data" not in response_text, "Параметр data найден в ответе"


    def test_register_successful(self, driver, link):
        driver.find_element(By.CSS_SELECTOR, "li:nth-child(11)").click()
        status_code = driver.find_element(By.CSS_SELECTOR, ".response-code").text
        response_text = driver.find_element(By.CSS_SELECTOR, ".response > pre").text
        assert status_code == "200", 'Статус код не 200'
        assert "id" in response_text, "Параметр id не найден в ответе"


    def test_register_unsuccessful(self, driver, link):
        driver.find_element(By.CSS_SELECTOR, "li:nth-child(12)").click()
        status_code = driver.find_element(By.CSS_SELECTOR, ".response-code").text
        response_text = driver.find_element(By.CSS_SELECTOR, ".response > pre").text
        assert status_code == "400", 'Статус код не 400'
        assert "data" not in response_text, "Параметр data  найден в ответе"


    def test_login_successful(self, driver, link):
        driver.find_element(By.CSS_SELECTOR, "li:nth-child(13)").click()
        status_code = driver.find_element(By.CSS_SELECTOR, ".response-code").text
        response_text = driver.find_element(By.CSS_SELECTOR, ".response > pre").text
        assert status_code == "200", 'Статус код не 200'
        assert "token" in response_text, "Параметр token не найден в ответе"


    def test_login_unsuccessful(self, driver, link):
        driver.find_element(By.CSS_SELECTOR, "li:nth-child(14)").click()
        status_code = driver.find_element(By.CSS_SELECTOR, ".response-code").text
        response_text = driver.find_element(By.CSS_SELECTOR, ".response > pre").text
        assert status_code == "400", 'Статус код не 400'
        assert "data" not in response_text, "Параметр data найден в ответе"

    def test_delayed_response(self, driver, link):
        driver.find_element(By.CSS_SELECTOR, "li:nth-child(15)").click()
        status_code = driver.find_element(By.CSS_SELECTOR, ".response-code").text
        response_text = driver.find_element(By.CSS_SELECTOR, ".response > pre").text
        assert status_code == "200", 'Статус код не 200'
        assert "data" in response_text, "Параметр data не найден в ответе"

