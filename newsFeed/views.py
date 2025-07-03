from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import UserRegisterForm, PostForm
from django.contrib import messages

from newsFeed import models
from .models import Post


def main(request):
    posts = models.Post.objects.filter(status="published")

    paginator = Paginator(posts, 3)

    page = request.GET.get('page')

    page_obj = paginator.get_page(page)

    user = request.user

    return render(request, 'main.html', {'posts': page_obj, 'user': user})

def user_posts(request):
    posts = models.Post.objects.filter(author=request.user)

    paginator = Paginator(posts, 3)

    page = request.GET.get('page')

    page_obj = paginator.get_page(page)

    user = request.user

    return render(request, 'user_posts.html', {'posts': page_obj, 'user': user})

@login_required
def add_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()
            messages.success(request, "Post Added")
            return redirect('user_posts')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, error)
    else:
        form = PostForm()
    return render(request, 'add_post.html', {'form': form})

@login_required
def edit_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if request.user != post.author:
        return redirect('main')

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, "Post Updated")
            return redirect('user_posts')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, error)
    else:
        form = PostForm(instance=post)

    return render(request, 'edit_post.html', {'form': form, 'post': post})

def post_details(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    return render(request, "post_detail.html", {'post': post, 'user': request.user})

def delete_post(request, post_id):
    user = request.user
    post = get_object_or_404(Post, pk=post_id)

    if user.id == post.author.id:
        post.delete()
        messages.success(request, "Post Deleted")
    else:
        messages.error(request, "You are not the author")

    return redirect('user_posts')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Аккаунт создан для {user.username}!')
            return redirect('/')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        form = UserRegisterForm()
    return render(request, 'registration/register.html', {'form': form})
