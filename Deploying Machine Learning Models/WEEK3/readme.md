# Review: Flask and Django

1.What are some key differentiators for Flask versus Django?  

Model-View-Controller (MVC) Architecture  

It's more lightweight  

2.Besides GET and POST, what are some other HTTP 'verbs' that are used?  
put  

3.W​hat does "loose coupling" mean in the context of Django's design philosophy?  
W​hen one line of code changes, it's not likely to break another line that depends on it.  

4.G​iven a list of dogs[], which code snippet is a valid Flask HTML template that iterates through this list, and prints a paragraph(<p>) for each dog in the list?  
```html
{% for dog in dogs %}
<p>{{dog}}</p>
{% endfor %}
```

# Deploying Recommender Systems
1.Flask and Django are examples of:   
Web Frameworks  
2.Which framework should be chosen for an analytical web applications? (Choose the best response based on how they apps were built)  
Flask  
(Flask is built as a general purpose web framework, making it a better fit than Django.)  
