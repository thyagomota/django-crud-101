from django.db import models  

class Employee(models.Model):  

    id   = models.IntegerField 
    name = models.CharField(max_length=50)  
     
    class Meta:  
        db_table = "employees"  
