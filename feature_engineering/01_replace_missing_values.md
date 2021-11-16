##### Numerical variables

For a numerical feature for which we have missing values, we (1) keep 
track of the observations that were missing using a binary indicator
 and (2) replace the missing values by the mean of that feature over all observations.
 
 ```
#Suppose num_na is ["age", "fare"]

for var in num_na:

    # calculate the mean using the train set
    mean_val = X_train[var].mean()
    
    print(var, mean_val)

    # add binary missing indicator (in train and test)
    X_train[var + '_na'] = np.where(X_train[var].isnull(), 1, 0)
    X_test[var + '_na'] = np.where(X_test[var].isnull(), 1, 0)

    # replace missing values by the mean
    # (in train and test)
    X_train[var].fillna(mean_val, inplace=True)
    X_test[var].fillna(mean_val, inplace=True)

# check that we have no more missing values in the engineered variables
X_train[num_na].isnull().sum()
``` 


##### Categorical variables

With categorical variables that have a lot of missing data, 
we replace the observations with the string "Missing.":

```
X_train[vars_cat] = X_train[vars_cat].fillna('Missing')
```
Chek that no remaining value is NA with: `X_train.isnull().sum()`.


For categorical variables that have relatively few missing data, we
replace the mising data with the most frequent category. 