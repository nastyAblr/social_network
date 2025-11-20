
from django.utils import timezone
from django.contrib.auth.models import User
from django.db import models




class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True, verbose_name='Фото')
    description = models.TextField(blank=True, verbose_name='описание')
    registration_date = models.DateTimeField(default=timezone.now, verbose_name='дата регистрации')

    friends = models.ManyToManyField('self', symmetrical=True, blank=True)


    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Профиль пользователя'
        verbose_name_plural = 'Профиль пользователя'
        ordering = ['registration_date']