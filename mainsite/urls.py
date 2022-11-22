from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_page, name="home_page"),
    path('registration/', views.register_page, name="registration"),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logoutUser, name='logout')
]