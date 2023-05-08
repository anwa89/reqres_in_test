import pytest
import settings
from selenium import webdriver


@pytest.fixture() #Фикстура апи адреса
def api_url():
    return "https://reqres.in/api/"

@pytest.fixture()#Фикстура для пост запроса создание пользователя test_create_user
def user_data():#При желании можно добаваить на проверку несколькопараметров name и job
    return {"name": settings.name, "job": settings.job}

@pytest.fixture()#Фикстура для пост запроса регистра пользователя test_register_successful
def user_register():#При желании можно добаваить на проверку несколькопараметров email и password
    return {"email": settings.email, "password": settings.password}

@pytest.fixture()#Фикстура для пост запроса регистра пользователя test_register_unsuccessful
def user_register_unsuccess():#При желании можно добаваить на проверку несколькопараметров email и password
    return {"email": settings.email_1}

@pytest.fixture()#Фикстура для пост запроса login пользователя test_login_successful
def user_login():#При желании можно добаваить на проверку несколькопараметров email и password
    return {"email": settings.email_2, "password": settings.password_1}

@pytest.fixture()#Фикстура для пост запроса login пользователя test_login_unsuccessful
def user_login_unsuccess():#При желании можно добаваить на проверку несколькопараметров email и password
    return {"email": settings.email_3}

@pytest.fixture()#Фикстура для test_update
def user_update():#При желании можно добаваить на проверку несколькопараметров name и job
    return {"name": settings.name_1, "job": settings.job_1}

@pytest.fixture()#Фикстура для test_patch
def user_patch():#При желании можно добаваить на проверку несколькопараметров name и job
    return {"name": settings.name_2, "job": settings.job_2}

@pytest.fixture()
def link():
    return "https://reqres.in/"

@pytest.fixture(scope='class')
def driver():
    print("\Запуск браузера для проведения тестирования")
    driver = webdriver.Chrome()
    driver.implicitly_wait(9)
    driver.get("https://reqres.in/")
    driver.execute_script("window.scrollBy(0,1000)")
    yield driver
    print("\Тестирование закончено, браузер закрываем")
    driver.quit()