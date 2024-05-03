from data import Data, UrlList
import pytest
from locators import Locators
from conftest import driver
import helper_functions
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class TestRegistration:
    # Проверка успешной регистрации рандомного пользователя
    def test_registration_successful(self, driver):
        driver.get(UrlList.REG_PAGE_URL)
        driver.find_element(*Locators.input_name_field).send_keys(helper_functions.random_name())
        driver.find_element(*Locators.input_email_field).send_keys(helper_functions.random_email())
        driver.find_element(*Locators.input_password_field).send_keys(helper_functions.random_password())
        driver.find_element(*Locators.registration_button).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.login_account_auth_form_but))
        login_button_displayed = driver.find_element(*Locators.login_account_auth_form_but).is_displayed()

        assert driver.current_url == UrlList.AUTH_PAGE_URL and login_button_displayed


    # Проверка регистрации при вводе пароля менее 6 символов, гз 1 и 5 символов
    @pytest.mark.parametrize('password', ['t', 'Test4'])
    def test_registration_password_less_6_synbols(self, driver, password):
        driver.get(UrlList.REG_PAGE_URL)
        driver.find_element(*Locators.input_name_field).send_keys(helper_functions.random_name())
        driver.find_element(*Locators.input_email_field).send_keys(helper_functions.random_email())
        driver.find_element(*Locators.input_password_field).send_keys(password)
        driver.find_element(*Locators.registration_button).click()
        WebDriverWait(driver, 6).until(expected_conditions.visibility_of_element_located(Locators.incorrect_password_message))

        assert driver.find_element(*Locators.incorrect_password_check).text == 'Некорректный пароль'

    # Проверка регистрации пользователя с некорректным email
    @pytest.mark.parametrize('email', [helper_functions.mail_with_name_only(), helper_functions.mail_with_error_domain()])
    def test_registration_with_incorrect_email(self, driver, email):
        driver.get(UrlList.REG_PAGE_URL)
        driver.find_element(*Locators.input_name_field).send_keys(helper_functions.random_name())
        driver.find_element(*Locators.input_email_field).send_keys(email)
        driver.find_element(*Locators.input_password_field).send_keys(helper_functions.random_password())
        driver.find_element(*Locators.registration_button).click()
        WebDriverWait(driver, 6).until(expected_conditions.visibility_of_element_located(Locators.user_exists_message))

        assert driver.find_element(*Locators.user_exists_check).text == 'Такой пользователь уже существует'

     # Проверка регистрации ранее зарегистрированного пользователя
    def test_registration_with_exist_user(self, driver):
        driver.get(UrlList.REG_PAGE_URL)
        driver.find_element(*Locators.input_name_field).send_keys(Data.name)
        driver.find_element(*Locators.input_email_field).send_keys(Data.email)
        driver.find_element(*Locators.input_password_field).send_keys(Data.password)
        driver.find_element(*Locators.registration_button).click()
        WebDriverWait(driver, 6).until(expected_conditions.visibility_of_element_located(Locators.user_exists_message))

        assert driver.find_element(*Locators.user_exists_check).text == 'Такой пользователь уже существует'