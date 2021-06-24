# Python MatPlotLib


## Simple Plot
```python
import matplotlib.pyplot as plt
...
plt.plot(x, y, color='red')

fig = plt.gcf()
fig.set_size_inches(8, 4.5)

plt.show()
```


## Formatting Axis Labels

```python
import matplotlib.ticker as tkr

ax = plt.gca()
ax.get_yaxis().set_major_formatter(
    tkr.FuncFormatter(lambda x, p: format(int(x), ','))
)

fig = plt.gcf()
fig.autofmt_xdate()

```
