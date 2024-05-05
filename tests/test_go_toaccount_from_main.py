from data import Data, UrlList
from locators import Locators
from conftest import driver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait



class TestPersonalAccount:
    # Проверка перехода по клику на «Личный кабинет» с главной страницы
    def test_go_to_account_from_main(self, driver):
        driver.get(UrlList.BASE_URL)
        driver.find_element(*Locators.login_button_main).click()
        driver.find_element(*Locators.input_email_field).send_keys(Data.email)
        driver.find_element(*Locators.input_password_field).send_keys(Data.password)
        driver.find_element(*Locators.login_button_login_page).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(Locators.order_button))

        driver.find_element(*Locators.personal_account_button).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(Locators.profile_link))

        assert driver.find_element(*Locators.profile_link)