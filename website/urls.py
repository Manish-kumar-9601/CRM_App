 
from django.contrib import admin # type: ignore
from django.urls import path# type: ignore
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    # path('login/',views.login_user,name='login')
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('customer_record/<int:pk>', views.customer_record, name='customer_record'),
    path('delete_customer_record/<int:pk>', views.delete_customer_record, name='delete_customer_record'),
    path('add_record/',views.add_record,name='add_record'),
]
