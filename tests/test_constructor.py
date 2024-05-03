from selenium.webdriver.common.by import By
from data import UrlList
from locators import Locators
from conftest import driver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestTabsSwitching:
    # Проверка перехода во вкладку "Соусы"
    def test_go_to_sauces(self, driver):
        driver.get(UrlList.BASE_URL)
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located((By.XPATH, Locators.sauces_span)))
        driver.find_element(By.XPATH, Locators.sauces_span).click()
        active_tab = driver.find_element(By.XPATH, Locators.current_tab).text
        assert active_tab == 'Соусы'



    # Проверка перехода во вкладку "Начинки"
    def test_go_to_filling(self, driver):
        driver.get(UrlList.BASE_URL)
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located((By.XPATH, Locators.filling_span)))
        driver.find_element(By.XPATH, Locators.filling_span).click()
        active_tab = driver.find_element(By.XPATH, Locators.current_tab).text
        assert active_tab == 'Начинки'

    # Проверка перехода во вкладку "Булки" через "Начинки", так как раздел «Булки» при заходе на сайт выбраны по дефолту
    def test_go_to_buns(self, driver):
        driver.get(UrlList.BASE_URL)
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located((By.XPATH, Locators.buns_span)))
        driver.find_element(By.XPATH, Locators.buns_span)
        current_tab = "//div[contains(@class, 'current')]/span"
        active_tab = driver.find_element(By.XPATH, Locators.current_tab).text
        assert active_tab == 'Булки'