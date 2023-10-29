import logging
import time
class LogGen:

    @staticmethod
    def loggen():
        #dateTimeStamp = time.strftime('%Y_%m_%d_%H_%M')
        logging.basicConfig(filename="C:\\Users\\LAVANYA\\PycharmProjects\\AutomationProject\\Logs\\automation.log",
                       format='%(asctime)s : %(name)s : %(levelname)s : %(message)s' ,
                            datefmt='%d-%m-%Y %I:%M:%S %p',force=True)
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger