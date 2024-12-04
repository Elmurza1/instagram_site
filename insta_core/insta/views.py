from urllib import request
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView

from insta.models import Publication, UserComment
from users.models import CustomUser, Follow


# Create your views here.


class HomeView(TemplateView):
    """ вью для домашней страницы  """

    template_name = 'home.html'


    def dispatch(self, request, *args, **kwargs):
        # Проверка аутентификации
        if not request.user.is_authenticated:
            return redirect('login-url')
        return super().dispatch(request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        user = self.request.user

        following = user.my_followers.all()
        publication = Publication.objects.all()
        # likes = user.user_likes.all().count()


        context = {
            'user': CustomUser.objects.all(),
            'following': following,
            'publication': publication,

        }
        return context


class AddLike(View):
    """ вью для добавления лайка публикации """
    def post(self, request, *args, pk ,**kwargs):
        # publication_id = kwargs['pk']
        publication_id = Publication.objects.get(pk=pk)

        user = request.user

        if user in publication_id.like.all():
            publication_id.like.remove(user)
        else:
            publication_id.like.add(user)
        return redirect('home-url')


class MakePostView(View):
    """ вью для публикации """
    def post(self, request, *args, **kwargs):
        description = request.POST.get('description')
        file = request.FILES.get('image')
        user = request.user

        if description and file:
            publication = Publication.objects.create(
                description=description,
                file=file,
                author=user
            )
            return redirect('home-url')
        if not file:
            print('yyyyyy где фто')

        return redirect('home-url')


class SendCommentView(View):
    """ вью для отправки коментов от пользователя  """
    def post(self, request, *args, **kwargs):
        publication_id = kwargs['pk']
        publication = Publication.objects.get(pk=publication_id)

        comment = request.POST.get('comment')
        user = request.user

        if comment:
            UserComment.objects.create(
                text=comment,
                publication=publication,
                user=user
            )
        return redirect('home-url')

