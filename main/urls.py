from django.urls import path
from main.views import banner_list

urlpatterns = [
    path('',banner_list,name='banner')
    
]
