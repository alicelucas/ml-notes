##### Measures for evaluating a classifier (logistic regression) model

When evaluating a classifier model, typically we look at the ROC-AUC and at the accuracy/
The ROC-AUC looks at the predicted probability, while the accuray look as the final predicted
`0` or `1` label. 


##### Make predictions on train and  test set

```
# make predictions for train set
class_ = model.predict(X_train)
pred = model.predict_proba(X_train)[:,1]

# determine mse and rmse
print('train roc-auc: {}'.format(roc_auc_score(y_train, pred)))
print('train accuracy: {}'.format(accuracy_score(y_train, class_)))
print()

# make predictions for test set
class_ = model.predict(X_test)
pred = model.predict_proba(X_test)[:,1]

# determine mse and rmse
print('test roc-auc: {}'.format(roc_auc_score(y_test, pred)))
print('test accuracy: {}'.format(accuracy_score(y_test, class_)))
print()
```

