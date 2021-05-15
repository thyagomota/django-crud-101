# django-crud-101
A simple Django webapp that performs CRUD operations, roughly based on https://www.javatpoint.com/django-crud-application. Any snippet that begins with `$` is supposed to run on a terminal. 

# Step 1 - Create a Project

```
$ django-admin startproject seamagnet 
$ cd seamagnet
```

# Step 2 - Create an App

```
$ python3 manage.py startapp employee
```

# Step 3 - Database Setup

Edit seamagnet/settings.py, adding the database configuration below (replacing the root's password accordingly). 

```
DATABASES = {  
    'default': {  
        'ENGINE': 'django.db.backends.mysql',  
        'NAME': 'djangodb',  
        'USER':'root',  
        'PASSWORD':'<<your root's password>>',  
        'HOST':'localhost',  
        'PORT':'3306'  
    }  
} 
```

# Step 4 - Create a Model for Employee

Replace employee/models.py with the following: 

```python
from django.db import models  

class Employee(models.Model):  

    id   = models.IntegerField 
    name = models.CharField(max_length=50)  
     
    class Meta:  
        db_table = "employees"  
```
