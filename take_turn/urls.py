from django.urls import  path
from . import views
app_name = 'turn'
urlpatterns = [
    path('', views.take_turn, name= 'take_turn'),
    path('<int:id>', views.take_turn_s, name= 'take_turn_s'),
    path('del/<int:id>', views.delete_turn, name= 'delete_turn'),
    path('delh/<int:id>', views.delete_turn_h, name= 'delete_turn_h'),

]
