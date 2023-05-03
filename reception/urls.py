from django.urls import  path
from . import views
app_name = 'reception'
urlpatterns = [
    path('List', views.list_of_rec, name='listRec'),
    path('reToSurgery/', views.reToSurgery, name= 'reToSurgery'),
    path('<int:id>', views.reception_form, name= 'reception'),
    path('<int:id>/<int:EntranceCode>', views.recption_detail, name= 'receptionDetaile'),
    path('surgery/<int:id>', views.Refer_Surgery, name= 'Refer_Surgery'),
]
