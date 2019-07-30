# Waits

Selenium Webdriver provides two types of waits - implicit & explicit. An explicit wait makes WebDriver wait for a certain condition to occur before proceeding further with execution. An implicit wait makes WebDriver poll the DOM for a certain amount of time when trying to locate an element.

### Explicit Waits:<br/>
   WebDriverWait in combination with ExpectedCondition is one way this can be accomplished.<br/>

```python
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    
    # Open test web page and verify URL + Title
    self.driver = webdriver.Firefox()
    self.driver.get(self.test_url)
    self.driver.maximize_window()
        
    # Explicit wait for a title
    WebDriverWait(self.driver, 10).until(EC.title_contains(self.test_title))

    self.assertEqual(self.test_url, self.driver.current_url)
    self.assertEqual(self.test_title, self.driver.title)
```

### Implicit Waits:<br/>
   An implicit wait tells WebDriver to poll the DOM for a certain amount of time when trying to find any element (or elements) not immediately available. The default setting is 0. Once set, the implicit wait is set for the life of the WebDriver object.<br/>
    
```python
    from selenium import webdriver
    
    # Open test web page and verify URL + Title
    self.driver = webdriver.Firefox()

    # Implicit wait
    self.driver.implicitly_wait(10)  # seconds

    self.driver.get(self.test_url)
    self.driver.maximize_window()

    self.assertEqual(self.test_url, self.driver.current_url)
    self.assertEqual(self.test_title, self.driver.title)
```


### Source:
https://selenium-python.readthedocs.io/waits.html