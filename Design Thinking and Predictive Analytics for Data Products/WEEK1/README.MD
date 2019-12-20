# Review: Supervised Learning
1.W​hat are some disadvantages of designing a system based on prior knowledge?
T​his system may depend on false assumptions on how users relate to items.
T​his system cannot adapt to new information.
2.W​hat do y, X, and theta represent in a linear regression equation?
```html
y​ - labels, the thing we want to predict
X​ - features, the things we will use to predict
t​heta - weights or parameters we tune to make the prediction
```
# Review: Regression
1.W​hy did we implement the feature function with a 1 at the 0th index (like below)?  
```html
def feature(datum):
    feat = [1, datum[0], datum[1]]
    return feat
```

T​o account for the intercept parameter  

2.Which of the following is true about autoregression?  
I​t is fitted with least-squares  
It allows us to capture periodic effects, such as weekly sales or website traffic  
It can be described as a​ time-series model that is trained with and takes input from previous observations.  
# Quiz Supervised Learning & Regression

1. What is the main difference between supervised and unsupervised learning?  

Supervised learning is optimized for predictive tasks  


Notice:  
Unsupervised learning is used to find patterns in data, but is not optimized for predictions.  
Supervised learning lets you understand the relationship between the response and predictors.  
Unsupervised learning lets you understand the relationship between observations.  
2.What is linear regression?  
Approximating a line to fit the data   
Y = x * θ  
Inflexible  
All of the above
3.What is the biggest difference between first three methods (sliding window, linear decay, exponential decay) and the fourth model (autoregression) for time-series regression?  
The first three assign weights based on an arbitrary scheme, while the fourth learns the weights.  
4.In the line of code pertaining to autoregression:  
```html
// This is Python, not Javascript
// windowSize = 10
x = [float(d[5]) for d in dataset[ind-windowSize:ind]]
```
x is a vector of the past 10 observations
