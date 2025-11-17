from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from users.models import UserProfile
from users.forms import UserProfileForm
from friends.models import FriendRequest


@login_required
def profile_view(request, username):
    """
    Просмотр профиля пользователя
    """
    user_profile = get_object_or_404(UserProfile, user__username=username)
    profile_user = user_profile.user

    # Входящие заявки (кому Я нужен)
    incoming_requests = FriendRequest.objects.filter(to_user=request.user)

    # Исходящие заявки (кого хочу Я)
    outgoing_requests = FriendRequest.objects.filter(from_user=request.user)

    # Проверка: уже друзья?
    is_friend = user_profile in request.user.userprofile.friends.all()

    # Входящая заявка от этого пользователя
    incoming_request = FriendRequest.objects.filter(
        from_user=profile_user, to_user=request.user
    ).first()

    # Исходящая заявка к этому пользователю
    outgoing_request = FriendRequest.objects.filter(
        from_user=request.user, to_user=profile_user
    ).first()

    return render(request, "users/profile.html", {
        "user_profile": user_profile,
        "incoming_requests": incoming_requests,
        "outgoing_requests": outgoing_requests,
        "incoming_request": incoming_request,
        "outgoing_request": outgoing_request,
        "is_friend": is_friend,
    })


@login_required
def user_profile_form_view(request):
    """
    Редактирование профиля пользователя
    """
    profile, created = UserProfile.objects.get_or_create(user=request.user)

    if request.method == "POST":
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect("profile", username=request.user.username)
    else:
        form = UserProfileForm(instance=profile)

    return render(request, "users/user_profile_form.html", {
        "form": form,
        "profile": profile,
    })
