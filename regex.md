# Regex

Source: [https://medium.com/factory-mind/regex-tutorial-a-simple-cheatsheet-by-examples-649dc1c3f285]

## Anchors — ^ and $

```bash
^The        matches any string that starts with The -> Try it!
end$        matches a string that ends with end
^The end$   exact string match (starts and ends with The end)
roar        matches any string that has the text roar in it
```

## Quantifiers — * + ? and {}

```bash
abc*        matches a string that has ab followed by zero or more c -> Try it!
abc+        matches a string that has ab followed by one or more c
abc?        matches a string that has ab followed by zero or one c
abc{2}      matches a string that has ab followed by 2 c
abc{2,}     matches a string that has ab followed by 2 or more c
abc{2,5}    matches a string that has ab followed by 2 up to 5 c
a(bc)*      matches a string that has a followed by zero or more copies of the sequence bc
a(bc){2,5}  matches a string that has a followed by 2 up to 5 copies of the sequence bc
```

## OR operator — | or []
```bash
a(b|c)     matches a string that has a followed by b or c (and captures b or c) -> Try it!
a[bc]      same as previous, but without capturing b or c
```

## Character classes — \d \w \s and
```bash
\d         matches a single character that is a digit -> Try it!
\w         matches a word character (alphanumeric character plus underscore) -> Try it!
\s         matches a whitespace character (includes tabs and line breaks)
.          matches any character -> Try it!
\D         matches a single non-digit character -> Try it!
\$\d       matches a string that has a $ before one digit
```

## Grouping and capturing — ()

```bash
a(bc)           parentheses create a capturing group with value bc -> Try it!
a(?:bc)*        using ?: we disable the capturing group -> Try it!
a(?<foo>bc)     using ?<foo> we put a name to the group -> Try it!
```

## Bracket expressions — []

```bash
a(bc)           parentheses create a capturing group with value bc -> Try it!
a(?:bc)*        using ?: we disable the capturing group -> Try it!
a(?<foo>bc)     using ?<foo> we put a name to the group -> Try it!
```

## Greedy and Lazy match

```bash
<.+?>            matches any character one or more times included inside < and >, expanding as needed -> Try it!
<[^<>]+>         matches any character except < or > one or more times included inside < and > -> Try it!
```

## Boundaries — \b and \B

```bash
\babc\b          performs a "whole words only" search -> Try it!
\Babc\B          matches only if the pattern is fully surrounded by word characters -> Try it!
```

## Back-references — \1

```bash
([abc])\1              using \1 it matches the same text that was matched by the first capturing group -> Try it!
([abc])([de])\2\1      we can use \2 (\3, \4, etc.) to identify the same text that was matched by the second (third, fourth, etc.) capturing group -> Try it!
(?<foo>[abc])\k<foo>   we put the name foo to the group and we reference it later (\k<foo>). The result is the same of the first regex -> Try it!
```

## Look-ahead and Look-behind — (?=) and (?<=)

```bash
d(?=r)       matches a d only if is followed by r, but r will not be part of the overall regex match -> Try it!
(?<=r)d      matches a d only if is preceded by an r, but r will not be part of the overall regex match -> Try it!
d(?!r)       matches a d only if is not followed by r, but r will not be part of the overall regex match -> Try it!
(?<!r)d      matches a d only if is not preceded by an r, but r will not be part of the overall regex match -> Try it!
```
