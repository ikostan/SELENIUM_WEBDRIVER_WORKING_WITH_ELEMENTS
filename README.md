# SELENIUM WEBDRIVER - WORKING WITH ELEMENTS 

This is ongoing project. The main goal is to practice with various HTML elements and master Selenium.

### Problem solving:

- **selenium.common.exceptions.WebDriverException: Message: unknown error: cannot find Opera binary**

```bash
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

- **Test are failed due to slow performance of WebBrowser**<br/>
Explicit wait is used to specify wait condition for a particular element.<br/> 
Here we define to wait for a certain condition to occur before proceeding further in the code.
```bash
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

# Wait for element to appear:
wait = WebDriverWait(self.driver, 10)
wait.until(ec.title_is(self.new_window_name))
```

### Useful tools:
- **ChroPath** generates unique relative xpath, absolute xpath, cssSelectors, linkText and partialLinkText just by one click. ChroPath can also be used as Editor for selectors. It makes easy to write, edit, extract, and evaluate XPath queries on any webpage. ChroPath also supports iframe, multi selectors generation, generate relative xpath with custom attribute, automation script steps generation and many more.
Source: https://chrome.google.com/webstore/detail/chropath/ljngjbnaijcbncmcnjfhigebomdlkcjo?hl=en