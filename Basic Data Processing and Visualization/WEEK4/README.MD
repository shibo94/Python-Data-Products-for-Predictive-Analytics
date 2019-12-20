# Review: NumPy
1.W​hy might we want to use numpy.matrix() instead of numpy.array() or numpy.stack()?  
W​e are performing complex mathematical expressions with matrices  
We are multiplying matrices together  
2.W​hat is the output of the code below?  
```html
[[ 1.  0.  0.]
 [ 0.  1.  0.]
 [ 0.  0.  1.]]
```
# Review: MatPlotLib
1.H​ow do you change the name of a library you are working with in Python?  
```html
import library as name
```
2.H​ow would you create a basic bar plot with matplotlib, given the following?  
```html
import matplotlib.pyplot as plt
X = list(features)
y = [results[x] for x in X]
```
3.W​hich of the following are useful functions for modifying a graph in matplotlib?  
x​label()  
y​lim()  
a​xis()  
t​itle()  
y​label()  
x​ticks()  
y​ticks()  
l​egend()  
p​lot()  
# Review: urllib and BeautifulSoup
1.W​hat is the difference between urllib and BeautifulSoup?  
u​rllib helps us get the HTML contents of a webpage, while BeautifulSoup helps us parse HTML.  
2.T​rue or False: We should use BeautifulSoup to traverse any HTML page we want to parse.  
F​alse  
3.W​hich of the following are advantages of BeautifulSoup?  
B​eautifulSoup parses the HTML contents of a given webpage to extract desired text  
B​eautifulSoup requires minimal setup to use  
# Quiz: Week 4 Assessment
1.H​ow would you extract a single feature from a dataset with a single line of code?  
```html
feature = [d['feature'] for d in dataset]
```
2.H​ow would you build a 3D array from these features? Assume each feature is currently a list.  
```html
array = numpy.stack(
        numpy.array(feature1),
        numpy.array(feature2),
        numpyarray(feature3)
        )
```
3.T​rue or False: Elements in numpy arrays must be all the same type.  
True  
4.How would you change the number 5 to 7 in this matrix?
```html
arr = numpy.array([1,2,3,4,5])
```
arr[4] = 7  
5.Which command allows you to edit the view of the axes on a matlibplot plot?  
axis()  
6.When is it NOT acceptable to avoid axis labels in plots using matlibplot?  
When you are presenting non-intuitive results to another person.  
7.Which graphing method should you use to visualize the correlation between two arrays?

S​catterplot  

Box Plot(I​ncorrect. You would mainly use this to show the distributions of variables.)
H​istogram(I​ncorrect. You would mainly use this to show the distribution of a numerical variable.)
