from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name','email','password']
        
    def create(self, validated_data):
        return User.objects.create_user(**validated_data) 
    
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostModel
        fields = '__all__'

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LikeModel
        fields = '__all__'
    
class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)
    class Meta:
        model = User
        fields=['email','password']    