# Review: Regression Diagnostics
1.Why do we commonly use mean squared error (MSE) (versus mean absolute error or otherwise)?  
Because the MSE accounts for the probability of large errors versus that of small errors  
2.F​ill in the blank: "The MSE is proportional to the _________ of the data."  
v​ariance  
3.Which of the following correctly corresponds to R^2?  
1 - (MSE(f) / Var(y))  
C​orrect! Recall that MSE(f) / Var(y) is also known as FVU(f).  
1​ - FVU(f)  
C​orrect! Recall that FVU means "fraction of variance unexplained".  
4.W​hich of the following are desirable attributes for selecting training and testing sets?  
Both sets should be n​on-overlapping  
Both sets should be r​andomized  
# Review: Classification Diagnostics
1.The robot apocalypse has arrived and is trying to identify all humans for "processing". IAJM-3000 stops you in your tracks and scans your barcode tattoo. There is a soft beep as the light flashes green, telling IAJM-3000 you are a robot and not human. What is this an example of?  

False negative  （不全）

2.Fill in the blank: "T​he ______ confidence is found the ______ from the decision boundary in the ______ direction."  

h​ighest -- furthest -- positive  

l​owest -- furthest -- negative  

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
