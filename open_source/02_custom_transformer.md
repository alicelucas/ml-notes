What if the available open-source python packages do not provide one of the
transformations you'd like to apply on your dataset? You'll have to make your own 
class such that it is compatible with `Scikit-learn`'s `Transformer` class. 


##### Base classes in `scikit-learn`

All of your custom-made classes should inherit of the base classes of `sklearn`. For example,
your custom Transformer should inherit from `base.BaseEstimator` and `base.TransformerMixin` (see docs for details).

If you want your transformer to compute and store variables, then you also need
to inherit `base.BaseEstimator`: this will allow you to implement the `fit` method 
which will compute the stats of interest from your relevant features, and save them
in a dictionary that you can then access later.



##### Example from Titanic assignment

We need a custom transformer where we extract the first letter of the cabin. Our
transformer class looks like:

```
class ExtractLetterTransformer(BaseEstimator, TransformerMixin):
    # Extract fist letter of variable

    def __init__(self, variables):
        
        if not isinstance(variables, list):
            raise ValueError('variables should be a list')
        
        self.variables = variables

    def fit(self, X, y=None):
        # we need this step to fit the sklearn pipeline
        return self

    def transform(self, X):

        # so that we do not over-write the original dataframe
        X = X.copy()
        
        for feature in self.variables:
            X[feature] = X[feature].str[0]

        return X


```