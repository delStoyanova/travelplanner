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
    url(r'^itemslist/$', views.TodoListItems.as_view(), name='itemslist'),
url(r'^postslist/$', views.PostsList.as_view(), name='postslist'),
url(r'^placeslist/$', views.PlacesList.as_view(), name='placeslist'),
url(r'^profileslist/$', views.ProfileUserLists.as_view(), name='profileslist'),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
