from django.db import models


class Book(models.Model):
    title=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    pages=models.IntegerField()
    price=models.FloatField()

class Company(models.Model):
        name=models.CharField(max_length=100)
        loction=models.CharField(max_length=100)
        CEO=models.CharField(max_length=100)

        def __str__(self):  ##add-this extra-code
          return self.name;


class Employee(models.Model):   #child-table
    eno=models.IntegerField()
    name=models.CharField(max_length=128)
    salary=models.FloatField()
    company=models.ForeignKey(Company,related_name='employees',on_delete=models.CASCADE)
