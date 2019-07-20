from drivers.path_config import DriverPath
from selenium.webdriver.opera.options import Options
from selenium import webdriver
import platform


class Driver:

    _driver_path = {
        'chrome': DriverPath.CHROME_WEB_DRIVER_PATH,
        'ie': DriverPath.IE_WEB_DRIVER_PATH,
        'opera': DriverPath.OPERA_WEB_DRIVER_PATH,
        'mozilla': DriverPath.MOZILLA_WEB_DRIVER_PATH,
        'edge': DriverPath.EDGE_WEB_DRIVER_PATH
    }

    def __init__(self, browser: str):

        if browser not in self._driver_path.keys():
            raise NameError("Invalid browser name: {}."
                            "\nOnly following browsers supported: {}".format(browser,
                                                                             ', '.join([key for key in self._driver_path.keys()])))

        self.browser = browser
        self._set_driver()

    def _set_driver(self):

        if self.browser == 'opera':
            options = Options()
            options.binary_location = DriverPath.OPERA_BINARY_PATH
            self.driver = webdriver.Opera(options=options,
                                          executable_path=self._driver_path[self.browser])

        if self.browser == 'chrome':
            self.driver = webdriver.Chrome(executable_path=self._driver_path[self.browser])

        if self.browser == 'ie':
            self.driver = webdriver.Ie(executable_path=self._driver_path[self.browser])

        if self.browser == 'mozilla':
            self.driver = webdriver.Firefox(executable_path=self._driver_path[self.browser])

        if self.browser == 'edge':
            print('Version      :', platform.python_version())
            print('Version tuple:', platform.python_version_tuple())
            print('Compiler     :', platform.python_compiler())
            print('Build        :', platform.python_build())
            self.driver = webdriver.Edge(executable_path=self._driver_path[self.browser])

    def get_driver(self):
        return self.driver
