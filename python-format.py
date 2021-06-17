# Python - Format

Original Source: https://www.w3schools.com/python/ref_string_format.asp

## Basic Usage

```python
txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
txt2 = "My name is {0}, I'm {1}".format("John",36)
txt3 = "My name is {}, I'm {}".format("John",36)
```


## Formatting Types

```bash
:< 	Left aligns the result (within the available space)
:> 	Right aligns the result (within the available space)
:^ 	Center aligns the result (within the available space)
:= 	Places the sign to the left most position
:+ 	Use a plus sign to indicate if the result is positive or negative

:- 	Use a minus sign for negative values only
:  	Use a space to insert an extra space before positive numbers (and a minus sign before negative numbers)
:, 	Use a comma as a thousand separator
:_ 	Use a underscore as a thousand separator
:b 	Binary format

:c 	Converts the value into the corresponding unicode character
:d 	Decimal format
:e 	Scientific format, with a lower case e
:E 	Scientific format, with an upper case E
:f 	Fix point number format

:F 	Fix point number format, in uppercase format (show inf and nan as INF and NAN)
:g 	General format
:G 	General format (using a upper case E for scientific notations)
:o 	Octal format
:x 	Hex format, lower case

:X 	Hex format, upper case
:n 	Number format
:% 	Percentage format
```
