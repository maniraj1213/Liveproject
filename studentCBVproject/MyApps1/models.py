from django.db import models
#from django.core.urlresolvers import reverse
from django.urls import reverse;
#Create your models here....
class Student(models.Model):
    sno=models.IntegerField();
    sname=models.CharField(max_length=128)
    sheight=models.FloatField(max_length=128)
    sage=models.FloatField(max_length=128)
    def __str__(self):
        return self.sname
    def get_absolute_url(self):
        return reverse('detail',kwargs={'pk':self.pk})
