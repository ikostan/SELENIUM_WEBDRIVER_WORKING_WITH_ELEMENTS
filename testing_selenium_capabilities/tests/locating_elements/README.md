### Topics covered:
    
**[Locating Elements:](https://github.com/ikostan/SELENIUM_WEBDRIVER_WORKING_WITH_ELEMENTS/tree/master/testing_selenium_capabilities/tests/locating_elements)**
<br/>There are various strategies to locate elements in a page. You can use the most appropriate one for your case.

There are two private methods which might be useful with locators in page objects. These are the two private methods: *find_element* and *find_elements*.<br/>

**Example usage:**<br/>

```python
    from selenium.webdriver.common.by import By

    driver.find_element(By.XPATH, '//button[text()="Some text"]')
    driver.find_elements(By.XPATH, '//button')
```

**These are the attributes available for By class:**<br/>

```python
    ID = "id"
    XPATH = "xpath"
    LINK_TEXT = "link text"
    PARTIAL_LINK_TEXT = "partial link text"
    NAME = "name"
    TAG_NAME = "tag name"
    CLASS_NAME = "class name"
    CSS_SELECTOR = "css selector"
```

1. **Locating by Id**<br/>
    Use this when you know id attribute of an element. With this strategy, the first element with the id attribute value matching the location will be returned. If no element has a matching id attribute, a NoSuchElementException will be raised.<br/>
    ```python
    from selenium.webdriver.common.by import By
    login_form = driver.find_element(By.ID, 'loginForm')
    ```

2. **Locating by Name**<br/>
    Use this when you know name attribute of an element. With this strategy, the first element with the name attribute value matching the location will be returned. If no element has a matching name attribute, a NoSuchElementException will be raised.<br/>
    ```python
    login_btn = self.driver.find_element(By.NAME, 'login')
    ```

3. **Locating by XPath**<br/>
    XPath is the language used for locating nodes in an XML document. As HTML can be an implementation of XML (XHTML), Selenium users can leverage this powerful language to target elements in their web applications.<br/>
    
4. **Locating Hyperlinks by Link Text**<br/>