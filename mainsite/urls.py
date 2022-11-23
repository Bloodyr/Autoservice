from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_page, name="home_page"),
    path('registration/', views.register_page, name="registration"),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('cars/',views.cars_page,name='cars_page'),
    path('cars_details/',views.cars_details_page,name='cars_details_page'),
    path('settings/', views.settings_page, name='settings_page')
]