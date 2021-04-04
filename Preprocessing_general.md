Reading csv file:
```
# Pandas
train_data = pd.read_csv(filename)
```

Removing label column from data to obtain train data:
```
# Pandas
train_X = train_data.drop(['targetCol'], axis=1)
```