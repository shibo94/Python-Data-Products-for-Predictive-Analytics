# Review: Data Filtering and Cleaning
1.Question 1  
W​hat are some reasons for cleaning or "pre-processing" datasets?  
S​ome parts of the dataset might have significant outliers    
S​ome parts of the dataset might be "stale" (outdated in a sense)  
F​ields might be missing from some entries  
S​ome data may need to be restricted to certain groups  
S​ome data may apply to only rare or inactive users  
S​ome entries might be poorly formatted  
2.H​ow might we filter a list of businesses based on their ratings and number of reviews? Assume "dataset" contains a complete cleaned dataset of businesses and relevant features.  
```html
dataset = [d for d in dataset if d['rating'] > 3.5 and d['num_reviews'] == 20]
```
3.W​hat are some ways we can filter reviews by?  
R​eview length  
R​eview quality  
U​ser activity  
R​eview rating D​ate  
User location  

# Review: Processing Different Data Types
1.What is tokenization (in the context of this module)?  
The act of splitting a string into dicrete "tokens" by a defined delimiter  
2.W​hen would strptime() be convenient?  
W​hen we want to extract features from data  
3.W​hat is the output of the code below?  
```html
string = ['hello', 'mam', 'why']
', '.join(string)
```
"​hello, mam, why"  
4.W​hich libraries are useful for processing time data?  
d​atetime  
(This library is a combination of date and time. See more at this link: https://docs.python.org/2/library/datetime.html#available-types)  
c​alendar  
(This library assumes each day has exactly 24*60*60 seconds. See more at this link: https://docs.python.org/2/library/calendar.html#module-calendar)  
t​ime  
(This library assumes each day has exactly 24*60*60 seconds. See more at this link: https://docs.python.org/2/library/datetime.html#available-types)

# Quiz: Processing Different Data Types
1.What is the meaning of a "KeyError"?  
The requested key is missing from the dictionary object  
2.What does string.punctuation return?  
A string of commonly-used punctuation characters  
3.Why are case-changing string commands like string.upper() or string.lower() useful?  
We can more easily compare different variations of the same word, like APPle and appLE  
We don't have to iterate character-by-character to convert a word to upper or lowercase  
Computing statistics on text is easier when we don't care about word case.  
4.What is Unix time?  
The number of seconds since January 1, 1970, in the UTC timezone  
5.What is true about Time.strptime?  
We can more easily extract features from data  
It converts a time string to a structured time object  
//
Time.strptime: time string --> structured time object  
Time.strftime: structured time object --> time string  
Time.mktime/calendar.timegm: structured time object --> number  
Time.gmtime: number --> structured time object  
6.What is the difference between mktime() and gmtime()?  
For the given time struct, mktime() assumes it is local time, gmtime() assumes it is UTC time.  
7.Write a function named string_processing that takes a list of strings as input and returns an all-lowercase string with no punctuation.  
```html
import string
def string_processing(string_list):
  newwordlist = ''
  for word in string_list:
    word=word.lower()
    newword= ''.join([x for x in word if not x in string.punctuation])
    if not newwordlist:
      newwordlist = newword
    else:
      newwordlist = newwordlist + ' ' + newword
  return newwordlist
```
