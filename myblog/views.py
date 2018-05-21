from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from myblog.models import Post
from django.contrib.auth.models import User
from .forms import PostForm
#import pdb; pdb.set_trace()

def post_list(request):
	me = User.objects.get(username="breakbadsp")
	posts = Post.objects.filter(author=me).order_by('published_date')
	return render(request, 'myblog/post_list.html', {'posts':posts})

	
def post_detail(request, pk):
	#Post.objects.get(pk=pk)
	post = get_object_or_404(Post,pk=pk)
	return render(request, 'myblog/post_detail.html', {'post':post})
	
def post_new(request):
    form = PostForm()
    return render(request, 'myblog/post_edit.html', {'form': form})