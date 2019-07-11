from selenium.webdriver.common.by import By


class EtPbSection1Locator:

    '''
    Contains all elements identifiers
    from https://www.ultimateqa.com/simple-html-elements-for-automation/
    webpage. class="et_pb_section >>> et_pb_section_1
    '''

    SECTION1 = (By.XPATH, '/html/body/div[1]/div/div/article/div/div[1]/div/div[2]/div/div[3]')

    # Click this button using "ID"
    BUTTON_WITH_ID = (By.ID, 'idExample')

    # Click button using ClassName
    BUTTON_WITH_CLASS_NAME = (By.CLASS_NAME, 'buttonClass')

    # Click button using Name
    BUTTON_WITH_NAME = (By.NAME, 'button1')

    # Click me using this link text!
    LINK_WITH_TEXT_1 = (By.LINK_TEXT, 'Click me using this link text!')

    # Click me using this link text
    LINK_WITH_TEXT_2 = (By.LINK_TEXT, 'Click me using this link text')
