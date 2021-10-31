#### Compute cardinality in categorical variables

##### Visualizing cardinality of data

To plot how many different categories are present in each categorical variable:

``data[cat_vars].nunique().sort_values(ascending=False).plot.bar(figsize=(12,5))``

The y-axis on the bar shot is the number of unique values, for each variable.

##### Dealing with variables of high cardinality
If there is  variable with a very high cardinality, it's important to think about ways to reduce this cardinality. E.g. in the titanic dataset, 
the Cabin variable has high cardinality (~150 different categories). But
the cardiality can be dropped to much lower by only using the first letter
of the cabin, and ignoring the digits after the letter.

(To reduce cardinality, you could also use Scikit-learn's `FeatureHasher` that uses the hashing trick to store high-dimensional data.) 

If no other option, you could also choose to drop these variables with high cardinality, to avoid any problem during training.

##### Dealing with variables of low cardinality 

If the cardinality of a categorical variable is low, you're in luck, then no need to do further action for now.

 