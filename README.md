# 🎀 🐈  PINKY PROMISE SHOP!!  🐈 🎀


## [LINK TO PINKY PROMISE'S PWS APP](https://samuella-putri-pinkypromise.pbp.cs.ui.ac.id/)

# ASSIGNMENT 2
### 1. HOW I IMPLEMENTED THE CHECKLISTS


#### A. CREATING A NEW DJANGO PROJECT
 1. I started by initializing a git configuration with git init inside a folder I created (pinky-promise), pinky-promise itself will become the name of my store that I created
 2. next I configured my email and username that i use in GitHub and also configured the authentication with the brew install git-credential-manager-core command, then verify it with 
 ```
 git config --list
 ```
 3. After that, I initialized a repository in github. I created a repository with the name pinky-promise
 4. Then back in the terminal, I created a new main branch with the command 
 ```
 git branch -M main
 ```
and connected it with my github repository with the command 
 ```
 git remote add origin HTTPS URL
 ```
 5. Then I created a virtual environment with the command 
 ```
 python3 -m venv env 
 ```
 and activated it with 
 ```
 source env/bin/activate 
 ```
 command
 6. After that I created a requirements.txt file inside the directory with some dependencies, then installed it with the command 
```
 pip install -r requirements.txt
```
 7. After that I created a django project with a command 
```
 django-admin startproject pinky-promise 
```
 8. Next I configured the project with a few steps. Firstly I edited the allowed hosts to become 
```
 ALLOWED_HOSTS = ["localhost", "127.0.0.1"] 
```
 for some deployment needs.
 
 9. Then I ran the django server with the command python3 manage.py runserver
 10. I also made sure that the django application has been created successfully using the link http://localhost:8000
 11. Then I added a gitignore file which is a configuration file used in the Git repository to specify the files and directories that should be ignored by Git.
 12. Then I did the usual add commit push commands to push any changes from the directory
#### B. CREATING AN APPLICATION NAMED "MAIN" IN THE PROJECT
 After that, inside the main app directory, I created a new main.html file in which I will be displaying my store name, my name, and also my class.
#### C. PERFORM ROUTING IN THE PROJECT SO THAT THE APPLICATION MAIN CAN RUN 
I created urls.py in the main director and filled it with. This will be responsible for managing the URL routing related to the main application.
#### D.  CREATE A MODEL IN THE APPLICATION MAIN 
 1. I modified the models.py file located in the main directory to store a few attributes. The attributes are as follows: 
```
 from django.db import models
 
 class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    coquetteness = models.TextField()

    def __str__(self):
        return self.name
```
 2. After that, I did the steps to make & apply model migrations  
 3. first of all, I ran 
 ```
 python3 manage.py makemigrations 
 ```
 to make model migrations
 
 4. after that, i ran 
 ```
 python3 manage.py migrate 
 ```
 to apply migrations to the local database

#### E. CREATE FUNCTION VIEWS.PY
 1. I integrated the mvt components with a few steps. 
 2. firstly I created a views.py file in the main application file and filled it as follows 
 ```
 from django.shortcuts import render
 def show_main(request):
    context = {
        'name': 'Samuella Putri Nadia Pauntu',
        'store_name': 'PINKY PROMISE',
        'class': 'PBP KKI',
    }
    return render(request, 'main.html', context)
```
 3. then i applied model modification to my main.html file to display data that has been retrieved from the mode. the inside of it is as follows:
 ```
 <h1>HI! Welcome to {{ store_name }}!!!</h1>


<h2>Name</h2>
<p>{{ name }}</p>

<h2>Class</h2>
<p>{{ class }}</p>
```

#### F. CREATE A ROUTING IN URLS.PY FOR THE APPLICATION MAIN 
I opened the urls.py file inside of the pinky_promise project directory and added it up with the following code under the available explanation with the following:
```
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
]

```
#### G. PERFORM DEPLOYMENT TO PWS
1. Before deploying to PWS I created a .gitignore file inside of my pinky_promise directory
2. I did the add, commit, push command from the local repository directory to github to push any changes
3. Next I accessed the PWS website through the link https://pbp.cs.ui.ac.id/web/
4. Then I created a new project with the name ' pinkypromise '
5. After clicking on Create New Project, I went back to my vscode and opened the settings.py file in the pinky_promise directory and added my PWS deployment url to it, making it become: 
```
ALLOWED_HOSTS = ["localhost", "127.0.0.1", "samuella-putri-pinkypromise.pbp.cs.ui.ac.id"]
```
6. Then, I did the add, commit, push commands to push the changes to the github repository
7. After that, I run the information in the Project Command on the PWS page and change the branch name to main with the following command:
```
git branch -M main
```
8. After that I ran the push pws master command to push any changes in the Django project to PWS.
```
git push pws main:master
```
9. After doing all of the steps, I did some checking to the building status of the PWS deployment (whether its still being built or its successfully built). I did that in order to check wether I made any mistakes during the deployment steps and to fix any errors if any.


