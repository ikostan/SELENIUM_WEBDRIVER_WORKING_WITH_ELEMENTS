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

    <br/>   
    <div align="center"> 
    <img width="95%" height="95%" src="https://github.com/ikostan/SELENIUM_WEBDRIVER_WORKING_WITH_ELEMENTS/blob/master/testing_selenium_capabilities/img/7.gif" hspace="20">
    </div>
    <br/> 

3. **Locating by XPath**<br/>
    XPath is the language used for locating nodes in an XML document. As HTML can be an implementation of XML (XHTML), Selenium users can leverage this powerful language to target elements in their web applications.<br/>
    ```python
    clear_button = driver.find_element_by_xpath("//input[@name='continue'][@type='button']")
    clear_button = driver.find_element_by_xpath("//form[@id='loginForm']/input[4]")
    ```
    
    [XPath Tutorial - with interactive examples.](http://www.zvon.org/comp/r/tut-XPath_1.html)
    
4. **Locating Hyperlinks by Link Text**<br/>
    Use this when you know link text used within an anchor tag. With this strategy, the first element with the link text value matching the location will be returned. If no element has a matching link text attribute, a NoSuchElementException will be raised.<br/>
    ```python
    continue_link = driver.find_element_by_link_text('Continue')
    continue_link = driver.find_element_by_partial_link_text('Conti')
    ```

5. **Locating Elements by Tag Name**<br/>
    Use this when you want to locate an element by tag name. With this strategy, the first element with the given tag name will be returned. If no element has a matching tag name, a NoSuchElementException will be raised.<br/>
    ```python
    heading1 = driver.find_element_by_tag_name('h1')
    ```

6. **Locating Elements by Class Name**<br/>
    Use this when you want to locate an element by class attribute name. With this strategy, the first element with the matching class attribute name will be returned. If no element has a matching class attribute name, a NoSuchElementException will be raised.<br/>
    ```python
    content = driver.find_element_by_class_name('content')
    ```

7. **Locating Elements by CSS Selectors**<br/>
    Use this when you want to locate an element by CSS selector syntax. With this strategy, the first element with the matching CSS selector will be returned. If no element has a matching CSS selector, a NoSuchElementException will be raised.<br/>
    ```python
    content = driver.find_element_by_css_selector('p.content')
    ```
    
    [Selenium Tips: CSS Selectors](https://saucelabs.com/resources/articles/selenium-tips-css-selectors)