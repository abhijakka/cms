from rest_framework import generics
from .models import *
from .seralizers import UserSerializer, PostSerializer, LikeSerializer
from django.db.models import Count
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.views import APIView



def get_refresh_token(user):
    refresh=RefreshToken.for_user(user)
    return {
        'refresh':str(refresh),
        'access':str(refresh.access_token), 
    }



class UserAuthenticationAPIView(APIView):
    
    def post(self, request):
    
        email = request.data.get('email')
        password = request.data.get('password')
        print(email,password)
       
        user = authenticate(email=email,password=password)
        print(user)
        
        if user is not None:
            token = get_refresh_token(user)
            def __init__(self):
                  abhi=self.token
            return Response({'token':token,'msg':'Login Success'}, status=status.HTTP_200_OK)
        else:
            return Response({'errors':{'non_field_errors':['Email or Password is not Valid']}},
                status=status.HTTP_404_NOT_FOUND) 
            
            

class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    



class PostDetailView(generics.ListAPIView):
    queryset = PostModel.objects.filter(is_public=True)
    serializer_class = PostSerializer
    

class LikeCreateView(generics.CreateAPIView):
    queryset = LikeModel.objects.filter(post__is_public=True)
    serializer_class = LikeSerializer

class PostListWithLikesView(generics.ListAPIView):
    queryset = LikeModel.objects.filter(post__is_public=True)
    serializer_class = LikeSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.annotate(like_count=Count('like_id'))
        return queryset
    


#private user
class PostCreateView(generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]

    queryset = PostModel.objects.all()
    
    serializer_class = PostSerializer
        
class PrivatePostDetailView(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = PostModel.objects.all()
    serializer_class = PostSerializer 
    
class PrivateLikeCreateView(generics.CreateAPIView):
    queryset = LikeModel.objects.all()
    serializer_class = LikeSerializer

class PrivatePostListWithLikesView(generics.ListAPIView):
    queryset = LikeModel.objects.all()
    serializer_class = LikeSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.annotate(like_count=Count('like_id'))
        return queryset       