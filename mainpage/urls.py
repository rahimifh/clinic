from django.urls import  path
from . import views
app_name = 'main'
urlpatterns = [

    path('', views.Home, name= 'home'),
    path('search/',views.searchb_us,name='search'),
    path('report/',views.pationt_list, name='pationt_list'),
    path('surgery_list/',views.surgery_list, name='surgery_list'),
    path('Turn_list/',views.Turn_list, name='Turn_list'),
    path('create',views.creatFile, name='creatFile'),
    path('calender',views.Calender, name='Calender'),
    path('<int:id>/', views.patient_file,name='patient_file'),
    path('p_download', views.download, name="p_download"),
    path('s_download', views.download2, name="s_download"),
    path('t_download', views.download3, name="t_download"),
    path('res_download', views.download4, name="p_download4")


]
