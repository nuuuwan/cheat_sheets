# Python

## re

```python
r'(?P<first>\w+) (?P<last>\w+)'
result = re.search(REGEX_MEDIA_URL, URL)
result_data = result.groupdict()
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

## xml

```python
import xml.etree.ElementTree as ET
tree = ET.parse(xmlfile)
root = tree.getroot()

tree = ET.fromstring(xml_as_string)

```

```python
_html = ET.Element('html')
_head = ET.SubElement(_html, 'head')
_link = ET.SubElement(_head, 'link', {
    'rel': 'stylesheet',
    'href': '../styles.css',
})
```

## unittest

```python
assertIsNone(x)
assertIsNotNone(x)
assertIn(a, b)
assertIsInstance(a, b)
assertRaises(...)
assertAlmostEqual(a, b)
assertGreater(a, b)
assertListEqual(a, b)
assertDictEqual(a, b)
```

## logging
```python
logging.basicConfig(
  filename='utils-nuuuwan',
  level=logging.DEBUG,
)
```

## argparse
```python
import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument(
  'integers',  # name (or flags)
  help='an integer'),
  type=int,
  default=12,
  required=True,
)
args = parser.parse_args()
```

