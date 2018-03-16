from django.shortcuts import render, render_to_response, get_object_or_404, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from .models import Post, Comment, User, Categories, BlogType
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.template import RequestContext, loader
from .forms import PostForm, CommentForm, CategoriesForm
from django.contrib import messages


def post_list(request):
    css1 = 'active'
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    paginator = Paginator(posts, 5)
    page = request.GET.get('page')
    user = request.user
    cat_list_side = Categories.objects.all()
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'blog/index.html', locals())


def post_detail(request, pk):
    cat_list_side = Categories.objects.all()
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.approve()
            comment.save()
            return redirect('blog:post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/post_detail.html', locals())


def post_new(request):
    css1 = 'active'
    cat_list_side = Categories.objects.all()
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.publish()
            post.save()
            form.save_m2m()
            return redirect('blog:post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_create.html', locals())

