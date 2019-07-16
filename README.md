# SELENIUM WEBDRIVER - WORKING WITH ELEMENTS 

This is ongoing project. The main goal is to practice with various HTML elements and master Selenium.
['Selenium with Python'](https://selenium-python.readthedocs.io/) official documentation is chosen as a general guide.  

### Dev environment:
- Python 3.7
- behave v1.2.6
- pip v19.1.1
- pytest 5.0.1
- selenium 3.141.0
- PyCharm 2019.1.3 (Community Edition)

### Supported browsers:
- Chrome
- IE
- Firefox
- Edge
- Opera

### Note: 
In order to instantiate webdriver I use Driver class of my own. For more info please look here:<br/>
https://github.com/ikostan/SELENIUM_WEBDRIVER_WORKING_WITH_ELEMENTS/tree/master/drivers

###  'Selenium with Python' official documentation webpage:
https://selenium-python.readthedocs.io

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

- **Test are failed due to slow performance of WebDriver**<br/>
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