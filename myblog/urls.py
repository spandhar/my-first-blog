from django.conf.urls import urls
from . import views

urlpatters = [
	url(r'^$', views.post_list, name='post_list')
]