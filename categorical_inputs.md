#### Encodings of categorical variables

There seems to be two school of thoughts when it comes to one-hot encoding. Given a categorical variable, you have two choices:

If categorical variables are to be mixed with continuous inputs, make sure to read `mixed_inputs.md` first.

#### Encoding

Ordinal encoding is not recommended for most classifiers, because these encoding might be interpreted as being ordered, so higher numbers will be weighed more in the loss. We don't want that! It's best to use one-hot encoding, also called dummy encoding. 


#### One-hot encoding

- In this case if the categories are (female, male), then your feature becomes either `[0, 1]` or `[0, 1]`.

```
# Pandas
one_hot_encoded_test_X = pd.get_dummies(test_X)
one_hot_encoded_train_X = pd.get_dummies(train_X)
```

```
# Sklearn
enc = preprocessing.OneHotEncoder()
enc.transform(train_X)
```

For non-regularized regression and in some learning models, co-linearity can be a problem as it may cause non-invertible covariance matrices. This will be the case for example if you use linear regression or GLMs using maximum likelihood. In such cases you can add a `drop="first"` or `drop="if_bibary"` to the arguments of `OneHotEncoder` to drop a category. Note that this applies only if the regression problem is not regularized. 

#### Effect coding

Represent the features as multiple boolean features. If the categories are (female, male) then you end up having two features, each of them either `-1` or `1`. Such coding is called "effect coding" and is sometimes recommended over "dummy codding" which using `0` or `1`.


#### Regression trees and random forests
Note that a nice advantage of using regression trees is that it is not needed to convert categorical variables. All that is needed is to define a splitting logic at a given node. 



#### Ordinal data

Imagine that you have a feature that is a number of something, e.g. a number of siblings on the Titanic boat. There are two approaches:
- you could treat the feature as continuous, and in this case see `continuous_inputs.md`. 
- or you could treat the features as categorical, in which case you would encode them for example with one-hot encoding. Note however that this would ignore the ordered nature of the variable. 