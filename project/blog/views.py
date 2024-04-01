from django.shortcuts import render,redirect
from django.http import HttpResponse

from .models import Post, Category
from .forms import PostForm
from .forms import CategoryForm

# Create your views here.



def all_posts(request):
    posts = Post.objects.all()
    categories = Category.objects.all()
    context = {
        'posts': posts,
        'categories': categories,
        'title': "Barcha maqolalar"
    }
    return render(request, 'blog/index.html', context=context)


def posts_by_category(request, category_id):
    posts = Post.objects.filter(category_id=category_id)
    categories = Category.objects.all()
    category = Category.objects.get(pk=category_id)
    context = {
        'posts': posts,
        'categories': categories,
        'title': f"{category.title} ga tegishli maqolalar"
    }
    return render(request, 'blog/index.html', context=context)

def post_detail(request,pk):
    post = Post.objects.get(pk=pk)
    context = {
        'post':post
    }
    return render(request,'blog/detail.html',context)

def category_detail(request,pk):
    category = Category.objects.get(pk=pk)
    context = {
        'category':category
    }
    return render(request,'blog/detail.html',context)


def post_created(request):

    form = PostForm(data=request.POST)
    if form.is_valid():
        form.save()

    form = PostForm()
    context = {
        'form':form
    }
    return render(request,'blog/post_form.html',context)
def category_created(request):
    form = CategoryForm(data=request.POST)
    if form.is_valid():
        form.save()

    form = CategoryForm()
    context = {
        'form':form
    }
    return render(request,'blog/post_form.html',context)

def post_update(request,pk):
    post = Post.objects.get(pk=pk)
    form = PostForm(data=request.POST or None,instance=post)

    if form.is_valid():
        form.save()
        return redirect('detail',pk=pk)
    context = {
        'form': form
    }
    return render(request,'blog/post_form.html',context)


def category_ubdate(request,pk):
        category = Category.objects.get(pk=pk)
        form = CategoryForm(data=request.POST or None,instance=category)
        if form.is_valid():
            form.save()
            return redirect('index')
        context = {
            'form':form
        }
        return render(request,'blog/post_form.html',context)
def post_delate(request,pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('index')
    context = {
        'post':post
    }
    return render(request,'blog/post_delete.html',context)

def category_delete(request,pk):
    category = Category.objects.get(pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('index')
    context = {
        'category':category
    }
    return render(request,'blog/category_delete.html',context)

