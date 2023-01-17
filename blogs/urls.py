
from django.contrib import admin
from django.urls import path
from . import views
import jobs.views

urlpatterns = [
    path('', views.allblogs , name='allblogs'),
    path('<int:blog_id>/', views.details, name='Detail'),
]
