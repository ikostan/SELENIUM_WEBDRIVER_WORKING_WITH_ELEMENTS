# Testing Selenium Capabilities

In order to master Selenium + Python3 I decided to go over on "Selenium with Python" documentation and test all basic capabilities with various browsers.

### Topics covered:

1. **[Getting Started:](https://github.com/ikostan/SELENIUM_WEBDRIVER_WORKING_WITH_ELEMENTS/tree/master/testing_selenium_capabilities/tests/simple_usage)**
    - Simple Usage:<br/>
    ```
    assert, driver.title, send_keys, find_element_by_name, clear
    ```
    - Using Selenium to write tests:<br/>
    ```
    setUpClass, setUp, tearDown, tearDownClass, self.assertIn, 
    self.assertFalse, driver.maximize_window
    ```

2. **[Navigating:](https://github.com/ikostan/SELENIUM_WEBDRIVER_WORKING_WITH_ELEMENTS/tree/master/testing_selenium_capabilities/tests/navigating)**
    - Interacting with the page:<br/>
    WebDriver offers a number of ways to find elements.<br/>
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
    You can use drag and drop, either moving an element by a certain amount, or on to another element.<br/>
    ```ActionChains, drag_and_drop, perform```
    
    <br/>   
    <div align="center"> 
    <img width="95%" height="95%" src="https://github.com/ikostan/SELENIUM_WEBDRIVER_WORKING_WITH_ELEMENTS/blob/master/testing_selenium_capabilities/img/3.gif" hspace="20">
    </div>
    <br/> 
    
    - Moving between windows:<br/>
    WebDriver supports moving between named windows using the “switch_to_window” method.<br/>
    ```switch_to_window, window_handles```<br/>
    For more info look here:<br/>
    http://antlong.com/common-operations-working-with-tabs-in-webdriver/
    
    <br/>   
    <div align="center"> 
    <img width="95%" height="95%" src="https://github.com/ikostan/SELENIUM_WEBDRIVER_WORKING_WITH_ELEMENTS/blob/master/testing_selenium_capabilities/img/2.gif" hspace="20">
    </div>
    <br/> 
    
    - Moving between frames:<br/>
    You can also swing from frame to frame (or into iframes).<br/>
    ```switch_to_frame, switch_to_default_content```
    
    <br/>   
    <div align="center"> 
    <img width="95%" height="95%" src="https://github.com/ikostan/SELENIUM_WEBDRIVER_WORKING_WITH_ELEMENTS/blob/master/testing_selenium_capabilities/img/4.gif" hspace="20">
    </div>
    <br/> 
    
    - Popup dialogs:<br/>
    Selenium WebDriver has built-in support for handling popup dialog boxes. After you’ve triggered action that would open a popup, you can access the alert with the following:<br/>
    ```alert = driver.switch_to_alert()```<br/>
    This will return the currently open alert object. With this object, you can now accept, dismiss, read its contents or even type into a prompt. This interface works equally well on alerts, confirms, prompts.
