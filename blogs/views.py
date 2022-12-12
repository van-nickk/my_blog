from django.shortcuts import render, redirect
from .models import BlogPost
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.http import Http404


@login_required
def posts(request):
    posts = BlogPost.objects.filter(owner=request.user).order_by('-date_added')
    context = {'posts': posts}
    return render(request, 'blogs/posts.html', context)


@login_required
def new_post(request):
    #post = BlogPost.objects.get(id=post_id)
    if request.method != 'POST':
# Данные не отправлялись; создается пустая форма.
        form = PostForm()
    else:
# Отправлены данные POST; обработать данные.
        form = PostForm(data=request.POST)
        if form.is_valid():
            #new_post = form.save(commit=False)
            #new_post.post = post
            new_post = form.save(commit=False)
            new_post.owner = request.user
            new_post.save()
            #form.save()
            return redirect('blogs:posts')

# Вывести пустую или недействительную форму.
    context = {'form': form}
    return render(request, 'blogs/new_post.html', context)



@login_required
def edit_post(request, post_id):
    post = BlogPost.objects.get(id=post_id)
    if request.method != 'POST':
# Данные не отправлялись; создается пустая форма.
        form = PostForm(instance=post)
    else:
# Отправлены данные POST; обработать данные.
        form = PostForm(instance=post, data=request.POST)
        if form.is_valid():
            #new_post = form.save(commit=False)
            #new_post.post = post
            form.save()
            return redirect('blogs:posts')

# Вывести пустую или недействительную форму.
    context = {'post':post, 'form': form}
    return render(request, 'blogs/edit_post.html', context)

@login_required
def delete_post(request,post_id=None):
    post_to_delete=BlogPost.objects.get(id=post_id)
    post_to_delete.delete()
    return redirect('blogs:posts')



