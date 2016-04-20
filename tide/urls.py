from django.conf.urls import url
from . import views

urlpatterns = [
	# /tide/ - points to the /tide/ page
	url(r'^$', views.index, name='index'),
	
	# /tide/1/ - accepts any integer from 0 to a billion or more
	# or any combination of integers you can think of
	url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),

	# /tide/234/favourite/ - to fav a song
	url(r'^(?P<album_id>[0-9]+)/favorite/$', views.favorite, name='favorite'),

]
