from django.shortcuts import render
from django.utils import timezone
from myblog.models import Post
from django.contrib.auth.models import User

def post_list(request):
	me = User.objects.get(username="breakbadsp")
	posts = Post.objects.filter(author=me).order_by('published_date')
	return render(request, 'myblog/post_list.html', {'posts':posts})
