from django.contrib.auth.base_user import BaseUserManager

class CustomUserManager(BaseUserManager):
    """кастомный менеджер для модели CustomUser"""
    def create_user(self, username, password, **extra_fields):
        """создает и сохраняет нового пользователя с паролем"""
        if not username:
            raise ValueError("Пожалуйста, введите номер телефона.")
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password, **extra_fields):
        """создает и сохраняет нового суперпользователя с паролем"""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        return self.create_user(username, password, **extra_fields)