### 2. DIAGRAM THAT CONTAINS REQUEST CLIENT TO A DJANGO-BASED APPLICATION AND THE RESPONSE IT GIVES. 
![DIAGRAM](diagram.png)


When a user makes a request by visiting a specific URL, Django first checks the urls.py file to find a matching route for that URL. Once match is found, it directs the request to the corresponding view function in views.py. The view function contains the business logic and often interacts with the data models, which are defined in models.py, to retrieve or modify information from the database. After gathering the necessary data, the view function passes it to an HTML template, where the data is rendered and formatted for display. The HTML file, located in the templates folder, then dynamically presents the data and is returned as a response to the user's browser, completing the request-response cycle. 

### 3. USAGE OF GIT IN SOFTWARE DEVELOPMENT
 GIT itself is a powerful tool widely used for source code management. It plays a crucial role in software development due to its efficient branching system, where branches are both easy to merge and lightweight. This enables the use of a feature branch workflow, which provides an isolated environment for each change made to the codebase. This workflow allows developers to work on new features, bug fixes, or experiments without affecting the main codebase until the changes are thoroughly tested and reviewed.
### 4. WHY IS DJANGO USED AS A STARTING POINT FOR LEARNING SOFTWARE DEVELOPMENT
 Based on my personal experience, I felt like Django is an easy to use web framework. Django also allows us to write our desired app without having to reinvent the wheel since Django takes care of much of the web development hassle. Here's some further explanation on some advantages of using Django as a starting point for lewarning software development.
 #### 1. Comprehensive Framework: 
 Django is a full-stack web framework, providing verything needed to develop web applications. This includes URL routing, database management, user authentication, and form handling. This makes django very beginner friendly to those wanting to learn core concepts without having to build everything from scratch
 #### 2. Real-world Application: 
 Learning Django equips beginners with skills we can use in real-world projects, since many professional web-appliations are built using Django.
### 5. WHY IS THE DJANGO MODEL CALLED ORM
 Django's ORM provides a way to interact with the database using Python code through models, abstracting away the underlying SQL queries, making it easier to work with databases in an object-oriented fashion. Django's model itself is called ORM due to a few reasons.
 ##### 1. Object-Relational Mapping: 
 It maps Python objects (like classes) to relational database tables, creating a bridge between the two different paradigms: the object-oriented world and the relational database world.
 #### 2. Model: 
 In Django, each database table is represented by a model. This model is a Python class that defines the structure of the table, including the fields and methods (which can encapsulate behavior related to that table).


# ASSIGNMENT 3
### 1. WHY WE NEED DATA DELIVERY IN IMPLEMENTING A PLATFORM
Data delivery is something that is considered essential in any data-driven organisation. Here are a few key reasons why data delivery is important:
#### Security:
In terms of security, it secures data delivery protocols, such as encryption during transmission, ensure that sensitive information is protected from interception or attacks, especially when dealing with personal or financial data.
#### Data Integrity: 
The correct and proper delivery mechanisms ensure that the data remains accurate and complete from the source to the destination. This is critical for applications that rely on precise data, such as healthcare platforms, e-commerce transactions, or data analytics tools.
#### User Experience:
Fast and reliable data delivery directly impacts the user experience. If data is delayed or delivered inefficiently, users may experience lag, slow loading times, or incomplete content, which can lead to frustration and a negative perception of the platform.


### 2. XML VS JSON, WHICH ONE IS BETTER?
The main difference between XML and JSON lies in their structure and syntax. JSON is built on key-value pairs, while XML relies on end tags. Structurally, XML tends to be more complex than JSON because it offers a more intricate representation of attributes. JSON, however, is more widely used due to its simpler, more flexible format for data exchange. Additionally, JSON is better supported by modern programming languages and software systems, making it a more popular choice than XML.

### 3. FUNCTIONAL USAGE OF is_valid() METHOD IN DJANGO FORMS
The purpose of is_valid() is to validate each field in a form. It returns True if all fields pass the validation rules and False if any field fails. Additionally, is_valid() helps with error handling by providing a list of error messages, which can be accessed via the form.errors attribute.

The is_valid() method is valuable in forms for several reasons. Here are some key benefits:

#### Data Integrity 
is_valid() ensures that only correctly formatted and valid data is processed through the form, protecting the application from invalid or harmful input and preserving data integrity.

#### Error Feedback 
is_valid() enables developers to offer users clear error messages when invalid data is entered, enhancing the overall user experience.


### 4. WHY DO WE NEED csrf_token WHEN CREATING A FORM IN DJANGO
Django generates a unique CSRF token for when a user is authenticated an surfing a web. This token is used to verify that the request is coming from the authenticated user and not from a malicious source. CSRF's protection is mainly focusing on protecting against actions that make changes in data. 

When CSRF is not used, the application becomes vulnerable to the CSRF attacks themselves. Any form submission can be spoofed by any attacker, leading to unauthorized actions on behalf of the user.

