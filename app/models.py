from django.db import models

# Create your models here.
class School(models.Model):
    scname=models.CharField(primary_key=True,max_length=100)
    scloc=models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.scloc
class Student(models.Model):
    scname=models.ForeignKey(School,on_delete=models.CASCADE)
    stdname=models.CharField(max_length=100)
    stdid=models.IntegerField(primary_key=True)

    def __str__(self) -> str:
        return self.stdname
    

