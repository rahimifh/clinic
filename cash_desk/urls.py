from django.urls import  path
from . import views
urlpatterns = [
    path('', views.cash_desk_form, name= 'desk_form'),


]
