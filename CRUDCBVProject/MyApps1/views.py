from django.shortcuts import render

# Create your views here.
from MyApps1.models import Company
from django.views.generic import CreateView
class CompanyCreateView(CreateView):
	model=Company

from django.shortcuts import render
from MyApps1.models import Company
from django.views.generic import DetailView, ListView
# Create your views here.
class CompanyListView(ListView):
	model=Company		#companylist = Company.objects.all();
	#default template_name is company_list.html
	#defult context_object_name is company_list var

class CompanyDetailView(DetailView):
	model=Company
	#default template_name is company_detail.html
	#defult context_object_name is "company"o r given-object for company_list, which is in usage for company_list.html

from MyApps1.models import Company
from django.views.generic import CreateView
class CompanyCreateView(CreateView):
	model=Company
	fields = ('name', 'location','ceo')		 #compulsory


from django.views.generic import UpdateView
class CompanyUpdateView(UpdateView):
	model=Company
	fields=('name','ceo');  #auto it takes company_form.html with given-fields

from django.views.generic import DeleteView
from django.urls import reverse_lazy
class CompanyDeleteView(DeleteView):
	model=Company
	success_url=reverse_lazy('list') #given name="" para. of path()
