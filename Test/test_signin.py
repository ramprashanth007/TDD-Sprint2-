# 11 Test cases to do


import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from PageObjects.signin import SigninPage


@pytest.mark.usefixtures("starter")
class TestSignin:

    # 1 Signup using invalid mobile number. ('1122334456') (NOT ASSERTED)

    def test_signup_using_invalid_mobile_number_illegal_input(self):  # THE REAL BUG
        signin = SigninPage(self.driver)
        time.sleep(3)
        signin.click_on_login_button()  # login button
        time.sleep(3)
        signin.click_on_create_your_account()  # Create your account
        time.sleep(3)
        signin.click_on_india_dropdown()  # India dropdown
        time.sleep(3)
        signin.india_select()  # India select
        time.sleep(3)
        signin.enter_invalid_creds_1()  # enter value
        time.sleep(3)
        signin.click_on_the_continue_button()  # continue click
        time.sleep(10)
        # assert driver.find_element(By.XPATH,"//p[@class='css-5piwwz-StyledP2 ena7kom0']").text.__eq__("Phone number is not valid")
        assert signin.assertion_logic()


    # 2 Signup using invalid mobile number. ('0000000000')

    def test_signup_using_invalid_mobile_number_0000000000(self):
        signin = SigninPage(self.driver)
        time.sleep(3)
        signin.click_on_login_button()  # login button
        time.sleep(3)
        signin.click_on_create_your_account()  # Create your account
        time.sleep(3)
        signin.click_on_india_dropdown()  # India dropdown
        time.sleep(3)
        signin.india_select()  # India select
        time.sleep(3)
        signin.enter_invalid_creds_2()  # Enter value
        time.sleep(3)
        signin.click_on_the_continue_button()  # continue click
        time.sleep(5)
        assert signin.assertion_2()

    # 3 Signup using invalid mobile number. ('no data')

    def test_signup_using_invalid_mobile_number_no_data(self):
        signin = SigninPage(self.driver)
        time.sleep(3)
        signin.click_on_login_button()  # login button
        time.sleep(3)
        signin.click_on_create_your_account()  # Create your account
        time.sleep(3)
        signin.click_on_india_dropdown()  # India dropdown
        time.sleep(3)
        signin.india_select()  # India select
        time.sleep(3)
        signin.enter_invalid_creds_3()
        time.sleep(3)
        signin.click_on_the_continue_button()  # continue click
        time.sleep(3)
        assert signin.assertion_3().__eq__("Join Unacademy")

    # 4 Signup using invalid mobile number. ('1') (minimum cred)

    def test_signup_using_invalid_mobile_number_min_cred(self):
        signin = SigninPage(self.driver)
        time.sleep(3)
        signin.click_on_login_button()  # login button
        time.sleep(3)
        signin.click_on_create_your_account()  # Create your account
        time.sleep(3)
        signin.click_on_india_dropdown()  # India dropdown
        time.sleep(3)
        signin.india_select()  # India select
        time.sleep(3)
        signin.enter_invalid_creds_4()
        time.sleep(3)
        signin.click_on_the_continue_button()  # continue click
        time.sleep(5)
        assert signin.assertion_4() .__eq__("Join Unacademy")

# 5 Signup using invalid mobile number. ('11111aaaaa') (Alphanumeric)

    def test_signup_using_invalid_mobile_number_alphanum(self):
        signin = SigninPage(self.driver)
        time.sleep(3)
        signin.click_on_login_button()  # login button
        time.sleep(3)
        signin.click_on_create_your_account()  # Create your account
        time.sleep(3)
        signin.click_on_india_dropdown()  # India dropdown
        time.sleep(3)
        signin.india_select()  # India select
        time.sleep(3)
        signin.enter_invalid_creds_5()
        time.sleep(3)
        signin.click_on_the_continue_button()  # continue click
        time.sleep(5)
        assert signin.assertion_5().__eq__("Join Unacademy")

# 6 Signup using invalid mobile number. ('aaa!!!@@@b') (Alphabets and special characters)

    def test_signup_using_invalid_mobile_number_alpha_splcha(self):
        signin = SigninPage(self.driver)
        time.sleep(3)
        signin.click_on_login_button()  # login button
        time.sleep(3)
        signin.click_on_create_your_account()  # Create your account
        time.sleep(3)
        signin.click_on_india_dropdown()  # India dropdown
        time.sleep(3)
        signin.india_select()  # India select
        time.sleep(3)
        signin.enter_invalid_creds_6()
        time.sleep(3)
        signin.click_on_the_continue_button()  # continue click
        time.sleep(5)
        assert signin.assertion_6().__eq__("Join Unacademy")

