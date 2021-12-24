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


## Page Source HTML

```python
driver.page_source
```

## Screenshots

```python
driver.get_screenshot_as_file(png_file)
```

## Screen/Window Size

```python
driver.set_window_size(1920, 1080)
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

```python
driver.find_element_by_xpath('//button[text()="Some text"]')
```


## Attributes


```python
a.text
a.get_attribute('href')
```



