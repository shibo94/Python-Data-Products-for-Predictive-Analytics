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
