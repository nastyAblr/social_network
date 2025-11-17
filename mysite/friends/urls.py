from django.urls import path
from friends.views import send_friend_request, accept_friend_request

urlpatterns = [
    path('send_friend_request/<int:user_id>/', send_friend_request, name='send_friend_request'),
    path('accept_friend_request/<int:request_id>/', accept_friend_request, name='accept_friend_request'),
]
