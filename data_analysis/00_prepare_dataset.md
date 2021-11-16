Assuming a pandas array was obtained: `` data = pd.read_csv()``. Visualize with `data.head()`

#### Prepare dataset 

The examples below are from the Titanic dataset. 

##### Replace question marks by NaN

`data = data.replace('?', np.nan)`


##### Cast numerical variables as float if not already
```
# cast numerical variables as floats

data['fare'] = data['fare'].astype('float')
data['age'] = data['age'].astype('float')
```

##### Drop unnecessary variables
```
# drop unnecessary variables

data.drop(labels=['name','ticket', 'boat', 'body','home.dest'], axis=1, inplace=True)

# display data
data.head()
```


##### Save out new dataset
`data.to_csv('titanic.csv', index=False)`