
from django.contrib import admin
from django.urls import path,include
from .import views
urlpatterns = [
    path("",views.classbaseview.as_view(),name="classbaseview"),
    path('classtemplate',views.classtemplate.as_view(),name="classtemplate"),
    path('Displyinfo',views.Displyinfo.as_view(),name="Displyinfo")
]
