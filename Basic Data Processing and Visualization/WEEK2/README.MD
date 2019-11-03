## Python: Reading Data and Simple Statistics
1.What are some techniques used to avoid utilizing too much memory while processing a dataset?  
Filter data as it is being read  
Read the data line by line  
2.What are the limitations of the CSV/TSV format?  
It can store only tabular data  
3.Why is JSON a convenient data format for Python?  
We can treat it like Python's dictionary structure with key-value pairs  
We can use the function eval() to easily convert a JSON file to a Python object  
4.What is the primary function of the command string.split(':')?  
Parses the string into a list of smaller strings, each originally separated by a colon  
5.What does the defaultdict() function do?  
Automatically initializes dictionary values to existing keys  
6.How would you convert a value into an int, if d is your dictionary?  
d['field'] = int(d['field'])  
7.Which of the libraries below are correctly paired with what we have used them for?  
json - Lets you parse JSON through strings or files  
gzip - Unzip a gzipped dataset to read it into Python  ast - Double-checks that the line of code to be executed is legitimate Python  
csv - Lets you parse CSV or TSV files.  
8.W​hat is the output of the code below?  
```html
string = "seller_id, product_id, price, customer_id, review_id"
string.split()
```
[​'seller_id,', 'product_id,', 'price,', 'customer_id,', 'review_id,']  
9.I​ understand, let's do this!   
10.Write a function named listavg that takes a numeric list as input and returns the average of the list. You do not have to check for edge cases (e.g. null list, extreme values, non-numeric values, etc.).  
```html
def listavg(list_of_nums):
  sum=0
  n=0
  for a in list_of_nums:
    sum = sum +a
    n = n + 1
  return sum/n
```
11.Write a function named count_data that takes a complete "dataset" and string as input. It returns a defaultdict object containing the count of content in the given dataset's column.  
```html
from collections import defaultdict
def count_data(dataset, field):
  ratingcounts=defaultdict(int)
  for d in dataset:
    ratingcounts[d[field]] += 1
  return ratingcounts
```
