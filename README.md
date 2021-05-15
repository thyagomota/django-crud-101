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

Open settings.py and look for the INSTALLED_APP entry. Make sure the employee app is added to the list. If not, add it!

```python
INSTALLED_APPS = [
    'employee',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

# Step 3 - Database Setup

Edit seamagnet/settings.py, adding the database configuration below (replacing the root's password accordingly). Also, make sure that the database `seamagnet` was created in MySQL. 

```
DATABASES = {  
    'default': {  
        'ENGINE': 'django.db.backends.mysql',  
        'NAME': 'seamagnet',  
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

# Step 5 - Create a ModelForm from the Employee's Model

In Django, a ModelForm is a class that is used to convert a model into a form. For this example, create employees/forms.py with the following code:

```python 
from django import forms  
from employee.models import Employee  

class EmployeeForm(forms.ModelForm):  
    
    class Meta:  
        model = Employee  
        fields = "__all__"  
```

# Step 6 - Create View Functions 

In Django, a view function is a python function that takes a web request and returns a web response. For this example, create employees/views.py with the following code:

```python
from django.shortcuts import render, redirect  
from employee.forms import EmployeeForm  
from employee.models import Employee  

def emp(request):  
    if request.method == "POST":  
        form = EmployeeForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass  
    else:  
        form = EmployeeForm()  
    return render(request,'index.html',{'form':form})  

def show(request):  
    employees = Employee.objects.all()  
    return render(request,"show.html",{'employees':employees})  

def edit(request, id):  
    employee = Employee.objects.get(id=id)  
    return render(request,'edit.html', {'employee':employee})  

def update(request, id):  
    employee = Employee.objects.get(id=id)  
    form = EmployeeForm(request.POST, instance = employee)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'employee': employee})  
    
def destroy(request, id):  
    employee = Employee.objects.get(id=id)  
    employee.delete()  
    return redirect("/show") 
```

# Step 7 - Create URL Mappings

In Django, a url mapping is simply a mapping between a url path and a view function. function is a python function that takes a web request and returns a web response. For this example, update urls.py with the following code:

```python
from django.contrib import admin  
from django.urls import path  
from employee import views  

urlpatterns = [  
    path('admin/', admin.site.urls),  
    path('emp', views.emp),  
    path('show',views.show),  
    path('edit/<int:id>', views.edit),  
    path('update/<int:id>', views.update),  
    path('delete/<int:id>', views.destroy),  
]  
```

# Step 8 - Create HTML Templates

Create a `templates` folder under `employee` and add the following html templates. You can learn more about Django's template language at https://docs.djangoproject.com/en/3.2/ref/templates/language/ . 

## index.html 

```html 
<!DOCTYPE html>  
<html lang="en">  
<head>  
    <meta charset="UTF-8">  
    <title>Index</title>  
    {% load static %}  
    <link rel="stylesheet" href="{% static 'css/style.css' %}"/>  
</head>  
<body>  
<form method="POST" class="post-form" action="/emp">  
        {% csrf_token %}  

    <div class="container">  
        <br>  
        <div class="form-group row">  
            <label class="col-sm-1 col-form-label"></label>  
            <div class="col-sm-4">  
                <h3>Enter Details</h3>  
            </div>  
        </div>  

        <div class="form-group row">  
            <label class="col-sm-2 col-form-label">Employee Id:</label>  
            <div class="col-sm-4">  
                {{ form.id }}  
            </div>  
        </div>

        <div class="form-group row">  
            <label class="col-sm-2 col-form-label">Employee Name:</label>  
            <div class="col-sm-4">  
                {{ form.name }}  
            </div>  
        </div>  

        <div class="form-group row">  
            <label class="col-sm-1 col-form-label"></label>  
            <div class="col-sm-4">  
                <button type="submit" class="btn btn-primary">Submit</button>  
            </div>  
        </div>  
    </div>  
</form>  
</body>  
</html>  
```

## show.html 

```html 
<!DOCTYPE html>  
<html lang="en">  
<head>  
    <meta charset="UTF-8">  
    <title>Index</title>  
    {% load static %}  
    <link rel="stylesheet" href="{% static 'css/style.css' %}"/>  
</head>  
<body>  
<form method="POST" class="post-form" action="/emp">  
    {% csrf_token %}  

    <div class="container">  
        <br>  
        <div class="form-group row">  
            <label class="col-sm-1 col-form-label"></label>  
            <div class="col-sm-4">  
                <h3>Enter Details</h3>  
            </div>  
        </div>  

        <div class="form-group row">  
            <label class="col-sm-2 col-form-label">Employee Id:</label>  
            <div class="col-sm-4">  
                {{ form.id }}  
            </div>  
        </div>

        <div class="form-group row">  
            <label class="col-sm-2 col-form-label">Employee Name:</label>  
            <div class="col-sm-4">  
                {{ form.name }}  
            </div>  
        </div>  

        <div class="form-group row">  
            <label class="col-sm-1 col-form-label"></label>  
            <div class="col-sm-4">  
                <button type="submit" class="btn btn-primary">Submit</button>  
            </div>  
        </div>  
    </div>  
</form>  
</body>  
</html> 
```

## edit.html 

```html
<!DOCTYPE html>  
<html lang="en">  
<head>  
    <meta charset="UTF-8">  
    <title>Index</title>  
    {% load static %}  
    <link rel="stylesheet" href="{% static 'css/style.css' %}"/>  
</head>  
<body>  
<form method="POST" class="post-form" action="/update/{{employee.id}}">  
        {% csrf_token %}  
    <div class="container">  
        <br>  
        <div class="form-group row">  
            <label class="col-sm-1 col-form-label"></label>  
            <div class="col-sm-4">  
                <h3>Update Details</h3>  
            </div>  
        </div>  

        <div class="form-group row">  
            <label class="col-sm-2 col-form-label">Employee Id:</label>  
            <div class="col-sm-4">  
                <input type="text" name="id" id="id_eid" required maxlength="20" value="{{ employee.id }}"/>  
            </div>  
        </div>  

        <div class="form-group row">  
            <label class="col-sm-2 col-form-label">Employee Name:</label>  
            <div class="col-sm-4">  
                <input type="text" name="name" id="id_ename" required maxlength="100" value="{{ employee.name }}" />  
            </div>  
        </div>  

        <div class="form-group row">  
            <label class="col-sm-1 col-form-label"></label>  
            <div class="col-sm-4">  
                <button type="submit" class="btn btn-success">Update</button>  
            </div>  
        </div>  
    </div>  
</form>  
</body>  
</html>  
```

# Step 9 - Add a CSS File

Create a `static/css` folder under `employee` and add a `style.css`. 

```css
body {
    font:18px/1.4 Verdana,Arial; 
    background: #fff; 
    height:100%; 
    margin:25px 0; 
    padding:0;
    text-align: center
}

p {
    margin-top:0
}

table { 
    border: 1px solid black; 
    margin: 0 auto; 
    border-collapse: separate;
    box-sizing: border-box;
    table-layout: fixed;
    width: 900px;
}

th, td { 
    border: 1px solid black;
    text-align: center; 
}

thead { 
    background: #008CBA; 
    color: #fff; 
}

tbody { 
    background: #fff; 
    color: #000; 
}

.button {
    background-color: #008CBA; 
    border: none;
    color: white;
    padding: 15px 32px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 16px;
}
```

# Step 10 - Run Migrations

In Django, you run migrations to propagate changes made in your model to your database schema. Run the following command to propagate migrations. 

```
$ python3 manage.py makemigrations  
$ python3 manage.py migrate
```

If everything works, you should be able to see the following tables created automatically in the `seamagnet` database: 

```
+----------------------------+
| Tables_in_seamagnet        |
+----------------------------+
| auth_group                 |
| auth_group_permissions     |
| auth_permission            |
| auth_user                  |
| auth_user_groups           |
| auth_user_user_permissions |
| django_admin_log           |
| django_content_type        |
| django_migrations          |
| django_session             |
| employees                  |
+----------------------------+
```

You `employees` table should have the following structure: 

```
+-------+-------------+------+-----+---------+----------------+
| Field | Type        | Null | Key | Default | Extra          |
+-------+-------------+------+-----+---------+----------------+
| id    | bigint      | NO   | PRI | NULL    | auto_increment |
| name  | varchar(50) | NO   |     | NULL    |                |
+-------+-------------+------+-----+---------+----------------+
```

# Step 11 - Test your app!

You app should be good to go! To start the server, run: 

```
$ python3 manage.py runserver
```

Then, open the app on `http://localhost:8000/show`. 
