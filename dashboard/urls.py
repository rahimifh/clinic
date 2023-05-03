from django.urls import path
from dashboard.views import *

app_name = 'dashboard'
urlpatterns = [
    path('lottery/list/', GameListView.as_view(), name='DashboardGameListView'),
    #path('lottery/<pk>/detail/', GameDetailView.as_view(), name='DashboardGameDetailView'),
    path('', DashboardView.as_view(), name='dashboard'),
    # path('in/', Dashboard2View.as_view(), name='dashboard2'),
    # path('dashboard/', DashboardView.as_view()),
]
