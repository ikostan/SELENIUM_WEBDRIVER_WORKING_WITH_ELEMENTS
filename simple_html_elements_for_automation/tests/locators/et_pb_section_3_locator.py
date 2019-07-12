from selenium.webdriver.common.by import By


class EtPbSection3Locator:
    '''
    Contains all elements identifiers
    from https://www.ultimateqa.com/simple-html-elements-for-automation/
    webpage. class="et_pb_section >>> et_pb_section_3
    '''

    COMMON_XPATH = (By.XPATH, '//*[@id="button1"]')

    # XPath tutorial for automation testers
    # /html/body/div[1]/div/div/article/div/div[1]/div/div[4]/div[1]/div/div[1]/div/div/div/form
    # /html/body/div[1]/div/div/article/div/div[1]/div/div[4]/div[1]/div/div[1]/div/div
    FIRST_BTN_FORM = (By.XPATH, '/html/body/div[1]/div/div/article/div/div[1]/div/div[4]/div[1]/div/div[1]/div/div')

    # 2. Button 2 - same exact button, different place in the HTML

    # Xpath with different button text

    # 2. Button 2 - same exact button, different place in the HTML
    # /html/body/div[1]/div/div/article/div/div[1]/div/div[4]/div[2]/div/div[2]/div/div/div/form
    FORTH_BTN_FORM = (By.XPATH, '/html/body/div[1]/div/div/article/div/div[1]/div/div[4]/div[2]/div/div[2]/div/div/div/form')
