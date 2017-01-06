from django.contrib.auth.models import User, Group
from rest_framework import serializers

from mysite.models import TodoList


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
