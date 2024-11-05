from django.shortcuts import render
from MyApps1.models import Student
#from django.core.urlresolvers import reverse_Jazy #old-lib
from django.urls import reverse_lazy	#new-lib
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
# Create your views here.
class StudentListView(ListView):
    model = Student

class StudentDetailView(DetailView):
    model = Student

class StudentCreateView(CreateView):
    model = Student
    #fields=('sid','sname','sheight','sage')
    fields = '__all__'

class StudentUpdateView(UpdateView):
    model = Student
    fields = ('sno','sname', 'sheight', 'sage')

class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('home')
