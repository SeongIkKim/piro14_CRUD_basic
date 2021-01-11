from .models import Post
from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here


def post_list(request):
    '''
    Retrieve, Read 
    저장된 모든 포스트를 렌더링하는 뷰
    '''
    posts = Post.objects.all()  # 정확히는 여기가 Retrieve(Read)
    ctx = {'posts': posts}

    return render(request, template_name='posts/list.html', context=ctx)


def post_detail(request, pk):
    '''
    Retrieve, Read
    url 파라미터로 가져온 pk값에 해당하는 특정 포스트만을 렌더링하는 뷰
    '''
    # print(pk) # -> url에서 넘겨준 parameter
    post = Post.objects.get(id=pk)  # 정확히는 여기가 Retrieve(Read)
    # print(dir(post)) # -> post의 내부 변수들을 보여준다
    # print(post.id) # -> 해당 post의 id는 (당연히) pk와 같다.
    ctx = {'post': post}

    return render(request, template_name='posts/detail.html', context=ctx)
