from django.contrib.auth.models import User
from django.db import models
from django.conf import settings


# Create your models here.
# models.py

class FriendRequest(models.Model):
    from_user = models.ForeignKey(User, related_name='from_user', on_delete=models.CASCADE)
    to_user = models.ForeignKey(User, related_name='to_user', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"From {self.from_user.username} to {self.to_user.username}"

    class Meta:
        verbose_name = 'Запрос другу'
        verbose_name_plural = 'Запросы друзьям'
        ordering = ['timestamp']


"""
# уже есть эта логика в @login_required -- def accept_friend_request


class Friendship(models.Model):
    user1 = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='friendship_user1', on_delete=models.CASCADE)
    user2 = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='friendship_user2', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        unique_together = ('user1', 'user2')


    def __str__(self):
        return f"{self.user1} <-> {self.user2}"
"""
