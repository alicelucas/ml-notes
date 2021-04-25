Below is an example of using Pandas if you wanted to keep only categorical inputs that have a low level of cardinality. 
```
# Pandas
low_cardinality_cols = [cname for cname in candidate_train_predictors.columns if 
                                candidate_train_predictors[cname].nunique() < 10 and
                                candidate_train_predictors[cname].dtype == "object"]
train_X = train_X[low_cardinality_cols]
test_X = test_X[my_cols]
```

If you do want to encode categorical features that have many categories, look into Scikit-learn's `FeatureHasher` uses the hashing trick to store high-dimensional data. This will add some complexity to your modeling code.

