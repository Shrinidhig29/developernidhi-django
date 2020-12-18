from django.contrib import admin
from django.urls import path, include
from home import views

# Django admin customization

admin.site.site_header = " Log In Developer Nidhi"
admin.site.site_title = "Welcome to Nidhi's Dashboard"
admin.site.index_title = "Welcome to this Portal"

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('about', views.about, name='about'),
    # path('projects', views.projects, name='projects'),
    path('contact', views.contact, name='contact'),
    path('services', views.services, name='services'),
]
