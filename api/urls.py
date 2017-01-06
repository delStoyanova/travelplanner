from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.routers import DefaultRouter

from . import views

app_name = 'api'
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
# ^ begin $ end,+ several decimal long pattern
urlpatterns = [
    url(r'^items/$', views.TodoListList.as_view(), name='items'),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
