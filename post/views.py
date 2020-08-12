from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .models import Blog

#.은 현재 디렉토리, 폴더

def read_blog_list(request):
    blogs = Blog.objects.all()
    return render(request,'post/blog_list.html',{'blogs':blogs} ) #dictionary 문법

def read_blog_detail(request, blog_id):
    blog = get_object_or_404(Blog, pk = blog_id)
    return render(request,'post/blog_detail.html', {'blog':blog} )
    #urls에서 받아온 blog_id를 통해서 객체가 있는지 get_object 메소드로 가져오고 그 가져온 객체(글)을 디테일html에 render한다.

def blog_new(request):
    return render(request,'post/blog_new.html')

def create_blog(request):
    blog = Blog()
    blog.title = request.POST['title']
    blog.body = request.POST['body']
    blog.pub_date = timezone.datetime.now()
    #작가추가
    blog.author = request.POST['author']
    blog.save()  #db에 저장해달라는 query method 중 하나. 즉, models.py가 db에게 명령하는 것.
    return redirect('read_blog_list')

