from django.urls import path
from . import views



urlpatterns = [
    path('create/', views.create_post, name='create_post'),
    path('<int:post_id>/comment/', views.add_comment, name='add_comment'),
]