Attackers could leverage this through a few forms:
#### Force Unwanted Actions: 
An attacker could create a form on another website that, once submitted by the victim (unknowingly), sends a request to the targeted Django application. This request would seem valid to the server because it comes from an authenticated user, but the form's action could lead to unintended consequences, such as modifying user settings, deleting an account, or transferring funds.

#### Bypass Authentication:
If a user is logged in and the attacker knows the URLs and activities expected by the server, the attacker can use CSRF attacks to perform actions that users would typically authenticate for, such as passwords. 

#### Hijacking User Sessions:
Attacker can make attacks using the user's sessions, meaning, they can perform any action the user has permission for. They can perform malicious actions without the user noticing them. 

### 5. HOW I IMPLEMENTED THE CHECKLISTS
#### A. Create a form input to add a model object to the previous app.
1. I created a new file forms.py in the main directory to create the structure of the form which will be recieving the data entries of the pre-ordered items in Pinky Promise.
 ```
from django.forms import ModelForm
from main.models import Product

class ProductEntryForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "description", "price", "coquetteness"]
 ```

2. Then i accessed the views.py file in the main directory to add some imports and also make a function create_product_entry which will be receiving the product entries 
```
from django.shortcuts import render, redirect 
from main.forms import ProductEntryForm
from main.models import Product
```
```
...
def create_product_entry(request):
    form = ProductEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product_entry.html", context)
```

3. I changed the show_main function by adding Product.objects.all() which will retrieve all objects of the Product objects stored in the database

```
def show_main(request):
    product_entries = Product.objects.all() # added this
    context = {
        'name': 'Samuella Putri Nadia Pauntu',
        'store_name': 'PINKY PROMISE',
        'class': 'PBP KKI',
        'product_entries': product_entries # added this
    }
    return render(request, 'main.html', context)
```

4. After that I moved to urls.py in the main directory to import the create_product_entry function that I just created. 

```
from main.views import show_main, create_product_entry
```

5. I also added the url path to urlpatterns in the same file 
```
urlpatterns = [
   ...
   path('create-product-entry', create_product_entry, name='create_product_entry'),
]
```

6. I created a new HTML file with the name create_product_entry.html (which will be used to add the new product entry) in the main/templates directory with its contents as follows:
```
{% extends 'base.html' %} 
{% block content %}
<h1>Add New Product Entry</h1>

<form method="POST">
  {% csrf_token %}
  <table>
    {{ form.as_table }}
    <tr>
      <td></td>
      <td>
        <input type="submit" value="Add Product Entry" />
      </td>
    </tr>
  </table>
</form>

{% endblock %}
```

7. Then, I fixed the main.html file and use the {% block content %} block to present the form data in a table format, along with an "Add Product Entry" button that will navigate to the form page.
```
{% extends 'base.html' %}
{% block content %}
<h1>Hi!! Welcome to {{ store_name }}</h1>

<h5>Name:</h5>
<p>{{ name }}</p>

<h5>Class:</h5>
<p>{{ class }}</p>

{% if not product_entries %}
<p>There are currently no product in stock yet. Please pre-order by clicking the add new product below.</p>
{% else %}
<table>
  <tr>
    <th>Product Name</th>
    <th>Price</th>
    <th>Description</th>
    <th>Coquetteness</th>
  </tr>

  {% comment %} This is how to display mood data
  {% endcomment %} 
  {% for product_entry in product_entries %}
  <tr>
    <td>{{product_entry.name}}</td>
    <td>{{product_entry.price}}</td>
    <td>{{product_entry.description}}</td>
    <td>{{product_entry.coquetteness}}</td>
  </tr>
  {% endfor %}
</table>
{% endif %}

<br />

<a href="{% url 'main:create_product_entry' %}">
  <button>Add New Product Entry</button>
</a>
{% endblock content %}
```
#### B. Add 4 views to view the added objects in XML, JSON, XML by ID, and JSON by ID formats.
1. First I added some imports to the views.py file
```
from django.http import HttpResponse
from django.core import serializers
```

2. Next, I created four functions that take 'request' as a parameter and define a variable within each function to store the result of querying all the data from Product. This will allow us to view the added entries/objects in XML, JSON, XML by ID, and JSON by ID.

``` 
def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```

#### C. Create URL routing for each of the views added in point 2.

1. I import the functions to the urls.py file
```
from main.views import show_main, create_mood_entry, show_xml, show_json, show_xml_by_id, show_json_by_id
```

2. Then, I included the URL path in the urlpatterns variable within the urls.py file located in the main directory, which will be allowing access to the functions that I created previously.
```
urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product-entry', create_product_entry, name='create_product_entry'), 
    path('xml/', show_xml, name='show_xml'), # this line
    path('json/', show_json, name='show_json'),  # this line
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),  # this line
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),  # this line

]
```

### SCREENSHOT OF POSTMAN
![JSON](JSON.png)
![JSON by ID](JSONID.png)
![XML](XML.png)
![XML by ID](XMLID.png)