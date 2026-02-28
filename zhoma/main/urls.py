from django.urls import path
from . import views

urlpatterns = [
    path('',views.celebrity_list, name='Celebrity'),
    
]
   