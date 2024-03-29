### Topics covered:

**[Navigating:](https://github.com/ikostan/SELENIUM_WEBDRIVER_WORKING_WITH_ELEMENTS/tree/master/testing_selenium_capabilities/tests/navigating)**
 
1. **Interacting with the page:**<br/>
    WebDriver offers a number of ways to find elements.<br/>
    ```
    find_element_by_id, find_element_by_name, find_element_by_xpath, 
    send_keys, Keys.ARROW_LEFT, Keys.ARROW_RIGHT, send_keys
    ```
    
2. **Filling in forms:**<br/>
    ```
    select_by_visible_text, select_by_value, get_attribute,
    find_element_by_name, get_attribute, click
    ```
    
    <br/>   
    <div align="center"> 
    <img width="95%" height="95%" src="https://github.com/ikostan/SELENIUM_WEBDRIVER_WORKING_WITH_ELEMENTS/blob/master/testing_selenium_capabilities/img/1.gif" hspace="20">
    </div>
    <br/> 
    
3. **Drag and drop:**<br/>
    You can use drag and drop, either moving an element by a certain amount, or on to another element.<br/>
    ```ActionChains, drag_and_drop, perform```
    
    <br/>   
    <div align="center"> 
    <img width="95%" height="95%" src="https://github.com/ikostan/SELENIUM_WEBDRIVER_WORKING_WITH_ELEMENTS/blob/master/testing_selenium_capabilities/img/3.gif" hspace="20">
    </div>
    <br/> 
    
4. **Moving between windows:**<br/>
    WebDriver supports moving between named windows using the “switch_to_window” method.<br/>
    ```switch_to_window, window_handles```<br/>
    For more info look here:<br/>
    http://antlong.com/common-operations-working-with-tabs-in-webdriver/
    
    <br/>   
    <div align="center"> 
    <img width="95%" height="95%" src="https://github.com/ikostan/SELENIUM_WEBDRIVER_WORKING_WITH_ELEMENTS/blob/master/testing_selenium_capabilities/img/2.gif" hspace="20">
    </div>
    <br/> 
    
5. **Moving between frames:**<br/>
    You can also swing from frame to frame (or into iframes).<br/>
    ```switch_to.frame, switch_to.default_content```
    
    <br/>   
    <div align="center"> 
    <img width="95%" height="95%" src="https://github.com/ikostan/SELENIUM_WEBDRIVER_WORKING_WITH_ELEMENTS/blob/master/testing_selenium_capabilities/img/4.gif" hspace="20">
    </div>
    <br/> 
    
6. **Popup dialogs:**<br/>
    Selenium WebDriver has built-in support for handling popup dialog boxes. After you’ve triggered action that would open a popup, you can access the alert with the following:<br/>
    ```alert = driver.switch_to.alert()```   
    <br/>This will return the currently open alert object. With this object, you can now accept, dismiss, read its contents or even type into a prompt. This interface works equally well on alerts, confirms, prompts:<br/>
    ```alert.confirm_box.dismiss(), alert.accept(), alert.text, alert.send_keys("<some text>")```   

    <br/>   
    <div align="center"> 
    <img width="95%" height="95%" src="https://github.com/ikostan/SELENIUM_WEBDRIVER_WORKING_WITH_ELEMENTS/blob/master/testing_selenium_capabilities/img/5.gif" hspace="20">
    </div>
    <br/> 
    
7. **Navigation: history and location:**<br/>
    WebDriver has a number of smaller, task-focused interfaces, and navigation is a useful task. To navigate to a page, you can use get method:<br/>
    ```driver.get("http://www.example.com")```
    <br/>To move backward and forward in your browser’s history:<br/>
    ```driver.forward(), driver.back()```

    <br/>   
    <div align="center"> 
    <img width="95%" height="95%" src="https://github.com/ikostan/SELENIUM_WEBDRIVER_WORKING_WITH_ELEMENTS/blob/master/testing_selenium_capabilities/img/6.gif" hspace="20">
    </div>
    <br/> 
    
8. **Cookies:**<br/>
    First of all, you need to be on the domain that the cookie will be valid for:<br/>   
    ```python
    # Go to the correct domain
    driver.get("http://www.example.com")
    
    # Now set the cookie. This one's valid for the entire domain
    cookie = {‘name’ : ‘foo’, ‘value’ : ‘bar’}
    driver.add_cookie(cookie)
    
    # And now output all the available cookies for the current URL
    driver.get_cookies()
    ```
