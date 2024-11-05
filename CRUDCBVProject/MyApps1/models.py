from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=128)
    location = models.CharField(max_length=64)
    ceo = models.CharField(max_length=64)


from django.db import models
# from django.core.urlresolvers import reverse #old-lib
from django.urls import reverse;  # new-lib


class Company(models.Model):
    name = models.CharField(max_length=128)
    location = models.CharField(max_length=64)
    ceo = models.CharField(max_length=64)

    def __str__(self):
        return self.name;

    def get_absolute_url(self):
        # return reverse('detail', kwargs={'pk': self.pk})
        return reverse('list')
