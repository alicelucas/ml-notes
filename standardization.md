## Standardization

The machine learning estimators in `sklearn` expect that the distribution of the data follows a Gaussian with zero mean and unit variance. 

Why is this necessary? During learning, the objective function assumes that all features are centered around zero and have a unit variance. If that is not the case, then a feature that is orders of mangnitude larger than another might be counted much more in the objective learning, preventing us to learn from the other features. 

`Scikit-learn`'s `preprocessing` module provides many helpful tools for standardization. 

#### Using sklearns `StandardScaler()`

You would use the following lines of code:
```
from sklearn import preprocessing
import numpy as np

#... Assume we have X_train

scaler = preprocessing.StandardScaler().fit(X_train)
X_scaled = scaler.transform(X_train)
```

If you were to inspect `X_scaled.mean(axis=0)` and `X_scaled.std(axis=0)`, you will see that all features have mean 0 and variance of 1. 

Note that when standardizing the testing dataset, you should be using the scaler obtained from the training dataset. 

#### Using `sklearn's` `MinMaxScaler() or MaxAbsScaler()`

There are cases in which we may want to just scale fetures so that are between a minimum and maximum, or such that each feature is scaled to unit size.

This is preferable in several cases, including:
 - when the original features have very small standard deviations
 - when we want to preserve zero entries in sparse data
 
 
 `MinMaxScaler()` will scale the data to the `[0, 1]` range. `MaxAbsScaler()` assumes that the data is centered around 0, and will scale the data to the [-1, 1] range. The `MaxAbsScaler` scaler is the recommended scaler to use for sparse data because it will not destroy the sparseness structure of the original data.
 
  

