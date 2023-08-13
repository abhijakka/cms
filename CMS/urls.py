"""restapiproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path,include
from mainapp.views import *

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', UserCreateView.as_view(), name='user-create'),
    path('posts/', PostCreateView.as_view(), name='post-create'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('likes/', LikeCreateView.as_view(), name='like-create'),
    path('posts_with_likes/', PostListWithLikesView.as_view(), name='post-list-with-likes'),
    path('authenticate/', UserAuthenticationAPIView.as_view(), name='user-authenticate'),
    
    #private user

    path('private/user/posts/<int:pk>/', PrivatePostDetailView.as_view(), name='private-post-detail'),
    path('private/user/likes/', PrivateLikeCreateView.as_view(), name='private-like-create'),
    path('private/user/posts_with_likes/', PrivatePostListWithLikesView.as_view(), name='private-post-list-with-likes'),
   
]
urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
   
    

