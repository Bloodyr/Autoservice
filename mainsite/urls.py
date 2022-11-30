from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_page, name="home_page"),
    path('registration/', views.register_page, name="registration"),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('cars/',views.cars_page,name='cars_page'),
    path('cars_details/',views.cars_details_page,name='cars_details_page'),
    path('settings/', views.settings_page, name='settings_page'),
    path('order_info/', views.order_info_page, name='order_info_page'),
    path('order_detail/<int:pk>/', views.order_detail_page, name='order_detail_page'),
    path('part_list/', views.part_list_page, name='part_list_page'),
    path('part_detail/<int:pk>/', views.part_detail_page, name='part_detail_page'),
    path('part_detail/part_check_page/<int:pk>/', views.part_check_page, name='part_check_page'), 
    path('job_list_page/', views.job_list_page, name='job_list_page'),
    path('job_list_page/details/<int:pk>/', views.job_details, name='job_details')
]