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

Create a `templates` folder under `employee` and add the following html templates. 

## index.html 

```html 
<!DOCTYPE html>  
<html lang="en">  
<head>  
    <meta charset="UTF-8">  
    <title>Index</title>  
    {% load staticfiles %}  
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
    <title>Employee Records</title>  
     {% load staticfiles %}  
    <link rel="stylesheet" href="{% static 'css/style.css' %}"/>  
</head>  
<body>  
<table class="table table-striped table-bordered table-sm">  
    <thead class="thead-dark">  
    <tr>  
        <th>Employee ID</th>  
        <th>Employee Name</th>  
        <th>Actions</th>  
    </tr>  
    </thead>  
    <tbody>  
    {% for employee in employees %}  
    <tr>  
        <td>{{ employee.eid }}</td>  
        <td>{{ employee.ename }}</td>   
        <td>  
            <a href="/edit/{{ employee.id }}"><span class="glyphicon glyphicon-pencil" >Edit</span></a>  
            <a href="/delete/{{ employee.id }}">Delete</a>  
        </td>  
    </tr>  
    {% endfor %}  
    </tbody>  
</table>  
<br>  
<br>  
<center><a href="/emp" class="btn btn-primary">Add New Record</a></center>  
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
    {% load staticfiles %}  
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
                <input type="text" name="eid" id="id_eid" required maxlength="20" value="{{ employee.id }}"/>  
            </div>  
        </div>  

        <div class="form-group row">  
            <label class="col-sm-2 col-form-label">Employee Name:</label>  
            <div class="col-sm-4">  
                <input type="text" name="ename" id="id_ename" required maxlength="100" value="{{ employee.name }}" />  
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

Create a `static/css` folder under `employee` and add the following css file (you can name it `employee.css`).

```css
body {font:12px/1.4 Verdana,Arial; background:#eee; height:100%; margin:25px 0; padding:0}
h1 {font:24px Georgia,Verdana; margin:0}
h2 {font-size:12px; font-weight:normal; font-style:italic; margin:0 0 20px}
p {margin-top:0}
ul {margin:0; padding-left:20px}

#testdiv {width:600px; margin:0 auto; border:1px solid #ccc; padding:20px 25px; background:#fff}

#tinybox {position:absolute; display:none; padding:10px; background:#fff url(images/preload.gif) no-repeat 50% 50%; border:10px solid #e3e3e3; z-index:2000}
#tinymask {position:absolute; display:none; top:0; left:0; height:100%; width:100%; background:#000; z-index:1500}
#tinycontent {background:#fff}

.button {font:14px Georgia,Verdana; margin-bottom:10px; padding:8px 10px 9px; border:1px solid #ccc; background:#eee; cursor:pointer}
.button:hover {border:1px solid #bbb; background:#e3e3e3}
```