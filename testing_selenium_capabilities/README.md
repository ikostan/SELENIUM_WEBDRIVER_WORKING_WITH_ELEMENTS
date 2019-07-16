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
    
    <br/>   
    <div align="center"> 
    <img width="95%" height="95%" src="https://github.com/ikostan/SELENIUM_WEBDRIVER_WORKING_WITH_ELEMENTS/blob/master/testing_selenium_capabilities/img/1.gif" hspace="20">
    </div>
    <br/> 
    
    - Drag and drop:<br/>
    ```ActionChains, drag_and_drop, perform```
    
    - Moving between windows:<br/>
    ```switch_to_window, window_handles```<br/>
    For more info look here:<br/>
    http://antlong.com/common-operations-working-with-tabs-in-webdriver/
    
    <br/>   
    <div align="center"> 
    <img width="95%" height="95%" src="https://github.com/ikostan/SELENIUM_WEBDRIVER_WORKING_WITH_ELEMENTS/blob/master/testing_selenium_capabilities/img/2.gif" hspace="20">
    </div>
    <br/> 
    
    - Moving between frames:<br/>
    ```switch_to_frame, switch_to_default_content```
