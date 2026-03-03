from django.urls import path
from . import views

urlpatterns = [
    path('celebrities/',views.celebrity_list, name='Celebrity'),
    path('celebrity/<int:id>/' ,views.look_detail, name = 'Lookdetail'),
    path('', views.nav_bar , name='Home')
    
]
   