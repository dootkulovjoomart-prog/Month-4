from django.urls import path
from . import views

urlpatterns = [
    path('celebrities/',views.celebrity_list, name='Celebrity'),
    path('celebrity/<int:id>/' ,views.look_detail, name = 'Lookdetail'),
    path('create-celebrities/' , views.create_celebrities , name='create_celebrities'),
    path('', views.nav_bar , name='home')
    
]
   