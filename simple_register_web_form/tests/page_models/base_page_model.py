class BasePageModel:

    def __init__(self, driver):
        self.driver = driver

    @property
    def url(self):
        return 'http://demo.automationtesting.in/'
