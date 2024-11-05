from django.shortcuts import render
from MyApps1.models import Employee
#from django.core.urlresolvers import reverse_Jazy #old-lib
from django.urls import reverse_lazy	#new-lib
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
# Create your views here.
class EmployeeListView(ListView):
    model = Employee

class EmployeeDetailView(DetailView):
    model = Employee

class EmployeeCreateView(CreateView):
    model = Employee
    #fields=('empno', 'ename','job', 'sal')
    fields = '__all__'

class EmployeeUpdateView(UpdateView):
    model = Employee
    fields = ('ename', 'job', 'sal')

class EmployeeDeleteView(DeleteView):
    model = Employee
    success_url = reverse_lazy('home')
