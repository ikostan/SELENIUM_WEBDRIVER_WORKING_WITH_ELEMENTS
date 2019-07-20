# SELENIUM WEBDRIVER - WORKING WITH ELEMENTS 

This is ongoing project. The main goal is to practice with various HTML elements and master Selenium.
['Selenium with Python'](https://selenium-python.readthedocs.io/) official documentation is chosen as a general guide.  

<br/>   
<div align="center"> 
<img width="100%" height="100%" src="https://github.com/ikostan/SELENIUM_WEBDRIVER_WORKING_WITH_ELEMENTS/blob/master/testing_selenium_capabilities/img/1.gif" hspace="20">
</div>
<br/>

### Dev environment:
- Python 3.7
- behave v1.2.6
- pip v19.1.1
- pytest 5.0.1
- selenium 3.141.0
- PyCharm 2019.1.3 (Community Edition)

### Supported/tested browsers:
- Chrome: v75 (64 bit)
- IE: v11 (64 bit)
- Firefox: v68 (64  bit)
- Edge: v17 and above
- Opera: v60

### Note: 
In order to instantiate webdriver I use Driver class of my own. For more info please look here:<br/>
https://github.com/ikostan/SELENIUM_WEBDRIVER_WORKING_WITH_ELEMENTS/tree/master/drivers

###  'Selenium with Python' official documentation webpage:
https://selenium-python.readthedocs.io

### Problem solving:

- **Microsoft webdriver for edge 18 and above:**<br/>
    MS made WebDriver a Windows Feature on Demand (FoD), which ensures that it’s always up to date automatically, and enables some new ways to get Microsoft WebDriver.<br/>
    
    The simplest way to get started is simply to enable Developer Mode. Simply open the Settings app and go to “Update & Security,” “For developers,” and select “Developer Mode.” The appropriate version of WebDriver will be automatically installed.<br/>
    
    You can also install a standalone version of WebDriver in one of two ways:<br/>
    * Search “Manage optional features” from Start, then select “Add a Feature,” “WebDriver.”<br/>
    * Install via DISM by running the following command in an elevated command prompt:
    <br/>```DISM.exe /Online /Add-Capability /CapabilityName:Microsoft.WebDriver~~~~0.0.1.0```<br/>
    
    This also means that we will no longer be providing standalone downloads for Microsoft WebDriver going forward<br/>
    
    Source: https://blogs.windows.com/msedgedev/2018/06/14/webdriver-w3c-recommendation-feature-on-demand/#Rg8g2hRfjBQQVRXy.97
    
- **selenium.common.exceptions.WebDriverException: Message: unknown error: cannot find Opera binary**

    ```python
    from selenium.webdriver.opera.options import Options
    
    options = Options()
    options.binary_location = r'<path to opera.exe>' 
    opera_web_driver_path = r'<path to operadriver.exe>' 
    driver = webdriver.Opera(options=options, executable_path=opera_web_driver_path)
    driver.get(<url>)
    driver.close()
    ```
    Source: https://stackoverflow.com/questions/52793537/selenium-common-exceptions-webdriverexception-message-unknown-error-cannot-fi

- **Internet Explorer browser window not getting closed in Selenium Webdriver**

    ```bash
    1. Open IE browser
    2. Go to Internet Options >>> Security
    3. For every zone heck "Enable Protected Mode"
    4. Restart IE
    ```

- **Test are failed due to slow performance of WebDriver**<br/>
    Explicit wait is used to specify wait condition for a particular element.<br/> 
    Here we define to wait for a certain condition to occur before proceeding further in the code.
    ```python
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as ec
    
    # Wait for element to appear:
    wait = WebDriverWait(self.driver, 10)
    wait.until(ec.title_is(self.new_window_name))
    ```

- **How to Get Selenium to Wait for Page Load After a Click:**<br/>
    It turns out Selenium has a built-in condition called staleness_of, as well as its own wait-for implementation. 
    Use them, alongside the @contextmanager decorator and the magical-but-slightly-scary yield keyword, and you get:

    ```python
    from contextlib import contextmanager
    from selenium.webdriver.support.ui import WebDriverWait 
    from selenium.webdriver.support.expected_conditions import staleness_of
    
    class MySeleniumTest(SomeFunctionalTestClass): 
      # assumes self.browser is a selenium webdriver
    
      @contextmanager
      def wait_for_page_load(self, timeout=30):
        old_page = self.browser.find_element_by_tag_name('html')
        yield
        WebDriverWait(self.browser, timeout).until(
          staleness_of(old_page)
        )
        
      def test_stuff(self):
        # example use
        with self.wait_for_page_load(timeout=10):
          self.browser.find_element_by_link_text('a link')
    ```
    
    **Note** that this solution only works for “non-JavaScript” clicks, i.e., clicks that will cause the browser to load a brand new page, and thus load a brand new HTML body element.
    <br/>Source: https://blog.codeship.com/get-selenium-to-wait-for-page-load/

- **[Required Configuration - IE only](https://github.com/SeleniumHQ/selenium/wiki/InternetExplorerDriver):**<br/>
    
    1. The IEDriverServer exectuable must be downloaded and placed in your **PATH**.<br/>
    2. On IE 7 or higher on Windows Vista or Windows 7, you must set the **Protected Mode** settings for each zone to be the same value. The value can be on or off, as long as it is the same for every zone. To set the Protected Mode settings, choose "Internet Options..." from the Tools menu, and click on the Security tab. For each zone, there will be a check box at the bottom of the tab labeled "Enable Protected Mode".<br/>
    3. Additionally, **"Enhanced Protected Mode"** must be disabled for IE 10 and higher. This option is found in the Advanced tab of the Internet Options dialog.<br/>
    4. The browser zoom level must be set to 100% so that the native mouse events can be set to the correct coordinates.<br/>
    5. For Windows 10, you also need to set *"Change the size of text, apps, and other items"* to 100% in display settings.<br/>
    6. For IE 11 only, you will need to set a registry entry on the target computer so that the driver can maintain a connection to the instance of Internet Explorer it creates. For 32-bit Windows installations, the key you must examine in the registry editor is *HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Internet Explorer\Main\FeatureControl\FEATURE_BFCACHE*. For 64-bit Windows installations, the key is *HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\Internet Explorer\Main\FeatureControl\FEATURE_BFCACHE*. Please note that the *FEATURE_BFCACHE* subkey may or may not be present, and should be created if it is not present. Important: Inside this key, create a *DWORD* value named *iexplore.exe* with the value of *0*.<br/>

- **NoSuchWindowException in IE 11:**<br/>

    1. IE Options --> Security Tab -> Uncheck "Enable Protected Mode".
    2. Add http://localhost/ to your trusted sites in IE11. 
    3. Registry keys:
    <br/>For 64-bit Windows installations, the key is:<br/> 
    ``` HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\Internet explorer\Main\FeatureControl\FEATURE_BFCACHE```
    <br/>For 32-bit Windows installations, the key is:<br/> 
    ```HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Internet Explorer\Main\FeatureControl\FEATURE_BFCACHE```
     
    <br/>Source: https://stackoverflow.com/questions/24746777/selenium-nosuchwindowexception-in-ie-11

### Useful tools:
- **ChroPath** generates unique relative xpath, absolute xpath, cssSelectors, linkText and partialLinkText just by one click. ChroPath can also be used as Editor for selectors. It makes easy to write, edit, extract, and evaluate XPath queries on any webpage. ChroPath also supports iframe, multi selectors generation, generate relative xpath with custom attribute, automation script steps generation and many more.<br/>
Source: https://chrome.google.com/webstore/detail/chropath/ljngjbnaijcbncmcnjfhigebomdlkcjo?hl=en