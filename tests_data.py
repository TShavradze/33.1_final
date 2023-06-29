from faker import Faker

class Invalid_Data:
    fake_email = Faker().email()
    fake_password = Faker().password()
    fake_name = Faker().name()
    last_name_32_char = 'Sandwinddddddddddddddddddddddddd'
    password_22_char = 'tamtamtamtamtamtamtamm'
    password_not_contain_digit = "Queen"
    email_without_domain = 'test@.ru'
    invalid_phoneNumber = '+79991111111'

class Valid_Data:
    valid_first_name = 'Анна'
    valid_last_name = 'Болейн'
    valid_password = 'Queen2'
    valid_phoneNumber = '+79161234567'