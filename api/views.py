from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from mysite.models import TodoList, Places, Post, ProfileUser
from .serializers import TodoListSerializer, UserSerializer, GroupSerializer, PlacesSerializer, PostSerializer, \
    ProfileUserSerializer


class TodoListItems(APIView):
    ## whenever when get request show all todolist
    def get(self, request):
        todolist = TodoList.objects.all()
        ## convert to json all todolist items and we need to specify that they are many of them
        serializers = TodoListSerializer(todolist, many=True)
        ##send the json data
        return Response(serializers.data)


class PlacesList(APIView):
    ## whenever when get request show all places
    def get(self, request):
        places = Places.objects.all()
        ## convert to json all places items and we need to specify that they are many of them
        serializers = PlacesSerializer(places, many=True)
        ##send the json data
        return Response(serializers.data)


class PostsList(APIView):
    ## whenever when get request show all posts
    def get(self, request):
        posts = Post.objects.all()
        ## convert to json all post items and we need to specify that they are many of them
        serializers = PostSerializer(posts, many=True)
        ##send the json data
        return Response(serializers.data)


class ProfileUserLists(APIView):
    ## whenever when get request show all profile
    def get(self, request):
        profile = ProfileUser.objects.all()
        ## convert to json all profile items and we need to specify that they are many of them
        serializers = ProfileUserSerializer(profile, many=True)
        ##send the json data
        return Response(serializers.data)


class UserViewSet(viewsets.ModelViewSet):
    ## it is allowed that users are viewed and edited
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    ## it is allowed that groups are viewed and edited
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
