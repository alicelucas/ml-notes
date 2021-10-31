#### Handling missing categorical and numerical variables 

We first identify all missing values in the dataset using the `isnull.sum() > 0` check: 

``vars_with_na = [var for var in data.columns if data[var].isnull().sum() > 0]``

Display percentage of missing values in each variable using: 

``data[vars_with_na].isnull().mean().sort_values(ascending=False)``

##### Identify categorical variables that have missing values

``cat_na = [var for var in vars_cat if var in vars_with_na]``


##### Identify numerical variables that have missing values
``num_na = [var for var in vars_num if var in vars_with_na]``


#### Analyzing missing values
At this point, it is very important to figure out whether the missing variable is 
important or not for the prediction problem. What we thus do is the following:

For a given variable that we know has missing values, in `vars_with_na`, (you will do this for each feature that you know has missing observations), 
 go through all values and make an iterim variable that is `1` if the observation 
 is missing and `0` otherwise. Then for observations with value `1`, compute the mean and 
 std of the target variable, and do the same for the observations with 
 value `0`. Plot a histogram with the two bins (0 and 1). If the mean and std differs
  between the two groups, then this indicates that the missing variable has
   an impact on the price and is important for the prediction.
  If not, it means you could drop the feature. Otherwise, you'll have to do
  missing value imputation.
  
  Here is the code:
  ```
def analyse_na_value(df, var):

    # copy of the dataframe, so that we do not override the original data
    # see the link for more details about pandas.copy()
    # https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.copy.html
    df = df.copy()

    # let's make an interim variable that indicates 1 if the
    # observation was missing or 0 otherwise
    df[var] = np.where(df[var].isnull(), 1, 0)

    # let's compare the median SalePrice in the observations where data is missing
    # vs the observations where data is available

    # determine the median price in the groups 1 and 0,
    # and the standard deviation of the sale price,
    # and we capture the results in a temporary dataset
    tmp = df.groupby(var)[target].agg(['mean', 'std'])

    # plot into a bar graph
    tmp.plot(kind="barh", y="mean", legend=False,
             xerr="std", title=target, color='green')

    plt.show()
    
    
# let's run the function on each variable with missing data

for var in vars_with_na:
    analyse_na_value(data, var)
```

