from django.urls import path

from messages_app.views import send_message, view_messages




urlpatterns = [

    path('send_message/<int:user_id>/', send_message, name='send_message'),
    path('view_messages/', view_messages, name='view_messages'),
]


