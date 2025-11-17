from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from friends.models import FriendRequest


@login_required
def send_friend_request(request, user_id):
    """
    Отправка заявки в друзья
    """
    to_user = get_object_or_404(User, id=user_id)

    # Проверяем, чтобы не отправлять запрос самому себе
    if to_user != request.user:
        FriendRequest.objects.get_or_create(
            from_user=request.user,
            to_user=to_user
        )

    # Переход на профиль пользователя
    return redirect('profile', username=to_user.username)


@login_required
def accept_friend_request(request, request_id):
    """
    Принятие заявки в друзья
    """
    friend_request = get_object_or_404(FriendRequest, id=request_id)

    # Проверяем, что заявка направлена текущему пользователю
    if friend_request.to_user == request.user:

        # Добавляем друг друга
        request.user.userprofile.friends.add(friend_request.from_user.userprofile)
        friend_request.from_user.userprofile.friends.add(request.user.userprofile)

        # Удаляем заявку
        friend_request.delete()

    # Возврат на свой профиль
    return redirect('profile', username=request.user.username)
