"""
URL configuration for insta_core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls.static import static
from django.conf.urls.static import settings
from django.urls import path
from insta.views import  HomeView, AddLike, MakePostView, SendCommentView
from users.views import UserRegisterView, ProfileView, MakeRegisterView, LoginView, MakeLoginView, MakeFollowView, MakeLogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register-list/', UserRegisterView.as_view(), name='register-url'),
    path('', HomeView.as_view(), name='home-url'),
    path('make-register-url/', MakeRegisterView.as_view(), name='make-register'),
    path('login-list/', LoginView.as_view(), name='login-url'),
    path('make-login-url/', MakeLoginView.as_view(), name='make-login'),
    path('profile-list/', ProfileView.as_view(), name='profile-url'),
    path('make-follow-url/<int:pk>/', MakeFollowView.as_view(), name='make-follow'),
    path('add-like/<int:pk>/', AddLike.as_view(), name='add-like'),
    path('make-post-url/', MakePostView.as_view(), name='make-post'),
    path('publication/<int:pk>/send-comment', SendCommentView.as_view(), name='send-comment'),
    path('logout-list/', MakeLogoutView.as_view(), name='logout-url')

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
