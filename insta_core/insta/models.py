from django.core.validators import FileExtensionValidator
from django.db import models
from users.models import CustomUser

# Create your models here.
class Publication(models.Model):
    """ вью для публикации пользователя """

    author = models.ForeignKey(CustomUser,
                               on_delete=models.CASCADE,
                               related_name='publications'
                               )
    description = models.TextField()
    publication_date = models.DateField(auto_now_add=True)
    file = models.FileField(upload_to='uploads/',
        validators=[FileExtensionValidator(allowed_extensions=[
            'jpg',
            'png',
            'mp4',
            'avi',
            'jpeg'
        ])]
    )
    like = models.ManyToManyField(CustomUser,  related_name='likes' )


class UserComment(models.Model):
    """ вью для комментариев пользователей """
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='comments_user' )
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE, related_name='comments_publications' )
    text = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

