##### Should feature selection be made part of the pipeline?

Integrating feature selection as part of our (fixed) pipeline is suitable when:


- We build and refresh the model on the same data.
- We train our model on small datasets (small amount of features).


It is not suitable when: 

- Your dataset as a very high feature space. 
- You are continuously enriching the data with new data sources.
 
 
 If doing feature selection prior to defining the pipeline, then your lists
 from the previous section should be updated with only the variables that you
 decided to include. This will do feature engineering only on the selected features. 