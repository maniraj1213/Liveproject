from django.contrib import admin
from MyApps1.models import Student
#Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ['sno','sname','sheight','sage']

admin.site.register(Student, StudentAdmin)
