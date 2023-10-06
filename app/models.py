from django.db import models

# Create your models here.

class Course(models.Model):
    Cid = models.IntegerField()
    Cname = models.CharField(max_length=20)
    ctrainer = models.CharField(max_length=50)
    
    def __str__(self):
        return self.Cname

class Student(models.Model):
    Sid = models.IntegerField()
    Sname = models.CharField(max_length=100)
    Sage = models.IntegerField()
    Cid = models.ForeignKey(Course,on_delete=models.CASCADE)

    def __str__(self):
        return self.Sname