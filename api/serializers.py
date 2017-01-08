from django.contrib.auth.models import User, Group
from rest_framework import serializers

from mysite.models import TodoList, ProfileUser, Places, Post


# take a model from mysite and serialize it, save data into a format you can send
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['name']


class TodoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoList
        fields = ['user', 'title', 'due_date', 'finished', 'is_done']


class ProfileUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileUser
        fields = ['author', 'avatar']


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['person', 'text','published_date']


class PlacesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Places
        fields = ['owner', 'name']
