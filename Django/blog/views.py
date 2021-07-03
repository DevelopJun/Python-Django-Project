from django.shortcuts import render
from .models import Post


def index(request):
    # 이런 방식으로 views.py에서 데이터베이스에 쿼리를 날려서 원하는 레코드를 가져올 수 있다.
    posts = Post.objects.all().order_by('-pk')
    # 여기서 쿼리는 데이터 베이스 데이터를 가져오거나 수정, 삭제하는 등의 행위를 하기 위한 요청입니다. 쿼리 명령어는 all()외에도
    # filter(), order_by(), create(), delete() 등으로 다양하다. 이 명령어들은 뒤에서 배운다.

    return render(  # 장고가 기본적으로 제공하는 render함수로서, 템플릿 폴더에서, blog 폴더의 index.html을 찾아서 방문자한테 보여준다.
        request,
        'blog/index.html',
        {
            'posts': posts,  # 지금 이걸로 posts 를 index html에 뿌려주고 있음.
        }
    )
