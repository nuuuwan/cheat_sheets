# Python - bs4 (Beautiful Soup)

```python
from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')
```

```python
elem.name == 'h1'

soup.find_all('div', class_='table-row')
soup.find_all('a', href=True):
soup.find_all(attrs={'name' : 'stainfo'})
```

```python
a_link.get('href')
```
