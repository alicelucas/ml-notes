#### Separate train and test set

Do this before any feature engineering. 

Using sklearn's `model_selection` module which incldues a 
`train_test_split`:

```
X_train, X_test, y_train, y_test = train_test_split(
    data.drop('survived', axis=1),  # predictors
    data['survived'],  # target
    test_size=0.2,  # percentage of obs in test set
    random_state=0)  # seed to ensure reproducibility

X_train.shape, X_test.shape
```

The feature engineering steps will be done on these pandas array (not on the original pandas `data`).


When you apply a feature engineering step, always use stats from the `X_train` dataset
and apply the resulting transformation to your `X_test` dataset as well.
That is because we don't want any "knowledge" of the `X_test` dataset to leak into the `X_train` dataset.