# 7 Signup using invalid mobile number. ('111!!!@@@2') (Number and special characters)

    def test_signup_using_invalid_mobile_number_num_splcha(self):
        signin = SigninPage(self.driver)
        time.sleep(3)
        signin.click_on_login_button()  # login button
        time.sleep(3)
        signin.click_on_create_your_account()  # Create your account
        time.sleep(3)
        signin.click_on_india_dropdown()  # India dropdown
        time.sleep(3)
        signin.india_select()  # India select
        time.sleep(3)
        signin.enter_invalid_creds_7()
        time.sleep(3)
        signin.click_on_the_continue_button()  # continue click
        time.sleep(5)
        assert signin.assertion_7().__eq__("Join Unacademy")

# 8 Signup using valid mobile number. ('9600415148') (Valid credentials)

    def test_signup_using_valid_mobile_number(self):
        signin = SigninPage(self.driver)
        time.sleep(3)
        signin.click_on_login_button()  # login button
        time.sleep(3)
        signin.click_on_create_your_account()  # Create your account
        time.sleep(3)
        signin.click_on_india_dropdown()  # India dropdown
        time.sleep(3)
        signin.india_select()  # India select
        time.sleep(3)
        signin.enter_valid_creds_8()
        time.sleep(3)
        signin.click_on_the_continue_button()  # continue click
        time.sleep(5)
        assert signin.assertion_8().__eq__("Verify your mobile number")

# 9 Signup using invalid creds. ('no data') (OTP iterations)

    def test_signup_using_valid_mobile_number_invalid_OTP_1(self):
        signin = SigninPage(self.driver)
        time.sleep(3)
        signin.click_on_login_button()  # login button
        time.sleep(3)
        signin.click_on_create_your_account()  # Create your account
        time.sleep(3)
        signin.click_on_india_dropdown()  # India dropdown
        time.sleep(3)
        signin.india_select()  # India select
        time.sleep(3)
        signin.enter_valid_creds_8()
        time.sleep(3)
        signin.click_on_the_continue_button()  # continue click
        time.sleep(5)
        signin.enter_invalid_otp_1()
        time.sleep(3)
        signin.click_on_otp_submit_button()
        time.sleep(3)
        assert signin.assertion_8().text.__eq__("Verify your mobile number")

# 10 Signup using invalid creds. ('111111') (OTP iterations)

    def test_signup_using_valid_mobile_number_invalid_OTP_2(self):
        signin = SigninPage(self.driver)
        time.sleep(3)
        signin.click_on_login_button()  # login button
        time.sleep(3)
        signin.click_on_create_your_account()  # Create your account
        time.sleep(3)
        signin.click_on_india_dropdown()  # India dropdown
        time.sleep(3)
        signin.india_select()  # India select
        time.sleep(3)
        signin.enter_valid_creds_8()
        time.sleep(3)
        signin.click_on_the_continue_button()  # continue click
        time.sleep(5)
        signin.enter_invalid_otp_2()
        time.sleep(3)
        signin.click_on_otp_submit_button()
        time.sleep(3)
        assert signin.assertion_10().__eq__("This OTP is not valid")

# 11 Signup using invalid creds. ('1') (OTP iterations)

    def test_signup_using_valid_mobile_number_invalid_OTP_3(self):
        signin = SigninPage(self.driver)
        time.sleep(3)
        signin.click_on_login_button()  # login button
        time.sleep(3)
        signin.click_on_create_your_account()  # Create your account
        time.sleep(3)
        signin.click_on_india_dropdown()  # India dropdown
        time.sleep(3)
        signin.india_select()  # India select
        time.sleep(3)
        signin.enter_valid_creds_8()
        time.sleep(3)
        signin.click_on_the_continue_button()  # continue click
        time.sleep(5)
        signin.enter_invalid_otp_3()
        time.sleep(3)
        signin.click_on_otp_submit_button()
        time.sleep(3)
        assert signin.assertion_10().__eq__("This OTP is not valid")

# 12 Signup using valid creds. ('Valid') (OTP iterations)

    def test_signup_using_valid_mobile_number_valid_OTP(self):
        signin = SigninPage(self.driver)
        time.sleep(3)
        signin.click_on_login_button()  # login button
        time.sleep(3)
        signin.click_on_create_your_account()  # Create your account
        time.sleep(3)
        signin.click_on_india_dropdown()  # India dropdown
        time.sleep(3)
        signin.india_select()  # India select
        time.sleep(3)
        signin.enter_valid_creds_8()
        time.sleep(3)
        signin.click_on_the_continue_button()  # continue click
        # Manually enters OTP
        time.sleep(17)
        signin.click_on_otp_submit_button()
        time.sleep(3)
        assert signin.assertion_12()

