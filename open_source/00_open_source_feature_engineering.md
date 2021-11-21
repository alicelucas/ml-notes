#### Open-source for feature engineering

It is highly recommended to use open-source libraries for feature engineering, 
instead of doing it manually ourselves. Manually computing the stats
of the training dataset and using these to then feature engineering the test dataset
is very inefficient and prone to error. That is because this implies copy-pasting the stats manually, 
or saving from somewhere, etc. 


Instead, we make use of `scikit-learn` and all of the classes it proposes for automated
feature engineering, which address all potential models. It also makes coding 
much easier. Using this library, we can do lost of things like 
ordinal encoding or imputing automatically, for example.

##### Scikit-learn `Transformer`

This class has the `fit()` method and the `transform()` method. It transforms data. Scalers, 
feature selectors, encoders, imputers, discretizers, and transformers all belong to that class.


##### Scikit-learn `Estimator`

A scikit-learn estimator is a class with a `fit()` and `predict()` method. Any ML algorithms
like lasso, decision treest, SVMs, are coded as estimators within `scikit-learn()`.


##### Scikit-learn `Pipeline`


A pipeline is a class that allows to run transformers and estimators in sequence. In a 
pipeline, we can accomodate several transformers, which will be run one after the other. 
Within the pipeline class, most steps are transformers, and the last step can be 
an estimator. 

In the end a pipeline is all we need for subsequent deployment, as it encapsulates
all the information we need in its class instance:

```
pipe.fit(X_train, y_train)
pipe.predict(X_train)
pipe.predict(X_test)
pipe.predict(live_data) #Any live data that comes our way
```

We can save an entire pipeline in just one `pickle` object. The next deployment step
just needs to load that one object, nothing else.

##### Other open-source 

Another feature-engineering open-source library worth looking into is "Feature Engine", which
includes many Transformers, more than what Scikit-learn offers. 

"Category Encoders" is another great open-source python libraries.

Note that transformers fom open-source other than sklearn CAN still be used 
as part of a Scikit-learn `Pipeline` object! You can even make your own custom Transformer, see section 02.


