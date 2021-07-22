from django.db import models
 
class Student(models.Model):  
    id = models.CharField(max_length=30,primary_key=True)  
    name = models.CharField(max_length=200)  
    email = models.EmailField()  
    age = models.IntegerField()  
    
    class Meta:  
        db_table = "student" 
