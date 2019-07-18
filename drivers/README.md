# Driver package: 

The main idea behind it is to simplify working process with Selenium 'webdriver' object.
In order to create webdriver object you just do the following:
```python
from driver.driver import Driver
driver = Driver('chrome').get_driver()
```

### Supported browsers:
- Chrome
- IE
- Firefox
- Edge
- Opera
