from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Blog,Category

def posts_by_category(request, category_id):

    #fetch the post that belongs to the category with the id category_id
    posts = Blog.objects.filter(status='Published', category=category_id)
    category = Category.objects.get(pk=category_id)
    context={
        'posts': posts,
        'category_id': category,
    }
    return render(request, 'posts_by_category.html', context)
