
import pytest
from selenium import webdriver
from selenium import webdriver


# from utility.readproperties import ReadConfig
# from utility.customLogger import LogGen

def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome", action="store")


# @pytest.fixture(scope="session")
# def browser(request):
#    return request.config.getoption("--browser")
driver =None
@pytest.fixture(scope='class')
def driver(request):
    global  driver
    browser = request.config.getoption("--browser")

    if browser == 'chrome':
        driver = webdriver.Chrome()
        print("Lanching chrome browser....")
        # yield driver
        # driver.close()
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("launching Firefox browser.....")
    elif browser == 'IE':
        driver = webdriver.Ie()
    else:
        driver = webdriver.Chrome()

    yield
    request.cls.driver = driver
    driver.quit()





# def pytest_configure(config):
#     '''
#              It is hook for adding environment info to the HTML report
#              :param config: Configure the html report
#              :return:
#              '''
#     config._metadata['Project Name'] = 'NOP COMMERCE'
#     config._metadata['Module Name'] = 'Customer'
#     config._metadata['Tester'] = 'MandarK'
#
#
# @pytest.mark.optionalhook
# def pytest_metadata(metadata):
#     '''
#              Hook for delete/modify environment info to the HTML report
#              :param metadata:
#              :return:
#              '''
#     metadata.pop("JAVA_HOME", None)
#     metadata.pop("Plugins", None)
#
# # from selenium import webdriver
# import pytest
#
#
# @pytest.fixture()
# def setup():
#     driver = webdriver.Chrome()
#     return driver
