### Topics covered:
    
**[Locating Elements:](https://github.com/ikostan/SELENIUM_WEBDRIVER_WORKING_WITH_ELEMENTS/tree/master/testing_selenium_capabilities/tests/locating_elements)**
<br/>There are various strategies to locate elements in a page. You can use the most appropriate one for your case.

1. **Locating by Id**<br/>
    Use this when you know id attribute of an element. With this strategy, the first element with the id attribute value matching the location will be returned. If no element has a matching id attribute, a NoSuchElementException will be raised.<br/>
    ```python
    from selenium.webdriver.common.by import By
    login_form = driver.find_element(By.ID, 'loginForm')
    ```