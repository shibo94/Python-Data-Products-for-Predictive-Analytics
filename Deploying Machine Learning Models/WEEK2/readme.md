# Review: Similarity-Based Recommenders
1.R​eviewing basic sets:
S​1 = {1, 2, 3}
S​2 = {3, 4, 5}
W​hat is S1.intersection(S2)?

3

2.R​eviewing basic sets:

S​1 = {1, 2, 3}

S​2 = {3, 4, 5}

W​hat is S1.union(S2)?

1​, 2, 3, 4, 5

3.R​ather than iterating through all items in the dataset, what can we do to recommend items more efficiently?
I​terate through the item history of users who have bought a selected item  
# Review: Implementing Latent Factor Models
1.W​hat are the two essential things we must provide the LBFGS library for gradient descent?  
C​ost function (f(x))  
D​erivative function (f'(x))  
2.W​hat does the "unpack" function do (in our livecoding sessions)?   
Parses a flat parameter vector (theta) to actual parameters for the latent factor model.

# Implementing Recommender Systems
1.What do we call a machine learning based recommender system?  
Latent-Factor Models  
2.In what way are latent factor models optimized?  
Gradient Descent  
3.Which of the following is the element we are trying to optimize in gradient descent?  
cost  
4.Which of the following functions are possible rating predictions models? (f being the model)  

f = Alpha  
This is the absolute simplest model where the prediction is equal to the standard deviation for any user/item pair.  

f = Alpha + Bias_User + Bias_Item  

This is another very basic model, where the biases are calculated and a simple sum of elements predicts the rating of the user/item pair.  
5.C​alculate the Jaccard similarity coefficient for A = {1, 3, 5, 7, 9} and B = {1, 2, 3, 4, 5}.  
3/7  
6.What are the correct definitions of numerator and denominator in the code below? Complete the function calculating the Jaccard similarity coefficient.  
```html
# Inputs are sets
def Jaccard(s1, s2):
    numerator = ______
    denominator = ______
    return numerator / denominator
```

n​umerator = len(s1.intersection(s2))

d​enominator = len(s1.union(s2))

7.T​rue or False: "A similarity-based recommender system cannot be used for predictions."  
False  
8.W​hich of the following are possible implementations of prediction for a similarity-based recommender?  
W​eight the rating of the evaluated item by the user's similarity to the similarity of other users who have purchased and rated the item  

W​eight the rating of each item in an user's item history by its similarity to the evaluated item  
9.H​ow many terms should a derivative function for a latent factor model have?  
O​ne for each parameter  
