from .forms import PostForm
from .models import Post
from django.http.response import HttpResponse
from django.shortcuts import render, redirect

# Create your views here


def post_list(request):
    '''
    Retrieve, Read == SELECT
    저장된 모든 포스트를 렌더링하는 뷰
    '''
    posts = Post.objects.all()  # 정확히는 여기가 Retrieve(Read)
    ctx = {'posts': posts}

    return render(request, template_name='posts/list.html', context=ctx)


def post_detail(request, pk):
    '''
    Retrieve, Read == SELECT
    url 파라미터로 가져온 pk값에 해당하는 특정 포스트만을 렌더링하는 뷰
    '''
    # print(pk) # -> url에서 넘겨준 parameter
    post = Post.objects.get(id=pk)  # 정확히는 여기가 Retrieve(Read)
    # print(dir(post)) # -> post의 내부 변수들을 보여준다
    # print(post.id) # -> 해당 post의 id는 (당연히) pk와 같다.
    ctx = {'post': post}

    return render(request, template_name='posts/detail.html', context=ctx)


def create_post(request):
    '''
    Create == INSERT
    모델을 이용하여 새로운 인스턴스를 생성하고 DB에 저장하는 뷰
    '''
    if request.method == 'POST':
        form = PostForm(request.POST)  # 유저가 전송해온 데이터(POST)를 채워넣은 form객체 생성
        if form.is_valid():  # form의 각 필드에 대하여 유효성 검증
            post = form.save()  # DB에 저장
            return redirect('posts:list')
    else:  # 일반적으로 GET방식
        form = PostForm()
        ctx = {'form': form}

        return render(request, 'posts/create.html', ctx)
