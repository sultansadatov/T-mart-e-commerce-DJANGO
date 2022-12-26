from django.http.response import HttpResponse
from django.shortcuts import render
from blog.models import *
from blog.services.blog import get_blog


# Create your views here.

def blog(request, blog_id):
    blogs = get_blog(blog_id)

    context = {
        'blogs': blogs
    }
    return render(request, "blog/blog-details.html", context=context)


def bloglist(request):
    blogs = Blog.objects.all()[:3]
    

    count = 3
    if request.method == 'POST':
        # form = LoadMoreForm(request.POST)# form = LoadMoreForm(request.POST)
        more = int(request.POST['more-blog'])
        blogs = Blog.objects.all()[:more+2]  
        count = len(blogs)

    

    context = {
        'blogs': blogs,
        'count': count,
        # 'form ' : form
    }


    return render(request, "blog/blog.html", context=context)

  

