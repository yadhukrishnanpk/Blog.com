from django.http import HttpResponse
from django.shortcuts import render,redirect,get_object_or_404
from .models import Blog,Category
from django.db.models import Q

def posts_by_category(request, category_id):

    #fetch the post that belongs to the category with the id category_id
    posts = Blog.objects.filter(status='Published', category=category_id)
    category = Category.objects.get(pk=category_id)
    context={
        'posts': posts,
        'category_id': category,
    }
    return render(request, 'posts_by_category.html', context)

def blogs(request, slug):
    single_blog =get_object_or_404(Blog, slug=slug, status='Published')
    context={
        'single_blog': single_blog
    }
    return render(request, 'blogs.html', context)

def search(request):
    keyword= request.GET.get('keyword')
    blogs= Blog.objects.filter(Q(title__icontains=keyword) | Q(short_discription__icontains=keyword) | Q(blogg_body__icontains=keyword), status='Published'  )
    context= {
        'blogs': blogs,
        'keyword': keyword,

    }
    return render(request, "search.html", context)