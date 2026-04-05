from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.index, name='index'), 
    path('dishes/<str:dish>', views.dishes),
    path('form/', views.ApForm),
    path('success/', views.success, name="success"),
    path('about/', views.about, name="aboutSection"),
    path('allDishes/', views.alldishes, name="allDishes"),
    path('home/', views.home, name='home'), 
    path('register/', views.register, name='register'),  
    path('login/', views.login, name='login'),  
] 