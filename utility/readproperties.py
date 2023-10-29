import configparser

config = configparser.RawConfigParser()
config.read("C:\\Users\\LAVANYA\\PycharmProjects\\AutomationProject\\configuration\\config.ini")


class ReadConfig:
    @staticmethod
    def getApplicationURL():
        print("hiii")
        url = config.get("common info", "baseURL")
        return url

    @staticmethod
    def getUseremail():
        username = config.get("common info", "username")
        return username

    @staticmethod
    def getPassword():
        password = config.get("common info", "password")
        return password
    #
    # @staticmethod
    # def screen_shots():
    #     screen_shots = config.get('SCREENSHOTS', 'screenshots')
    #     return screen_shots

# print(readConfig.chrome_driver_path())
# print(readConfig.firefox_driver_path())
# print(readConfig.login_page_url())
# print(readConfig.login_email())
# print(readConfig.login_password())
