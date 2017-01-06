from django.conf.urls import url
from django.contrib.auth.views import password_change

from . import views

app_name = 'mysite'
# ^ begin $ end,+ several decimal long pattern
urlpatterns = [
    # mysite/1/ user id=1
    # url(r'^home/(?P<user_id>[0-9]+)$', index),
    # url(r'^share/$', views.share, name='share'),
    url(r'^$', views.home, name='home'),
    url(r'^home/$', views.home, name='home'),
    url('^change-password/$', password_change, {'post_change_redirect': 'mysite:userprofile'}, name='password_change'),
    url(r'^userprofile/$', views.profile, name='userprofile'),
    url(r'^photo/$', views.photo, name='photo'),
    url(r'^register/$', views.UserFormView.as_view(), name='register'),
    url(r'^login/$', views.UserLogin.as_view(), name='login'),
    url(r'^userlogout/$', views.user_logout, name='userlogout'),
    url(r'^mytodolist/$', views.ListFormView.as_view(), name='mytodolist'),
    url(r'^pack/$', views.pack, name='pack'),
    url(r'^guides/$', views.guides, name='guides'),
    url(r'^places/$', views.PlacesFormView.as_view(), name='places'),
    url(r'^share/$', views.PostFormView.as_view(), name='share'),
    url(r'^attractive.places/$', views.attractive_places, name='attractive.places'),
    url(r'^advices/$', views.advices, name='advices'),
    url(r'^deleteallitems/$', views.deleteall, name='deleteallitems'),
    url(r'^deleteitem/(?P<item_id>\d+)/$', views.deleteitem, name="deleteitem"),
    url(r'^finishitem/(?P<item_id>\d+)/$', views.finishitem, name="finishitem"),
    url(r'^findplace/(?P<place_id>\d+)/$', views.findplace, name="findplace"),
    url(r'^deleteplace/(?P<place_id>\d+)/$', views.deleteplace, name="deleteplace"),
    url(r'^deletepost/(?P<post_id>\d+)/$', views.deletepost, name="deletepost"),
]
