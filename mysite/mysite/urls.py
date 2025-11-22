
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from users.views import home
from django.contrib.auth import views as auth_views

urlpatterns = [
    # главная страница
    path('', home, name='home'),
    # админка
    path('admin/', admin.site.urls),
    # Авторизация
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # пользователи(регистрация, профиль, редактирование)
    path('', include('users.urls')),
    # друзья
    path('friends/', include('friends.urls')),
    # посты
    path('posts/', include('posts.urls')),
    # сообщения
    path('messages/', include('messages_app.urls')),

]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)