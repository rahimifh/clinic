from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from . import views

app_name = 'account'

urlpatterns = [

    path('login/', csrf_exempt(views.user_login), name='login'),
    path('profile/', views.profile, name='profile'),
    path('logout',views.logoutuser, name='logoutuser')
]
