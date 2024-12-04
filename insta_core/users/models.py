from django.contrib.auth.models import AbstractUser
from django.db import models

from users.managers import CustomUserManager


# Create your models here.
class CustomUser(AbstractUser):
    """модель для кастомного пользователя"""

    username = models.CharField(max_length=22, unique=True)


    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    avatar = models.ImageField(blank=True, upload_to='avatars/')

    objects = CustomUserManager()


    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'


class Follow(models.Model):
    """ вью для подписки друг на друга """
    follower = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='my_followers', null=True)
    following = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='my_following', null=True)
    created_ad = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'подписка'
        verbose_name_plural = 'подписки'
        unique_together = ('follower', 'following')


# class Like(models.Model):
#     """ вью для лайков публикаций """
#     user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='user_likes')
#     publication = models.ForeignKey("insta.Publication", on_delete=models.CASCADE, related_name='publication_likes')
#     created_at = models.DateTimeField(auto_now_add=True)
#     class Meta:
#         verbose_name = 'лайк'
#         verbose_name_plural = 'лайки'


