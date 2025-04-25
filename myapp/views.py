from django.shortcuts import render,redirect
from .models import Post
from .forms import PostForm


def home(request):
    posts = Post.objects.all().order_by('-published_date')
    return render(request, 'home.html',{'posts':posts})

def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'add_post.html', {'form': form})