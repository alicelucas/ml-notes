#### The challenges of continuous data
Always keep in mind that the contribution of an input depends heavily on its variability relative to other inputs. It is therefore crucial that the continuous data ends up having a distribution similar to the other inputs in the dataset. 

#### Recommended steps for pre-processing continuous features
Follow theses steps :
- Rescale the continuous features to be in the `[-1, 1]` range.
- Standardize the continuous features such that their mean is `0` and variance is `1`. See `standardization.md` for more information on how to do that with `scitkit`.

If these continuous variables are to be mixed with categorical variables, make sure to read `mixed_inputs.md`.

#### Dividing by two standard deviations if used with binary variables
In the case in which the continuous inputs are to be used with binary inputs, some ML advocates recommend to scale the variables by two standard deviations (instead of one standard deviation). 

#### When to discretize continuous inputs
In some cases, it might be worth considering discretizing continuous inputs into bins. The resulting one-hot encoded features can make a model more expressive, while maintaining interpretability. Furthermore, discretizing these features can introduce non-linearity to linear models. 


