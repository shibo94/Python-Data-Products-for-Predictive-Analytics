#  Review: Setting Up a Codebase

1.W​hat are some of the ways Professor McAuley cleaned his dictionary of words for sentiment analysis?  
R​emoving punctuation  
(You can filter this out with a simple if-statement.)   
R​emoving capitalization  
(You can do this easily with string methods like lower() or upper().)  
Identifying a subset of the most popular words  
(We can do this with a little list manipulation and sort().)  
S​temming  
(Here we use the Porter Stemmer from Python's NLTK.)  


# Review: Regularization

1.Fill in the blank: "T​o avoid overfitting, the model should ideally have ____ ____ and ____ ____."  

h​igh accuracy; low complexity  

2.W​hich of the following are good measurements of complexity in a model?  


C​ount the number of non-zero parameters in theta
(the L1 norm measures.)   

Measure the amount of variance in the parameters
(Also what the L2 norm measures.)

# Diagnostics for Data
1.W​hat is the MSE?
T​he sum of the squared differences between actual and predicted values, divided by the number of values.

2.G​iven a list of predictions and corresponding list of actual values, write a function named MSE to compute the MSE. You may reference other questions or videos. You do not need to account for edge cases here.
M​ethod Header:
Y​ou may copy and paste this to start your code below.
```html
def MSE(pred, actual):
```
| Input	      |Output (MSE)     |
| ---------- | :-----------:  |
| P​rediction A: [1, 222, 55, 77, 33, 41]	     | 8340.546666666667   |
| Actual A: [1, 21, 5, 7, 3.2, 4.2]		     |    |
| P​rediction B: [1, 2, 3, 4]		     | 5   |
| Actual B: [4, 3, 2, 1]		     |   |

3.G​iven a MSE in the features of 0.2 and a variance in the labels of 0.8, what would the R^2 statistic be?
0.75
equation 1 - (MSE / Var)

4.We run our model and our R^2 is 1. What is the MSE?
0

5.W​hy do we evaluate our model using a testing set?
To detect and avoid possible overfitting
B​ecause a good model is one that generalizes to new data
T​o validate diagnostics like MSE or R^2

6.S​elect the correctly paired statements.
T​rue Positive -- labeled as True -- predicted as True
T​rue Negative -- labeled as False -- predicted as False
F​alse Negative -- labeled as True -- predicted as False
False Positive -- labeled as False -- predicted as True

7.W​hat is the balanced error rate from the data below? Remember that you need to calculate the false positive rate and false negative rate.
| Prediction      | Label     | Result     | Count     |
| ---------- | :-----------:  | :-----------: | :-----------: |
| T​rue	     | T​rue	    | T​rue Positive	     | 10     |
| T​rue	     | F​alse	    | F​alse Positive		     | 5     |
| ​False		     | T​rue	    | ​False Negative	     | 7     |
| ​False		     | ​False		    | True Negative		     | 12     |

6/17

8.G​iven the following labels and confidence scores, what would be the precision@5?
| y      | Confidence     |
| ---------- | :-----------:  |
| 1​	     |  1.5    |
| 1​	     |  0.3    |
| -1​	     |  0.9    |
| -1​	     |  1.1    |
| -1​	     |  0.2    |
| 1​	     |  0.7    |

3/5
