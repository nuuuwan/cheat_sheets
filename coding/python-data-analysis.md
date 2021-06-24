# Python Data Analysis

## Read from Excel

```python
import pandas as pd
df = pd.read_excel(
  'test.xlsx',
  sheet_name='Sheet 1',
  engine='openpyxl',
)
```

## Write to CSV

```python
df.to_csv('test.csv')
```

...
## References and Notes
