from .models import Post
from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here


def post_list(request):
    posts = Post.objects.all()  # 정확히는 여기가 Retrieve(Read)
    ctx = {'posts': posts}

    return render(request, template_name='posts/list.html', context=ctx)
