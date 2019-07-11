# SELENIUM WEBDRIVER - WORKING WITH ELEMENTS COURSE

Master web element identification, manipulation, and interrogation using Selenium WebDriver. Taught by Nikolay Advolodkin.

### Topics covered:
- Basics of HTML
- All the different locator strategies for Selenium WebDriver
- How to identify web elements using Selenium WebDriver
- Master XPath
- Navigation with Selenium WebDriver
- Web element manipulation
- Web element interrogation
- Mouse and keyboard actions with Selenium WebDriver
- Performing actions such as drag n' drop, drawing, hovering
- Implicit and Explicit waits
- How to properly handle element identification so that your tests are not flaky
- Expected Conditions in Selenium WebDriv

### Source:
https://courses.ultimateqa.com/courses/take/working-with-elements

### Problem solving:

- selenium.common.exceptions.WebDriverException: Message: unknown error: cannot find Opera binary

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