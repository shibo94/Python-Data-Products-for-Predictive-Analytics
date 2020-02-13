# Review: Classification and K-Nearest Neighbors

1.W​hat is the best definition of classification below?  
A​ model that seeks to predict the numerical value of some variable  
2.Which of the following is/are classification problem(s)?  
Predicting whether monsoon will be normal next year  
Predicting the gender of a person by his/her handwriting style  
3.A selected Flower has its neighbors as Tall, Short, Short, Tall, Tall, Short, from nearest to furthest in that order. What would the Flower be classified as, given a K of 5?  
Tall  
(Because K = 5, we count the number of Talls and Shorts in the 5 nearest neighbors. There are 3 Talls and 2 Shorts, so the Flower will be predicted as Tall.)  





```html
[[ 1.  0.  0.]
 [ 0.  1.  0.]
 [ 0.  0.  1.]]
```

# Review: Logistic Regression and Support Vector Machines


1.W​hich of the following are questions answerable with logistic regression (vs. linear regression)?  
Will a given stock will issue a dividend this year based on last year’s percent profit?  
(C​orrect! This is a binary classification.)  
What is the probability that a student who studies for 40 hours and has an undergrad GPA of 3.5 gets an A in the class?  
(C​orrect! Probability is a good hint that logistic regression will be useful.)  
H​ow well does square footage affect a house's price?  
(I​ncorrect. This question is looking at the relevance of the predictors and the predicted variable is continuous.)  
Is at least one of weight, height, body mass index, or number of cigarettes smoked per week useful in predicting a heart attack?  
(I​ncorrect. This question is looking at the relevance of the predictors, rather than the actual probability of a heart attack.)  

2.W​hat is the basic idea behind Support Vector Machines?    
T​o find a border, or hyperplane, that best divides multidimensional data into classes  

# Quiz: Classification
1.W​hat is the difference between regression and classification?  
In r​egression, we predict the output value with training data. In classification, we group the output into a class.
2.How do we calculate the accuracy of a classification?  
W​e record our model's predictions and see how many of them match the actual outcomes of the data.
3.Y​ou have the following data and want to classify a point with X1 = 1, X2 = 2, X3 = 3 with K-Nearest Neighbors. What would this point be classified as if K = 3?  

| X1 | X2 | X3 | Y​ |
| ------ | ------ | ------ | ------ |
| 0​ | 0 | 0​ | Cat |
| 2​ | -​2 | 1​ | Dog |
| 1​ | 1​ | 1​ | D​og |
| 3​ | 2 | 1​ | C​at |
| 2​ | -​2 | 2​ | C​at |
| 3​ | 1 | -​1 | D​og |  

C​at  
(O​bservations 1, 3, and 4 are the closest points to the test point, with labels of cat, dog, and cat, respectively.)  

4.True or False: We use logistic regression to model the probability of a certain outcome.  
T​rue  
(This is why the result of logistic regression shows an S-shaped curve.)  
5.True or False: W​e can use K-Nearest Neighbors for both classification and regression.  
T​rue  
(The k-nearest neighbors algorithm (k-NN) is a non-parametric method used for classification and regression.)  
6.W​hat is the difference between linear and logistic regression?  
The outcome (label) for l​inear regression is the actual value of the outcome.The outcome (label) for logistic regression is the probability of getting a certain outcome.  
T​he equation for linear regression is in the form of a line (y = mx + b), whereas the equation for logistic regression is given by the logistic function (y = e^X + e^(-X)).  
L​inear regression results in a line, whereas logistic regression gives us an S-shaped curve.   
( This is related to the fact that logistic regression gives us the probability of a certain outcome and will never be less than 0.)   
The outcome (label) for l​inear regression can have any one of an infinite set of values. The outcome (label) for logistic regression has a limited number of possible values.  
7.W​hat is true of Support Vector Machines (SVMs)?  
S​VMs use kernel functions to divide classes/labels.  
S​VMs are memory-efficient since they use a subset of training points rather than all the points  

# Review: Gradient Descent
1.W​hy do we initialize theta_0 (offset parameter) to the mean value of the output labels?  
T​o help the model converge faster  
2.W​hat are some pitfalls we should watch out for when using TensorFlow to compute a gradient descent?  

W​e should explicitly define our variables as variables, rather than leaving them as constants  
W​e should convert our vector of labels to a TensorFlow column vector, rather than a row vector  

# Quiz: More on Classification
1.Which of the following are true about gradient descents?  

Mathematically, it is a partial derivative with respect to its inputs.  

It is used as a​ way to update the parameters of your model.  

T​he size of each iterative step in the direction of steepest descent is called the learning rate.  

It is an optimization procedure used with many machine learning algorithms to minimize some function by iteratively moving in the direction of steepest descent as defined by the negative of the gradient.  

2.W​hy do we use separate training and testing datasets?  
We use training sets to build our model and testing sets to see how well our model performs on never-before-seen data.   

3.W​hat does the TensorFlow method tf.constant() do for us?
It creates a tensor (generalized matrix) populated with the given values.  

4.W​hat is the main advantage of TensorFlow for gradient descents?   

TensorFlow computes the gradient with various built-in functions like optimizer.minimize() and tf.train.AdamOptimizer().


5.By what factor is our Theta modified in each iteration of Gradient Descent in Python?  

Learning Rate * dTheta

6.In a data set containing n variables, what is the maximum number of variables usable to calculate a specific feature?

n-1

7.What will happen if all values of theta_n = 0 for n > 0? (Say theta_0 = 1)  

The function will be constant.  

The function is independent of the other variables.  
