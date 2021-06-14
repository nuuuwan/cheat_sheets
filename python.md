# Python

## re

```python
r'(?P<first>\w+) (?P<last>\w+)'
result = re.search(REGEX_MEDIA_URL, URL)
result.groupdict()
```

## os

```python
os.path.exists
os.path.join
os.mkdir
for root_dir, sub_dirs, files in os.walk(PATH):
    …
os.path.isdir
file_name, ext = os.path.splitext(file_path)
```

## shutil (High-level file operations)

```python
shutil.move(src, dst, … )
shutil.copytree(src, dst, … )
shutil.rmtree
shutil.copy(src, dst, … )
```

## bs4 (Beautiful Soup)

```python
from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')

elem.name == 'h1'

soup.find_all('div', class_="table-row")
soup.find_all('a', href=True):


```

## xml

```python
import xml.etree.ElementTree as ET
tree = ET.parse(xmlfile)
root = tree.getroot()
```

## unittest

```python
assertIsNone(x)
assertIsNotNone(x)
assertIn(a, b)
assertIsInstance(a, b)
assertRaises
assertAlmostEqual(a, b)
assertGreater(a, b)
assertListEqual(a, b)
assertDictEqual(a, b)
```
