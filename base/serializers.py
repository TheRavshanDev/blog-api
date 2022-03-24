from rest_framework.serializers import ModelSerializer
from .models import Blog
from django.contrib.auth.models import User

class BlogSerializer(ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'

class UsersSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'