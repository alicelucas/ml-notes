#### One-hot encoding of categorical variables

We transform categorical variables into k - 1 binary variables. For example
if we have 9 different categories, then we end up with 8 binary variables.



Use `pd.get_dummies()` to get the one hot encoding.

The code to use is:

```
for var in vars_cat:
    
    # to create the binary variables, we use get_dummies from pandas
    
    X_train = pd.concat([X_train,
                         pd.get_dummies(X_train[var], prefix=var, drop_first=True)
                         ], axis=1)
    
    X_test = pd.concat([X_test,
                        pd.get_dummies(X_test[var], prefix=var, drop_first=True)
                        ], axis=1)
    

X_train.drop(labels=vars_cat, axis=1, inplace=True)
X_test.drop(labels=vars_cat, axis=1, inplace=True)

X_train.shape, X_test.shape
```

Note that `get_dummies()` is going to rename the variable name in the pandas array by
appending a `_` to the original category name. E.g. if a category `name` has values 
`a` or `b` or `c`, then we have two new columns named `name_a` and `name_b` with 
binary values `0` or `1`. The observations that had the category `c` assigned 
to them would take on values `0` in both `name_a` and `name_b` (since we 
went to `k - 1` binary variables for a category with `k` different values).



##### ! Warning when using get_dummies()!

Note that after this step, there may be a different number of features between
`X_test` and `X_train` because `X_test` might not have observations with a certain same
category that is present in `X_test`, so the corresponding binary column
won't show up in `X_test`. To remediate, add this column to `X_test` and 
assign a value of `0`. For example: ```X_test['embarked_Rare'] = 0```.


Note that now embarked_Rare will be at the end of the test set, 
which is a different order than that of the train set,
so in order to pass the variables in the same order, we will 
create a `variables` variable:

```variables = [c  for c in X_train.columns]```

and the next steps (variable scaling) will be operating on `X_train[variables]` and
`X_test[variables]`.