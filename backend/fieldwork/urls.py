from django.contrib import admin
from django.urls import path, include
from . import views





app_name = 'fieldwork'

urlpatterns = [
    # path('', views.index, name='index'),
    path('index', views.index, name="index"),
    path('fielduser/', views.fielduser_formpage, name="fielduser-form"),

    path('fielduser/create/', views.FieldUserCreateView.as_view(), name="fielduser-create")
    # path('observation/user_form/', views.user_entered, name="user_entered"),


    ]