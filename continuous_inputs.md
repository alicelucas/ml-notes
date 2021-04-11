If dealing with continuous input data, don't forget to standardize these features such that their mean is 0 and their variance is 1. You want all of your inputs to be roughly on the same scale.

Always keep in mind that the contribution of an input depends heavily on its variability relative to other inputs. 

If the continuous inputs are to be combined with binary inputs, it is recommended to scale the variables by two standard deviations (instead of 1). This is so the resulting distribution is comparable to that of the binary variables. 

In some cases, it might be worth considering discretizing continuous inputs into bins. The resulting one-hot encoded features can make a model more expressive, while maintaining interpretability. Furthermore, discretizing these features can introduce non-linearity to linear models. 
