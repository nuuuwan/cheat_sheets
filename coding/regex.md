# Regex

Also, use https://pythex.org

## Usage Patterns in Python (by nuuuwan)

### Named Groups
```python
RE_NAME = r'(?P<first_name>\w+)\s(?P<last_name>\w+)'
s = 'Albert Einstein'
result = re.match(RE_NAME, s)
if result:
  result_data = result.groupdict()
  first_name = result_data['first_name']
  last_name = result_data['last_name']
```

### Substitute

```python
s = 'Albert      Einstein'
s = re.sub(r'\s+', ' ', s)
print(s)  # "Albert Einstein" (replaces multiple spaces with single spaces)
```

### Does string match

```python
RE_NAME = r'(?P<first_name>\w+)\s(?P<last_name>\w+)'
s = 'Albert Einstein'
result = re.match(RE_NAME, s)
if bool(result):
  print('String matches!')
```

...

(Based on https://medium.com/factory-mind/regex-tutorial-a-simple-cheatsheet-by-examples-649dc1c3f285, with @nuuuwan's notes and additions)

## Basic Topics

### Anchors — ^ and $

```bash
^The        matches any string that starts with The
end$        matches a string that ends with end
^The end$   exact string match (starts and ends with The end)
roar        matches any string that has the text roar in it
```

### Quantifiers — * + ? and {}

```bash
abc*        matches a string that has ab followed by zero or more c
abc+        matches a string that has ab followed by one or more c
abc?        matches a string that has ab followed by zero or one c
abc{2}      matches a string that has ab followed by 2 c
abc{2,}     matches a string that has ab followed by 2 or more c
abc{2,5}    matches a string that has ab followed by 2 up to 5 c
a(bc)*      matches a string that has a followed by zero or more copies of the sequence bc
a(bc){2,5}  matches a string that has a followed by 2 up to 5 copies of the sequence bc
```

### OR operator — | or []
```bash
a(b|c)     matches a string that has a followed by b or c (and captures b or c)
a[bc]      same as previous, but without capturing b or c
```

#### "Capturing"
```python
import re
re.match(r'a[bc]', 'abc').groups()
# returns ()
re.match(r'a(b|c)', 'abc').groups()
# returns ('b',)
```

### Character classes — \d \w \s and
```bash
\d         matches a single character that is a digit
\w         matches a word character (alphanumeric character plus underscore)
\s         matches a whitespace character (includes tabs and line breaks)
.          matches any character
\D         matches a single non-digit character
\$\d       matches a string that has a $ before one digit
```


## Intermediate topics

### Grouping and capturing — ()

```bash
a(bc)           parentheses create a capturing group with value bc
a(?:bc)*        using ?: we disable the capturing group
a(?P<foo>bc)     using ?P<foo> we put a name to the group
```

### Bracket expressions — []

```bash
a(bc)           parentheses create a capturing group with value bc
a(?:bc)*        using ?: we disable the capturing group
a(?P<foo>bc)     using ?P<foo> we put a name to the group
```

### Greedy and Lazy match

```bash
<.+?>            matches any character one or more times included inside < and >, expanding as needed
<[^<>]+>         matches any character except < or > one or more times included inside < and >
```

### Boundaries — \b and \B

```bash
\babc\b          performs a "whole words only" search
\Babc\B          matches only if the pattern is fully surrounded by word characters
```

## Advanced topics

### Back-references — \1

```bash
([abc])\1              using \1 it matches the same text that was matched by the first capturing group
([abc])([de])\2\1      we can use \2 (\3, \4, etc.) to identify the same text that was matched by the second (third, fourth, etc.) capturing group
(?P<foo>[abc])\k<foo>   we put the name foo to the group and we reference it later (\k<foo>). The result is the same of the first regex
```

### Look-ahead and Look-behind — (?=) and (?P<=)

```bash
d(?=r)       matches a d only if is followed by r, but r will not be part of the overall regex match
(?P<=r)d      matches a d only if is preceded by an r, but r will not be part of the overall regex match
d(?!r)       matches a d only if is not followed by r, but r will not be part of the overall regex match
(?P<!r)d      matches a d only if is not preceded by an r, but r will not be part of the overall regex match
```
