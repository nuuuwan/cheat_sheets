# Python - Selenium


## Basic

```python
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options = Options()
options.headless = True

driver = webdriver.Firefox(options=options)

driver.get(URL)

driver.close()  # closes only the current window on which Selenium is running

driver.quit() # closes all browser windows and ends the WebDriver session.


```

## Find Elements

```python
find_element_by_id
find_element_by_tag_name
find_element_by_class_name
find_element_by_xpath
find_element_by_css


find_elements_by_id

```

## Attributes


```python
a.text
a.get_attribute('href')
```



