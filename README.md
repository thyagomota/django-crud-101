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

In Django, a view function is a python function that takes a web request and returns a web response. iFor this example, create employees/views.py with the following code:

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