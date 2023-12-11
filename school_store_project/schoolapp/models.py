from django.db import models


class Department(models.Model):
    department_name=models.CharField(max_length=50)
    def __str__(self): 
      return self.department_name

class Course(models.Model):
    
    name=models.CharField(max_length=50)
    department_id=models.ForeignKey(Department,on_delete=models.CASCADE)
    def __str__(self):
        return self.name
class Purpose(models.Model):
    purpose=models.CharField(max_length=30)
    def __str__(self):
        return self.purpose

class Person(models.Model):
    name=models.CharField(max_length=30)
    dob=models.DateField()
    age=models.IntegerField()
    phone=models.CharField(max_length=50)
    mail=models.EmailField()
    address=models.TextField()
    department=models.ForeignKey(Department,on_delete=models.SET_NULL,blank=True,null=True)
    course=models.ForeignKey(Course,on_delete=models.SET_NULL,blank=True,null=True)
    purpose=models.ForeignKey(Purpose,on_delete=models.SET_NULL,blank=True,null=True)
    material=models.CharField(max_length=50,unique=True)

    def __str__(self):
        return self.name






