In many ML algorithms, it is fine to combine both continuous and categorical data in the input data -- as long as preprocessing is one such that all features have similar distributions. After this step, the algorithm will not know whether the inputs are continuous or binary.

If presented with continuous and categorical inputs, do the following:
- standardize inputs as described in `continuous_inputs.md`
- encode categorical variables by using multiple boolean features as described in `categorial_inputs.md`. You may use either dummy coding or effect coding.

The most important thing is to make sure that categorical data and continuous data are in the same range, at the end of the day. For example if using one-hot encoded categorical data, it may be best to have the continuous features standardized to the [0, 1] range.