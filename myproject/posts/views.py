from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Post
from django.contrib.auth.decorators import login_required
from .form import CreateForm

# Create your views here.
def posts_list(request):
    # Displaying Posts with Template Tags
    posts = Post.objects.all()
    return render(request, 'posts/post_list.html', {'posts': posts})

def posts_page(request, slug):
    post = Post.objects.get(slug=slug)
    if post is None:
        return HttpResponse('Post not found', status=404)
    return render(request, 'posts/post_page.html', {'post': post})

@login_required(login_url='/users/login')
def post_new(request):
    if request.method == 'POST':
        form = CreateForm(request.POST, request.FILES)
        if form.is_valid():
            # Save with user
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('posts:list')
    else:
        form = CreateForm()
    return render(request, 'posts/post_new.html', {'form': form})

