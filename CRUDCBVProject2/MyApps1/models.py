from django.db import models
#from django.core.urlresolvers import reverse
from django.urls import reverse;
#Create your models here....
class Employee(models.Model):
    empno=models.IntegerField();
    ename=models.CharField(max_length=128)
    job=models.CharField(max_length=128)
    sal=models.FloatField(max_length=128)
    def __str__(self):
        return self.ename
    def get_absolute_url(self):
        return reverse('detail',kwargs={'pk':self.pk})
