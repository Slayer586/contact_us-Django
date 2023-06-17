
from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.contactus , name="contactus"),   
    path("contactus", views.contactus , name="contactus"),   
]
