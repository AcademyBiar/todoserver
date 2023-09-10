from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('getinvite/', views.create_invite_code),
    path('adduser/', views.create_user),
    path('addtask/', views.create_task),
    path('get/actual/<int:chat_id>', views.get_actual_task),
    path('get/notactual/<int:chat_id>', views.get_not_actual_task),
    path('set/notactual/', views.set_not_actual)
]