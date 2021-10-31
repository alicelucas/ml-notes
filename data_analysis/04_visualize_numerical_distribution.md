#### Visualizing distribution of numerical variables


Visualize numerical variables with:
```
print('Number of numerical variables: ', len(num_vars))

# visualise the numerical variables
data[num_vars].head()
```

##### Temporal variables

If we have multiple temporal variables, it's usually a good idea
to use relative values of these temporal variables
 (e.g. by subtracting one from another) than using the absolution
 temporal values. E.g. in the House Price prediction problem, 
 it's best to capture the amount of time that has passed
 between a house build and house sold than using these two numbers
 individually. 
 
 
 ##### Discrete variables  
 
 Find discrete variables with 
 
 ```
#  let's make a list of discrete variables
discrete_vars = [var for var in vars_num if len(
    data[var].unique()) < 20]
```
 
 and visualize with `data[discrete_vars].head()`.
 
 Some discrete variables may correspond to "quality" variables. 
 It might be a good idea to map each value to an actual score, 
 and visualize whether higher/lower scores has an impact on the target value, to complete your analysis.
 
 ##### Continuous variables 
 
 Find the continuous variables with 
 
 ```
# make list of continuous variables
cont_vars = [
    var for var in vars_num if var not in discrete_vars]
```

and visualize with `data[cont_vars].head()`.
    
Plot the histogram of these continuous variables: 
````
# lets plot histograms for all continuous variables

data[cont_vars].hist(bins=30, figsize=(15,15))
plt.show()
````

Look at whether the variables are normally distributed or skewed. If highly skewed (e.g. 0s or not 0s), 
you can apply a binary transformation to improve the predictive power
of your model. Other things you can do to skewed variables are a logarithmic transformation
or a Yeo-Johnson transformation. Apply these transformations and see if the 
variables are more Gaussian-looking as a result. 
 
Note that regardless of visualization results, this does not guarantee improved model performance. 
But if transformations during visualization revealed better looking distributions it's worth trying one experiment with transformed features, and
one experiment without, to see whether it does improve things. 