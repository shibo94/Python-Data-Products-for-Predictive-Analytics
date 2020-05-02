#  Review: Recommender Systems
1.T​rue or False: "Similarity-based" recommender systems use machine learning to estimate specific outcomes.
False
2.W​hich of the following are possible issues with collaborative filtering?
C​ollaborative filtering does not necessarily encourage diverse results

C​ollaborative filtering may be slow, especially with large datasets
# Review: Introduction to Latent Factor Models
1.W​hat is a latent factor model, in simplest terms?  
A​ machine-learning based recommender system  
2.H​ow do we solve for the issue of personalizing recommendations to individual users?
W​e use gradient descent to approximate low-dimensional representations of users and the data.  
W​e use dimensionality reduction to best explain the data  
# Week 1 Assessment
1.Which of the following are possible to recommend using a Recommender System?  
Companies  
Products  
Words  
Movies  
2.Which of these functions can be used to determine similarity between any finite sets?  
Mean Squared Difference(Correct! This function can be used to find the similarity based on absolute rating, meaning the given rating of an object relates more to other similarly rated objects. This method can also be combined with Jaccard similarity.)  
Jaccard(Correct! This function is the most commonly used function for gauging similarity between finite sets. It is based on the number of items rated.)  
Cosine(This method uses split sets and agreement (or lack of) between users to "insert" opinions into our recommendations.)  
3.What are the two most common types of recommender systems?  
Similarity & Model based  
4.True or False: There is an inverse relation when measuring similarity between users and items.  
True  
5.Which of the following are issues with collaborative filtering in practice?  
Large datasets cause the execution to be rather slow.  
(Correct! If one user purchases one item, it can change the rankings of every other item that was purchased which has as least one user in common.)  

Lack of diversity in recommendations  

 (The recommendations won't vary more than a marginal amount without further tweaking to how recommendations are made.)  

Systems aren't useful to new users

(Without any data on a user, there is no discernible way to find similarities, which is an issue when your recommendations are based on similarity.
)  
6.W​hat is a drawback of using Euclidean distance to measure similarity?  
W​eighted towards small sets, even with few commonalities  
7.Sally is browsing an online store selling seashells. The store's recommender system calculates a cos(θ) of 0.87 for a Cornish Shell and a cos(θ) of -0.87 for a French Curl. Which shell will get recommended to Sally, and why?   

C​ornish Shell -- a positive cos(θ) indicates more commonalities between user item histories because of their direct relationship  
8.H​ow is the Pearson correlation calculated for numerical ratings?  

S​ubtract the average of the total ratings from each individual rating  
9.T​rue or False: Latent factor models are an example of supervised learning recommender systems.  

T​rue  
10.F​ill in the blank: "Applying gradient descent to latent factor models (with the terms shown in lecture) will _______ lead to a global optimum."

n​ot necessarily  

( To obtain the best results, be careful when you initialize the model or run it with several random restarts)  
11.W​hat are the roles of the gamma parameters (last 2 parameters) in the latent factor model equation?  
![avatar](https://raw.githubusercontent.com/shibocs/Python-Data-Products-for-Predictive-Analytics/master/Deploying%20Machine%20Learning%20Models/WEEK1/1.png)
T​o capture a low-dimensional representation of the users and items  

T​o personalize recommendations to individual users  
