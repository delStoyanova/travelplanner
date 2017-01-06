from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from mysite.models import TodoList
from .serializers import TodoListSerializer, UserSerializer, GroupSerializer


class TodoListList(APIView):
    ## whenever when get request show all todolist
    def get(self, request):
        todolist = TodoList.objects.all()
        ## convert to json all todolist items and we need to specify that they are many of them
        serializers = TodoListSerializer(todolist, many=True)
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
