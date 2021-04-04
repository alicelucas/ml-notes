Missing values are often written as blanks, NaNs, None, or other. What do we do with those?

A basic strategy is to discards rows or columns where the values are missing. 
[PANDAS]
--> train_data.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)
--> axis specifies whether you'd like to drop rows or columns. 

Identify any missing columns with pandas:
--> cols_with_missing = [col for col in train_data.columns 
                                 if train_data[col].isnull().any()] 
--> You can now drop any column you'd like, for example:  train_data.drop(['Id'] + cols_with_missing, axis=1) 

However, a problem with that is that you might be losing valuable data points. It's usually better to impute missing data, i.e., by inferring it from the rest of the data. There exists two types of imputation: univariate and multivariate. In the univariate case, we look along the missing i-th feature column to estimate the missing value. In the multivariate case, we use the entire set of available features to compute the missing value. 