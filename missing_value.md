## Missing values

Missing values are often written as blanks, NaNs, None, or other. What do we do with those?

##### Detecting missing values 
It is easy to detect missing values if you have a `pandas` dataframe:

```
cols_with_missing = [col for col in train_data.columns if train_data[col].isnull().any()
```

A basic strategy is to discards rows or columns where the values are missing. 

However, a problem with that is that you might be losing valuable data points. It's usually better to impute missing data, i.e., by inferring it from the rest of the data.

##### Using Sklearn to impute data 

`sklearn` proposes two types of imputation: univariate and multivariate.
In the univariate case, we look along the missing i-th feature column to estimate the missing value. Use `sklearn.impute`'s `SimpleImputer()` class with either the `mean`, `median`, `constant`, or `most_frequent` strategy. Choose whichever makes most sense based on the type of data you have.

In the multivariate case, the entire set of available features is used to compute the missing value. In this case use `sklearn.impute`'s `IterativeImputer()` class, which is going to model each feature as a function of other features based on a round-robin linear regression model. 

##### Example with titanic data on Kaggle

For example, suppose you know that your `Age` and `Cabin` columns in your `df` pandas data frame has missing values, more specifically NaNs. 

```
#impute age
imp_mean = SimpleImputer(missing_values=np.nan, strategy='median')
age = train_data['Age'].to_numpy().reshape(-1, 1)
age_imp = imp_mean.fit_transform(age)

#impute cabin
imp_most_freq = SimpleImputer(missing_values=np.nan, strategy='most_frequent')
cabin = train_data['Cabin'].to_numpy().reshape(-1, 1)
cabin_imp = imp_most_freq.fit_transform(cabin)
```

Then replace the existing train data:
```
X_train_imp = np.copy(X_train)
X_train_imp[:, train_data.columns.get_loc("Age")] = np.squeeze(age_imp)
X_train_imp[:, train_data.columns.get_loc("Cabin")] = np.squeeze(cabin_imp)
X_train_imp[:, train_data.columns.get_loc("Embarked")] = np.squeeze(embarked_imp)
```