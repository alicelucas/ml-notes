Ordinal encoding is not recommended for most classifiers, because these encoding might be interpreted as being ordered, so higher numbers will be weighed more in the loss. We don't want that! It's best to use one-hot encoding, also called dummy encoding. 

Convert categorical to one-hot encoding:
```
# Pandas
one_hot_encoded_test_X = pd.get_dummies(test_X)
one_hot_encoded_train_X = pd.get_dummies(train_X)
```

```
# Sklearn
enc = preprocessing.OneHotEncoder()
enc.transform(train_X).toarray()
enc.fit(train_X)
enc.transform(test_X).toarray()
```

Note that a nice advantage of using regression trees is that it is not needed to convert categorical variables. All that is needed is to define a splitting logic at a given node. 

Notes on level of cardiality:
You could choose to keep only categorical inputs that have a low level of cardinality, but that's a bit arbitrary. 
```
# Pandas
low_cardinality_cols = [cname for cname in candidate_train_predictors.columns if 
                                candidate_train_predictors[cname].nunique() < 10 and
                                candidate_train_predictors[cname].dtype == "object"]
numeric_cols = [cname for cname in candidate_train_predictors.columns if 
                                candidate_train_predictors[cname].dtype in ['int64', 'float64']]
my_cols = low_cardinality_cols + numeric_cols
train_X = train_X[my_cols]
test_X = test_X[my_cols]
```

If features are categorical with many values, look into Scikit-learn's FeatureHasher uses the hashing trick to store high-dimensional data. This will add some complexity to your modeling code.