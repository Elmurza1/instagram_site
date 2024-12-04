from django.contrib import admin
from .models import Publication, UserComment


# Register your models here.

@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ['author', ]

@admin.register(UserComment)
class UserCommentAdmin(admin.ModelAdmin):
    list_display = ['user',  'text']

