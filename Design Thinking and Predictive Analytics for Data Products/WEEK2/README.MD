# Review: Getting Feature  
1.W​hy do we use one-hot encoding?  
B​ecause label encoding assumes an order to categorical variables (i.e. the higher, the better)  
T​o get a better representation of categorical variables in a dataset  
2.Y​ou want to build a piecewise model based on days of the week. Which of the following could be the one-hot encoding for this model's features?  
```html
M​onday: [1, 1, 0, 0, 0, 0, 0]
T​uesday: [1, 0, 1, 0, 0, 0, 0]
Wednesday: [1, 0, 0, 1, 0, 0, 0]
Thursday: [1, 0, 0, 0, 1, 0, 0]
Friday: [1, 0, 0, 0, 0, 1, 0]
Saturday: [1, 0, 0, 0, 0, 0, 1]
```
# Review: Working with Features
1.W​hy is it okay if we transform features for linear models, but not the parameters?  
A​rbitrary combinations of features will not modify the linearity of the parameters  
L​inear models also need linear parameters  
2.W​hich of the following are reasonable estimates to replace missing values (for missing data imputation)?  
A​ value placed by an additional prediction  
T​he average of all instances of that feature  
T​he average of all instances of some subgroup  
T​he median of all instances of that feature  
# Quiz:Features
1.Which of the following matrices could be used in one-hot encoding for a 5-dimensional dataset?  
[0, 0, 1, 0]  
(One-hot encoding means that there is only a single “1” in the matrix.)  
2.Why is it more difficult to create a linear regression model for categorical features?  
Because the outputs are not quantitative  
(Categorical features are qualitative and so you must use one-hot encoding or other techniques to measure them.)  
(NOT RIGHT:   
Because categorical features must be measured with two lines or more. You can capture categorical features with a single line.  
)   
3.What is the limitation of feature transformations in linear models?  
We can make different combinations of features, but not parameters  
(This is also equivalent to saying that the linear models may only have linear parameters.)  
4.W​hich of the following can be good strategies for dealing with missing data?  
M​odeling: change our regression/classification algorithms to explicitly deal with missing values.   
(We change our regression/classification algorithms to explicitly deal with missing values. For example, we can add a feature to flag whether a value is missing.)  
F​iltering: discard missing values  
(We can simply discard missing values in some cases.)  
M​issing Data Imputation: fill in missing data with reasonable estimates.  
 (We fill in missing data with reasonable estimates. More advanced schemes include computing the average of subgroups or training a predictor to fill in missing values.)  
 5.W​hy shouldn't we simply discard every instance that has a missing value in the data?  
 I​f many features are missing, we can end up tossing out a large percentage or even all of the dataset.  
