from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from faker import Faker
from tests_data import Valid_Data
from tests_data import Invalid_Data
from locators import RTAutorizationLocators
from locators import RTAutorizationAllerts
from locators import RTRegistrationLocators
from locators import RTRegistrationsAllerts
import allure


fake_name = Faker().name()
fake_email = Faker().email()
fake_password = Faker().password()

@allure.story('Тесты Ростелеком')
class TestValidRegistrationRT:

    def setup(self):
        self.open()

    def open(self):
        self.driver = webdriver.Chrome('./chromedriver.exe')
        self.driver.get("https://b2c.passport.rt.ru")
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_BUTTON_REGISTER)))
        self.driver.find_element(By.ID, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_BUTTON_REGISTER).click()


    def close(self):
        self.driver.quit()

    def teardown(self):
        self.close()

    def test_base(self):
        self.driver.find_element(By.XPATH, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_FIRSTNAME).send_keys(
            Valid_Data.valid_first_name)
        self.driver.find_element(By.XPATH, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_LASTNAME).send_keys(
            Valid_Data.valid_last_name)
        self.driver.find_element(By.ID, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_NUMBER_OR_EMAIL).send_keys(
            Invalid_Data.fake_email)
        self.driver.find_element(By.ID, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_PASSWORD).send_keys(
            Invalid_Data.fake_password)
        self.driver.find_element(By.ID, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_PASSWORD_CONFIRM).send_keys(
            Invalid_Data.fake_password)
        self.driver.find_element(By.XPATH, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_BUTTON_SUBMIT).click()
        assert self.driver.find_element(By.ID, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_ENTER_CODE)

#1 (1)
    @allure.feature('Авторизация с некорректным Email')
    def test_autorization_invalid_email(self):
        self.driver.find_element(By.ID, RTAutorizationLocators.LOCATOR_RT_AUTORIZATION_USER).send_keys(
            Invalid_Data.fake_email)
        self.driver.find_element(By.ID, RTAutorizationLocators.LOCATOR_RT_AUTORIZATION_PASSWORD).send_keys(
            Invalid_Data.fake_password)
        self.driver.find_element(By.ID, RTAutorizationLocators.LOCATOR_RT_AUTORIZATION_BUTTON_LOGIN).click()
        assert self.driver.find_element(By.XPATH, RTAutorizationAllerts.LOCATOR_RT_AUTORIZATION_ALLERTS_ERROR)
        assert self.driver.find_element(By.XPATH, RTAutorizationAllerts.LOCATOR_ERROR_TEXT_INVALID_EMAIL)

# 2 (3)
    @allure.feature('Авторизация с недействительному номеру телефона')
    def test_autorization_invalid_phoneNumber(self):
        self.driver.find_element(By.ID, RTAutorizationLocators.LOCATOR_RT_AUTORIZATION_USER).send_keys(
            Invalid_Data.invalid_phoneNumber)
        self.driver.find_element(By.ID, RTAutorizationLocators.LOCATOR_RT_AUTORIZATION_PASSWORD).send_keys(
            Invalid_Data.fake_password)
        self.driver.find_element(By.ID, RTAutorizationLocators.LOCATOR_RT_AUTORIZATION_BUTTON_LOGIN).click()
        assert self.driver.find_element(By.XPATH, RTAutorizationAllerts.LOCATOR_RT_AUTORIZATION_ALLERTS_ERROR)
        assert self.driver.find_element(By.XPATH, RTAutorizationAllerts.LOCATOR_ERROR_TEXT_INVALID_EMAIL)

# 3 (7)
    @allure.feature('Регистрация с паролем более 20 символов')
    def test_registration_user_with_pass_22char(self):
        self.driver.find_element(By.XPATH, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_FIRSTNAME).send_keys(
            Valid_Data.valid_first_name)
        self.driver.find_element(By.XPATH, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_LASTNAME).send_keys(
            Valid_Data.valid_last_name)
        self.driver.find_element(By.ID, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_NUMBER_OR_EMAIL).send_keys(
            Invalid_Data.fake_email)
        self.driver.find_element(By.ID, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_PASSWORD).send_keys(
            Invalid_Data.password_22_char)
        self.driver.find_element(By.ID, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_PASSWORD_CONFIRM).send_keys(
            Invalid_Data.password_22_char)
        self.driver.find_element(By.XPATH, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_BUTTON_SUBMIT).click()
        assert self.driver.find_element(By.XPATH, RTRegistrationsAllerts.LOCATOR_RT_REGISTRATION_ALLERTS_ERROR)

