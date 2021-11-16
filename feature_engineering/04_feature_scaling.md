##### Standard scaling

After having one-hot encoded the categorical variables and kept the numerical variables as is, 
we can use standard scaling which computes the standard deviation and the mean
of each feature, and subtract and scales these from each obsevation for that feature. 

We use `StandardScaler()` from `Scikit-learn`. 

```
# create scaler
scaler = StandardScaler()

#  fit  the scaler to the train set
scaler.fit(X_train[variables]) 

# transform the train and test set
X_train = scaler.transform(X_train[variables])

X_test = scaler.transform(X_test[variables])
```