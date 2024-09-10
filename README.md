# 🎀 🐈  PINKY PROMISE SHOP!!  🐈 🎀

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
 3. first of all, I ran python3 manage.py makemigrations to make model migrations
 4. after that, i ran python3 manage.py migrate to apply migrations to the local database

#### E. CREATE FUNCTION VIEWS.PY
 1. I integrated the mvt components with a few steps. 
 2. firstly I created a views.py file in the main application file and filled it as follows (isi)
 from django.shortcuts import render
```
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
9. After doing all of the steps, I did some checking to the building status of the PWS deployment (wether its still being built or its successfully built). I did that in order to check wether I made any mistakes during the deployment steps and to fix any errors if any.


### 2. DIAGRAM
### 3. USAGE OF GIT IN SOFTWARE DEVELOPMENT
 GIT itself is a DevOps tool that is used for source-code management. GIT is used for software development since its branches are easy to merge and cheap as well. This also facilitates the feature branch workflow in which these feature branches provide an isolated environment for every change to the codebase. 
### 4. WHY IS DJANGO USED AS A STARTING POINT FOR LEARNING SOFTWARE DEVELOPMENT
 Based on my personal experience, I felt like Django is an easy to use web framework. Django also allows us to write our desired app without having to reinvent the wheel since Django takes care of much of the web development hassle
### 5. WHY IS THE DJANGO MODEL CALLED ORM