# 4 (8)
    @allure.feature('Регистрация по Email с несуществующим доменом')
    def test_registration_user_with_email_without_domain(self):
        self.driver.find_element(By.XPATH, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_FIRSTNAME).send_keys(
            Valid_Data.valid_first_name)
        self.driver.find_element(By.XPATH, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_LASTNAME).send_keys(
            Valid_Data.valid_last_name)
        self.driver.find_element(By.ID, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_NUMBER_OR_EMAIL).send_keys(
            Invalid_Data.email_without_domain)
        self.driver.find_element(By.ID, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_PASSWORD).send_keys(
            Invalid_Data.fake_password)
        self.driver.find_element(By.ID, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_PASSWORD_CONFIRM).send_keys(
            Invalid_Data.fake_password)
        self.driver.find_element(By.XPATH, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_BUTTON_SUBMIT).click()
        assert self.driver.find_element(By.XPATH, RTRegistrationsAllerts.LOCATOR_RT_REGISTRATION_ALLERTS_ERROR)

# 5 (9)
    @allure.feature('Регистрация пользователя с фамилией длиной более 30 символов')
    def test_registration_user_with_laststname_32char(self):
        self.driver.find_element(By.XPATH, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_FIRSTNAME).send_keys(
            Invalid_Data.last_name_32_char)
        self.driver.find_element(By.XPATH, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_LASTNAME).send_keys(
            Valid_Data.valid_first_name)
        self.driver.find_element(By.ID, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_NUMBER_OR_EMAIL).send_keys(
            Invalid_Data.fake_email)
        self.driver.find_element(By.ID, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_PASSWORD).send_keys(
            Invalid_Data.fake_password)
        self.driver.find_element(By.ID, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_PASSWORD_CONFIRM).send_keys(
            Invalid_Data.fake_password)
        self.driver.find_element(By.XPATH, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_BUTTON_SUBMIT).click()
        assert self.driver.find_element(By.XPATH, RTRegistrationsAllerts.LOCATOR_RT_REGISTRATION_ALLERTS_ERROR)

# 6 (10)
    @allure.feature('Регистрация пользователя без указания фамилии')
    def test_registration_user_with_not_filled_lastname(self):
        self.driver.find_element(By.XPATH, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_FIRSTNAME).send_keys(
            Valid_Data.valid_first_name)
        self.driver.find_element(By.ID, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_NUMBER_OR_EMAIL).send_keys(
            Invalid_Data.fake_email)
        self.driver.find_element(By.ID, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_PASSWORD).send_keys(
            Invalid_Data.fake_password)
        self.driver.find_element(By.ID, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_PASSWORD_CONFIRM).send_keys(
            Invalid_Data.fake_password)
        self.driver.find_element(By.XPATH, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_BUTTON_SUBMIT).click()
        assert self.driver.find_element(By.XPATH, RTRegistrationsAllerts.LOCATOR_RT_REGISTRATION_ALLERTS_ERROR)

# 7 (11)
    @allure.feature('Регистрация с паролем, не содержащим обязательный символ - цифру')
    def test_registration_user_with_password_not_contain_digit(self):
        self.driver.find_element(By.XPATH, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_FIRSTNAME).send_keys(
            Valid_Data.valid_first_name)
        self.driver.find_element(By.XPATH, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_LASTNAME).send_keys(
            Valid_Data.valid_last_name)
        self.driver.find_element(By.ID, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_NUMBER_OR_EMAIL).send_keys(
            Invalid_Data.fake_email)
        self.driver.find_element(By.ID, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_PASSWORD).send_keys(
            Invalid_Data.password_not_contain_digit)
        self.driver.find_element(By.ID, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_PASSWORD_CONFIRM).send_keys(
            Invalid_Data.password_not_contain_digit)
        self.driver.find_element(By.XPATH, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_BUTTON_SUBMIT).click()
        assert self.driver.find_element(By.XPATH, RTRegistrationsAllerts.LOCATOR_RT_REGISTRATION_ALLERTS_ERROR)

# 8 (12)
    @allure.feature('Регистрация с несовпадающими паролями')
    def test_registration_user_with_non_matching_passwords(self):
        self.driver.find_element(By.XPATH, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_FIRSTNAME).send_keys(
            Valid_Data.valid_first_name)
        self.driver.find_element(By.XPATH, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_LASTNAME).send_keys(
            Valid_Data.valid_last_name)
        self.driver.find_element(By.ID, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_NUMBER_OR_EMAIL).send_keys(
            Invalid_Data.fake_email)
        self.driver.find_element(By.ID, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_PASSWORD).send_keys(
            Invalid_Data.fake_password)
        self.driver.find_element(By.ID, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_PASSWORD_CONFIRM).send_keys(
            Valid_Data.valid_password)
        self.driver.find_element(By.XPATH, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_BUTTON_SUBMIT).click()
        assert self.driver.find_element(By.XPATH, RTRegistrationsAllerts.LOCATOR_RT_REGISTRATION_ALLERTS_ERROR)





