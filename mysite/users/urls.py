from django.urls import path
from users.views import profile_view, user_profile_form_view

urlpatterns = [

    path('profile/edit/', user_profile_form_view, name='user_profile_form'),
    path('profile/<str:username>/', profile_view, name='profile'),

]
