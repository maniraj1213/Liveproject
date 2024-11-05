from django.contrib import admin

from MyApps1.models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['empno','ename','job','sal','address'];

admin.site.register(Employee,EmployeeAdmin)
