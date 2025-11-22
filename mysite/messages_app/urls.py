from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_messages, name='messages_home'),  # <--- ВАЖНО!
    path('send_message/<int:user_id>/', views.send_message, name='send_message'),
    path('view_messages/', views.view_messages, name='view_messages'),
]
