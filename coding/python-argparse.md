# Python - Argparse

```python
import argparse
def get_options():
    parser = argparse.ArgumentParser()
    parser.add_argument('pdf_file', type=str)
    parser.add_argument('start_page', type=int)
    parser.add_argument('end_page', type=int)
    return parser.parse_args()  
```

```bash
>> python pdf_split.py hellow.pdf 1 20
Namespace(pdf_file='hellow.pdf', start_page=1, end_page=20)
```

```bash
>> python pdf_split.py hellow.pdf 1
usage: pdf_split.py [-h] pdf_file start_page end_page
pdf_split.py: error: the following arguments are required: end_page
```
