from simple_register_web_form.tests.locators.register_form_locators import RegisterFormLocator
from simple_register_web_form.tests.page_models.base_page_model import BasePageModel


class RegisterPageModel(BasePageModel):

    _url = 'Register.html'

    # Web page title
    @property
    def title(self):
        '''
        returns web page title
        :return:
        '''
        return self.driver.find_element(*RegisterFormLocator.TITLE)

    # Register page URL
    @property
    def url(self):
        '''
        returns web page url
        :return:
        '''
        return super(RegisterPageModel, self).url + self._url

    # First Name field:
    @property
    def first_name_field(self):
        '''
        returns first name field
        :return:
        '''
        return self.driver.find_element(*RegisterFormLocator.FIRST_NAME_INPUT)

    # Last Name field:
    @property
    def last_name_field(self):
        '''
        returns last name field
        :return:
        '''
        return self.driver.find_element(*RegisterFormLocator.LAST_NAME_INPUT)

    # Address text area:
    @property
    def address_text_area(self):
        '''
        returns address text area
        :return:
        '''
        return self.driver.find_element(*RegisterFormLocator.ADDRESS_TEXT_AREA)

    # Email address field:
    @property
    def email_field(self):
        '''
        returns email address field
        :return:
        '''
        return self.driver.find_element(*RegisterFormLocator.EMAIL_ADDRESS_INPUT)

    # Phone field:
    @property
    def phone_field(self):
        '''
        returns phone number field
        :return:
        '''
        return self.driver.find_element(*RegisterFormLocator.PHONE_INPUT)

    # Gender inputs:
    @property
    def gender_male_radio(self):
        '''
        returns gender male radio button
        :return:
        '''
        return self.driver.find_element(*RegisterFormLocator.GENDER_MALE_RADIO)

    @property
    def gender_female_radio(self):
        '''
        returns gender female radio button
        :return:
        '''
        return self.driver.find_element(*RegisterFormLocator.GENDER_FEMALE_RADIO)

    # Hobbies:
    @property
    def hobbies_checkboxes(self):
        '''
        returns set of checkboxes
        :return:
        '''
        checkboxes = {'cricket': self.driver.find_element(*RegisterFormLocator.CRICKET_CHECKBOX),
                      'movies': self.driver.find_element(*RegisterFormLocator.MOVIES_CHECKBOX),
                      'hockey': self.driver.find_element(*RegisterFormLocator.HOCKEY_CHECKBOX)}
        return checkboxes

    # Languages:
    @property
    def languages_combo(self):
        '''
        returns languages combo box
        :return:
        '''
        return self.driver.find_element(*RegisterFormLocator.LANGUAGES_MULTI_SELECT)

    # Skills Combo:
    @property
    def skills_combo(self):
        '''
        returns skills combo box
        :return:
        '''
        return self.driver.find_element(*RegisterFormLocator.SKILLS_MULTI_SELECT)

    # Country Combo:
    @property
    def country_combo(self):
        '''
        returns country combo box
        :return:
        '''
        return self.driver.find_element(*RegisterFormLocator.COUNTRY_MULTI_SELECT)

    # Select Country Combo:
    @property
    def select_country_combo(self):
        '''
        returns select country combo box
        :return:
        '''
        return self.driver.find_element(*RegisterFormLocator.SELECT_COUNTRY_MULTI_SELECT)

    # Date of Birth:
    @property
    def dob_year_combo(self):
        '''
        returns date of birth - year combo
        :return:
        '''
        return self.driver.find_element(*RegisterFormLocator.DOB_YEAR)

    def dob_month_combo(self):
        '''
        returns date of birth - month combo
        :return:
        '''
        return self.driver.find_element(*RegisterFormLocator.DOB_MONTH)

    def dob_day_combo(self):
        '''
        returns date of birth - day combo
        :return:
        '''
        return self.driver.find_element(*RegisterFormLocator.DOB_DAY)

    # Password field:
    @property
    def password_field(self):
        '''
        returns password field
        :return:
        '''
        return self.driver.find_element(*RegisterFormLocator.PASSWORD_INPUT)

    # Confirm Password field:
    @property
    def confirm_password_field(self):
        '''
        returns confirm password field
        :return:
        '''
        return self.driver.find_element(*RegisterFormLocator.CONFIRM_PASSWORD_INPUT)

    # Submit button
    @property
    def submit_button(self):
        '''
        returns submit button
        :return:
        '''
        return self.driver.find_element(*RegisterFormLocator.SUBMIT_BTN)

    # Refresh button
    @property
    def refresh_button(self):
        '''
        returns refresh button
        :return:
        '''
        return self.driver.find_element(*RegisterFormLocator.REFRESH_BTN)

    # Browse button
    @property
    def browse_button(self):
        '''
        returns browse button
        :return:
        '''
        return self.driver.find_element(*RegisterFormLocator.BROWSE_BTN)

