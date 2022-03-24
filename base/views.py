from rest_framework.viewsets import ModelViewSet
from .models import Blog
from .serializers import BlogSerializer, UsersSerializer
from django.contrib.auth.models import User
from rest_framework import filters

class HomeViewSet(ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    filter_backends = [filters.OrderingFilter,filters.SearchFilter,]
    ordering_fields = ['id','title',]
    search_fields = ['id','title','date',]

class UsersViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsersSerializer
