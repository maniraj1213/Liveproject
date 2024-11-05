from django.contrib import admin
from MyApps1.models import Book
from MyApps1.models import Company
from MyApps1.models import Employee

class BookAdmin(admin.ModelAdmin):
    list_display = ["title","author","pages","price"];
admin.site.register(Book, BookAdmin)



class Companyadmin(admin.ModelAdmin):
    list_display=["name","loction","CEO"];
admin.site.register(Company,Companyadmin)



class EmployeeAdmin(admin.ModelAdmin):
    list_display=['eno','name','salary','company'];

admin.site.register(Employee,EmployeeAdmin)


