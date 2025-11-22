from django.urls import path
from . import views

urlpatterns = [
    # Список всех постов
    path('', views.post_list, name='post_list'),

    # Создать пост
    path('create/', views.create_post, name='create_post'),

    # Просмотр конкретного поста
    path('<int:post_id>/', views.post_detail, name='post_detail'),

    # Добавить комментарий к посту
    path('<int:post_id>/comment/', views.add_comment, name='add_comment'),

    # Редактировать пост
    path('<int:post_id>/edit/', views.edit_post, name='edit_post'),

    # Удалить пост
    path('<int:post_id>/delete/', views.delete_post, name='delete_post'),
]
