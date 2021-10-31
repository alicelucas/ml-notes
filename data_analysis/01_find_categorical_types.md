Assuming a pandas array was obtained: `` data = pd.read_csv()``. Visualize with `data.head()`
#### Identifying categorical and numerical variables in a pandas dataset

The categorical variables usually have a type "Object". Thus you can find these variables with:

`cat_vars = [var for var in data.columns if data[var].dtype == 'O']`

which will return a list of the variable names that have been identified as categorical. 

Then cast all variables as categorical:

`data[cat_vars] = data[cat_vars].astype('O')`

Then once we have this, the numerical variables are easily identified with:

`num_vars = [
    var for var in data.columns if var not in cat_vars and var != target
]`

Note the `var != target` check is important, to make sure we don't put the target variable in the input.