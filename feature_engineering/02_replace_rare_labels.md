##### Rare labels in categorical variables

For variables that have categories with less than 5% occurence in the observation, replace
these observations with the string "Rare."

The code for finding such rare occurences is:

```
def find_frequent_labels(df, var, rare_perc):
    
    # function finds the labels that are shared by more than
    # a certain % of the passengers in the dataset
    
    df = df.copy()
    
    tmp = df.groupby(var)[var].count() / len(df)
    
    return tmp[tmp > rare_perc].index


```

And code for replacing the categories with the string "Rare":

```
for var in vars_cat:
    
    # find the frequent categories
    frequent_ls = find_frequent_labels(X_train, var, 0.05)
    
    # replace rare categories by the string "Rare"
    X_train[var] = np.where(X_train[var].isin(
        frequent_ls), X_train[var], 'Rare')
    
    X_test[var] = np.where(X_test[var].isin(
        frequent_ls), X_test[var], 'Rare')
```


Check the number of unique categories for each categorical variable with: 

```X_train[vars_cat].nunique()```

and 

```X_test[vars_cat].nunique()```