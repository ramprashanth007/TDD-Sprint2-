import pytest
from selenium import webdriver

driver = None


@pytest.fixture()
def starter(request):
    global driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://unacademy.com/")
    request.cls.driver = driver
    yield
    driver.quit()
