from django.urls import path
from users.views import profile_view, user_profile_form_view, signup_view, home, users_list
from django.contrib.auth import views as auth_views



urlpatterns = [
    # главная страница
    # path('', home, name='home'),
    #  профили
    path('profile/edit/', user_profile_form_view, name='user_profile_form'),
    path('profile/<str:username>/', profile_view, name='profile'),
    # регистрация
    path('signup/', signup_view, name='signup'),
    # логин / логаут
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    # список пользователей
    path('users/', users_list, name='users_list'),

]
