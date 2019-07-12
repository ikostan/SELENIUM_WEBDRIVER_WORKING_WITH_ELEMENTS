from selenium.webdriver.common.by import By


class RegisterFormLocator:
    '''
    Contains identifiers for all HTML objects
    Web page: http://demo.automationtesting.in/Register.html
    '''

    # First Name field:
    FIRST_NAME_INPUT = (By.XPATH, '/html/body/section/div/div/div[2]/form/div[1]/div[1]/input')

    # Last Name field:
    LAST_NAME_INPUT = (By.XPATH, '/html/body/section/div/div/div[2]/form/div[1]/div[2]/input')

    # Address text area:
    ADDRESS_TEXT_AREA = (By.XPATH, '/html/body/section/div/div/div[2]/form/div[2]/div/textarea')

    # Email address field:
    EMAIL_ADDRESS_INPUT = (By.XPATH, '/html/body/section/div/div/div[2]/form/div[3]/div[1]/input')

    # Phone field:
    PHONE_INPUT = (By.XPATH, '/html/body/section/div/div/div[2]/form/div[4]/div/input')

    # Gender inputs:
    GENDER_MALE_RADIO = (By.XPATH, '/html/body/section/div/div/div[2]/form/div[5]/div/label[1]/input')
    GENDER_FEMALE_RADIO = (By.XPATH, '/html/body/section/div/div/div[2]/form/div[5]/div/label[2]/input')

    # Hobbies:
    CRICKET_CHECKBOX = (By.ID, 'checkbox1')
    MOVIES_CHECKBOX = (By.ID, 'checkbox2')
    HOCKEY_CHECKBOX = (By.ID, 'checkbox3')

    # Languages:
    LANGUAGES_MULTI_SELECT = (By.ID, 'msdd')

    # Skills Combo:
    SKILLS_MULTI_SELECT = (By.ID, 'skills')

    # Country Combo:
    COUNTRY_MULTI_SELECT = (By.ID, 'countries')

    # Select Country Combo:
    SELECT_COUNTRY_MULTI_SELECT = (By.XPATH, '/html/body/section/div/div/div[2]/form/div[10]/div/span/span[1]/span')

    # Date of Birth:
    DOB_YEAR = (By.ID, 'yearbox')
    DOB_MONTH = (By.XPATH, '/html/body/section/div/div/div[2]/form/div[11]/div[2]/select')
    DOB_DAY = (By.ID, 'daybox')

    # Password field:
    PASSWORD_INPUT = (By.ID, "firstpassword")

    # Confirm Password field:
    CONFIRM_PASSWORD_INPUT = (By.ID, "secondpassword")

    # Submit button
    SUBMIT_BTN = (By.ID, 'submitbtn')

    # Refresh button
    REFRESH_BTN = (By.ID, 'Button1')

    # Browse button
    BROWSE_BTN = (By.ID, 'imagesrc')

