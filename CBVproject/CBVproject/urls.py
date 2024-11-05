from django.contrib import admin
from django.urls import path
from MyApps1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('helloworld/', views.HelloWorldView.as_view()),

    path('home/', views.TemplateCBV.as_view()),
    path('booklistview/',views.BookListView.as_view()),
    path('companies/',views.CompanyListView.as_view()),
    path('<pk>/',views.CompanyDetailView.as_view()),

]
