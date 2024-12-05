from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView
from django.db import IntegrityError

from users.models import CustomUser, Follow


# Create your views here.
class UserRegisterView(TemplateView):
    """" вью для регистрации пользователя """
    template_name = 'sign_up.html'


class ProfileView(TemplateView):
    """ вью для страницы профиля """
    template_name = 'profile.html'

    def dispatch(self, request, *args, **kwargs):
        # Проверка аутентификации
        if not request.user.is_authenticated:
            return redirect('login-url')
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        user = self.request.user

        followers_count = user.my_followers.all().count()
        followings_count = user.my_following.all().count()
        publications_count = user.publications.all().count()
        publications = user.publications.all()
        context = {
            'user': user,
            'followers_count': followers_count,
            'followings_count': followings_count,
            'publications_count': publications_count,
            'publications': publications,
        }
        return context



class MakeRegisterView(View):
    """Вьюшка для регистрации пользователя"""
    def post(self, request, *args, **kwargs):
        data = request.POST
        password = data['password']
        username = data['username']
        first_name = data['first_name']
        last_name = data['last_name']

        try:
            user = CustomUser.objects.create_user(
                username=username,
                password=password,
                first_name=first_name,
                last_name=last_name
            )
            user.save()

            login(request, user)
            return redirect('home-url')
        except IntegrityError:
            return redirect('register-url')



class LoginView(TemplateView):
    """Вьюшка для входа в аккаунт"""
    template_name = 'login.html'



class MakeLoginView(View):
    """Вьюшка для логина"""
    def post(self, request, *args, **kwargs):
        data = request.POST
        username = data.get('username')
        password = data.get('password')

        try:
            user = CustomUser.objects.get(username=username)
        except CustomUser.DoesNotExist:
            return redirect('login-url')

        if user.check_password(password):
            login(request, user)
            return redirect('home-url')
        else:
            return redirect('login-url')




class MakeFollowView(View):
    """ вью для подписки """
    def post(self, request, *args, **kwargs):
        user = request.user
        follow_id = kwargs['pk']



        user_follower = CustomUser.objects.get(id=follow_id)

        if Follow.objects.filter(follower=user, following=user_follower).exists():
            Follow.objects.filter(follower=user, following=user_follower).delete()
        else:
            Follow.objects.create(follower=user, following=user_follower)



        return redirect('home-url',)



class MakeLogoutView(View):
    """ вью для выхода из аккаунта """
    def post(self, request, *args, **kwargs):
        logout(request)
        return redirect('login-url')


