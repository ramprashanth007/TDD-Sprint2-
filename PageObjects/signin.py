from selenium.webdriver.common.by import By


class SigninPage:

    def __init__(self, driver):
        self.driver = driver

    def click_on_login_button(self):
        return self.driver.find_element(By.XPATH, "//span[normalize-space()='Log in']").click()  # login button

    def click_on_create_your_account(self):
        return self.driver.find_element(By.XPATH,"//h6[@class='css-nmgvwj-H6-StyledH6 e1l7v5xe2']").click() # Create your account

    def click_on_india_dropdown(self):
        return self.driver.find_element(By.XPATH,"//div[@role='presentation']//div[1]//div[1]//img[1]").click() # India dropdown

    def india_select(self):
        return self.driver.find_element(By.XPATH,"//span[contains(@class,'css-1szx4e-Label e10ouzx63')]").click() # India select

    def click_on_the_continue_button(self):
        return self.driver.find_element(By.XPATH,"//button[contains(@aria-label,'Continue')]").click()  # continue click

    def assertion_comparison_otp_page(self):
        return self.driver.find_element(By.XPATH,'//*[@id="DrawerPaper"]/div[2]/h2').text

    def click_on_otp_submit_button(self):
        return self.driver.find_element(By.XPATH, '//*[@id="DrawerPaper"]/div[2]/div[2]/button').click() # submit button click

    # INPUT FUNCTIONS

    def enter_invalid_creds_1(self):
        return self.driver.find_element(By.XPATH,"//input[@aria-invalid='false']").send_keys('1122334456') # enter value 1

    def enter_invalid_creds_2(self):
        return self.driver.find_element(By.XPATH,"//input[@aria-invalid='false']").send_keys('0000000000') # enter value 2

    def enter_invalid_creds_3(self):
        return self.driver.find_element(By.XPATH,"//input[@aria-invalid='false']").send_keys('')  # enter value 3

    def enter_invalid_creds_4(self):
        return self.driver.find_element(By.XPATH,"//input[@aria-invalid='false']").send_keys('1') # enter value 4

    def enter_invalid_creds_5(self):
        return self.driver.find_element(By.XPATH,"//input[@aria-invalid='false']").send_keys('11111aaaaa') # enter value 5

    def enter_invalid_creds_6(self):
        return self.driver.find_element(By.XPATH,"//input[@aria-invalid='false']").send_keys('aaa!!!@@@b') # enter value 6

    def enter_invalid_creds_7(self):
        return self.driver.find_element(By.XPATH,"//input[@aria-invalid='false']").send_keys('111!!!@@@2') # enter value 7

    def enter_valid_creds_8(self):
        return self.driver.find_element(By.XPATH,"//input[@aria-invalid='false']").send_keys('9600415148') # enter value 8

    def enter_invalid_otp_1(self):
        return self.driver.find_element(By.XPATH, '//*[@id="DrawerPaper"]/div[2]/form/div/input').send_keys('')  #no data OTP

    def enter_invalid_otp_2(self):
        return self.driver.find_element(By.XPATH, '//*[@id="DrawerPaper"]/div[2]/form/div/input').send_keys('111111')  #max OTP

    def enter_invalid_otp_3(self):
        return self.driver.find_element(By.XPATH, '//*[@id="DrawerPaper"]/div[2]/form/div/input').send_keys('1')  #min OTP



    # ASSERTIONS

    def assertion_2(self):
        return self.driver.find_element(By.XPATH,"//p[@class='css-5piwwz-StyledP2 ena7kom0']").is_displayed()  # testcase 2

    def assertion_3(self):
        return self.driver.find_element(By.XPATH,'//*[@id="DrawerPaper"]/div[2]/h2').text  # testcase 3

    def assertion_4(self):
        return self.driver.find_element(By.XPATH, '//*[@id="DrawerPaper"]/div[2]/h2').text #testcase 4

    def assertion_5(self):
        return self.driver.find_element(By.XPATH, '//*[@id="DrawerPaper"]/div[2]/h2').text #testcase 5

    def assertion_6(self):
        return self.driver.find_element(By.XPATH, '//*[@id="DrawerPaper"]/div[2]/h2').text #testcase 6

    def assertion_7(self):
        return self.driver.find_element(By.XPATH, '//*[@id="DrawerPaper"]/div[2]/h2').text #testcase 7

    def assertion_8(self):
        return self.driver.find_element(By.XPATH, "//h2[@class='css-18xjf2j-H2-Header e52pvpx0']").text  # testcase 8

    def assertion_10(self):
        return self.driver.find_element(By.XPATH, "//p[@class='css-5piwwz-StyledP2 ena7kom0']").text  # testcase 10

    def assertion_12(self):
        return self.driver.find_element(By.XPATH, "//div[@class='css-1l0yl4a-WrapperBg e1nb2fb81']").is_displayed() #testcase 12

    # assertion logic
    def assertion_logic(self):
        if self.assertion_comparison_otp_page.__eq__("Verify your mobile number"):
            return False
        else:
            return True






