In many ML algorithms, it is fine to combine both continuous and categorical data in the input data -- as long as preprocessing is one such that all features have similar distributions. After this step, the algorithm will not know whether the inputs are continuous or binary.

If presented with continuous and categorical inputs, do the following:
- standardize inputs as described in `continuous_inputs.md`
- encode categorical variables by using multiple boolean features as described in `categorial_inputs.md`. Use effect coding instead of dummy coding.


Using effect coding instead of dummy coding is particularly important because it allows you to represent all of your features in a single vector, and then use any off-the-shelf package for classification/regression. 