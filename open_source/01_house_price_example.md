##### Libraries used for feature engineering in house-price model prediction

We can use `feature_engine` library's imputers: `AddMissingIndicator`, `MeanMedianImputer`,
`CategoricalImputer`. 

Use their encoders: `RareLabelEncoder` and `OrdinalEncoder`.


Use their transformers: `LogTransformer`, `YeoJohnsonTransformer`.
 
 All these
are engineering steps that were done manually before, but here we are letting the 
libraries do their thing. 


Use `MinxMaxScaler` and `Binarizer` from `sklearn.preprocessing`.

##### Example: Imputing categorical variables with `CategoricalImputer`

We still need to manually find what features have observations with a lot of missing values
and save that out in a `with_string_missing` list. Then we do:

```
cat_imputer_missing = CategoricalImputer(
                            imputation_method = "missing",
                            variables=with_string_missing)
X_train = cat_imputer_missing.transform(X_train)
X_test = cat_imputer_missing.transform(X_test)
```

This will replace all NA variables with the "Missing" label. 

If we wanted to replace values with most frequent category instead, then we would first 
save the variables in a `with_fequent_category` list (those are the features that had
less than 10% of missing values) and we then can do:


```
cat_imputer_frequent = CategoricalImputer(
                            imputation_method = "frequent",
                            variables=with_frequent_category)
X_train = cat_imputer_frequent.transform(X_train)
X_test =cat_imputer_frequent.transform(X_test)
```

This will compute in the background the most frequent category for the feature
in question, and use it to impute the variable that needs it. 


##### Example: Adding missing indicator with `AddMissingIndicator`

 As usual, first the features that are numerical that have NA should be stored in a list 
 `vars_with_na`. Then we add a feature that corresponds to the missing indicator:
 
 
 ```
missing_ind = AddMissingIndicator(variables=vars_with_na)
missing_ind.fit(X_train)
X_train = missing_ind.transform(X_train)
X_test = missing_ind.transform(X_test)
```

This adds new features corresponding to an indicator for missing numerical variables. 



##### Saving and loading the class instance 
The parameters stored in the different class instances can be saved and loaded later, 
so that we can access the stats predicted on the train dataset easily (instead
of explicitly writing out these stats). E.g. the `missing_ind` object can be saved, to be
re-used later. That is the case for all the other classes that are used in the feature-engineering step. 



##### Conclusion
- Code is much simpler and less prone to bug. 
- We have options to save classes and load them later. 

Note that we can still simplify all of this even more, if we put all the transformations
within a single pipeline. Then we won't have to apply each class (each transformation or imputation)
to the new test data. We will just be saving out the whole `scikit-learn` pipeline, 
and that is what will be saved and loaded. 


##### Question: what if we need to a apply a transformation that is not offered by one of our open-source libraries?
We will need to implement our class ourselves. See next section (02). 