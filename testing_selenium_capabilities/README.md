# Testing Selenium Capabilities

In order to master Selenium + Python3 I decided to go over on "Selenium with Python" documentation and test all basic capabilities with various browsers.

### Topics covered:

1. **Getting Started:**
    - Simple Usage:<br/>
    ```
    assert, driver.title, send_keys, find_element_by_name, clear
    ```
    - Using Selenium to write tests:<br/>
    ```
    setUpClass, setUp, tearDown, tearDownClass, self.assertIn, 
    self.assertFalse, driver.maximize_window
    ```

2. **Navigating:**
    - Interacting with the page:<br/>
    ```
    find_element_by_id, find_element_by_name, find_element_by_xpath, 
    send_keys, Keys.ARROW_LEFT, Keys.ARROW_RIGHT, send_keys
    ```
    - Filling in forms:<br/>
    ```
    select_by_visible_text, select_by_value, get_attribute,
    find_element_by_name, get_attribute, click
    ```
    - Drag and drop:<br/>
    ```
    ActionChains, drag_and_drop, perform
    ```

<br/>   
<div align="center"> 
<img width="95%" height="95%" src="https://github.com/ikostan/SELENIUM_WEBDRIVER_WORKING_WITH_ELEMENTS/blob/master/testing_selenium_capabilities/img/ezgif.com-video-to-gif.gif" hspace="20">
</div>
<br/> 

### Note: 
In order to instantiate webdriver I use Driver class of my own. For more info please look here:<br/>
https://github.com/ikostan/SELENIUM_WEBDRIVER_WORKING_WITH_ELEMENTS/tree/master/drivers

### Supported browsers:
- Chrome
- IE
- Firefox
- Edge
- Opera

### Switch Between IFrames Using Selenium Python:
- Detect iframe element:<br/>
```iframe = driver.find_elements_by_tag_name('iframe')```
- Switch to iframe:<br/>
```self.driver.switch_to.frame(iframe)```
- Every time you need to move back from an IFrame to the parent HTML. Selenium Webdriver provides the following method:<br/>
```driver.switch_to.default_content()```

### Documentation webpage:
https://selenium-python.readthedocs.io