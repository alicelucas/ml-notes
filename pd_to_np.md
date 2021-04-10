Getting data from a pandas frame as a numpy array is easy:

```
X = df.to_numpy()
```

Note that if you need the index of a particular column name in the pandas data frame, you caneasily retrieve it with `.get_loc()`:

```
idx = df.columns.get_loc(name)
```
