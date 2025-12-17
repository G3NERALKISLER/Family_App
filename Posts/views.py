from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Post
from . import forms
# Create your views here.
@login_required(login_url="login/")
def Home_page(request):
    return render(request, 'posts/home.html')
def Post_Page(request):
    posts = Post.objects.all().order_by('-date')
    return render(request, 'posts/Posts.html', {'posts':posts})
def Post_Detail(request, slug):
    post= Post.objects.get(slug=slug)
    return render(request, 'posts/Post_detail.html', {'post':post})
def new_post(request):
    if request.method == "POST": 
        form = forms.CreatePost(request.POST, request.FILES)
        if form.is_valid():
            newpost = form.save(commit=False)
            newpost.author = request.user
            newpost.save()
            return redirect('posts:postpage')
    else:
        form = forms.CreatePost()
        return render(request, 'posts/new_post.html', {'form': form})