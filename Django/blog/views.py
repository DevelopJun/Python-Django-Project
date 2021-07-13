from .models import Post, Category
from django.shortcuts import render
from django.views.generic import ListView, DetailView


class PostList(ListView):  # 이게 지금 list view가 레코드 목록 형태 보여줄때 사용하는거고,
    model = Post
    # 이렇게 안하고, 그냥 저 템플릿 이름 바꿔도 괜찮은데 난 이게 편해서 이름 지정해줌
    template_name = 'blog/index.html'
    ordering = '-pk'  # 이거는 FCV 방식에서 order_by(-pk)랑 똑같은 거임.

    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data()
        # 모든 카테고리를 들고와서 'categories'라는 이름의 키에 연결해 담는거임.
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(
            category=None).count()

        return context


class PostDetail(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data()
        # 모든 카테고리를 들고와서 'categories'라는 이름의 키에 연결해 담는거임.
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(
            category=None).count()

        return context

    template_name = 'blog/single_post_page.html'

# 이거는 FCV 방식이라서  CBV 방식으로 하기 위해서 주석 처리함.
# def index(request):
#     # 이런 방식으로 views.py에서 데이터베이스에 쿼리를 날려서 원하는 레코드를 가져올 수 있다.
#     posts = Post.objects.all().order_by('-pk')
#     # 여기서 쿼리는 데이터 베이스 데이터를 가져오거나 수정, 삭제하는 등의 행위를 하기 위한 요청입니다. 쿼리 명령어는 all()외에도
#     # filter(), order_by(), create(), delete() 등으로 다양하다. 이 명령어들은 뒤에서 배운다.

#     return render(  # 장고가 기본적으로 제공하는 render함수로서, 템플릿 폴더에서, blog 폴더의 index.html을 찾아서 방문자한테 보여준다.
#         request,
#         'blog/index.html',
#         {
#             'posts': posts,  # 지금 이걸로 posts 를 index html에 뿌려주고 있음.
#         }
#     )


# def single_post_page(request, pk):
#     post = Post.objects.get(pk=pk)  # 지금 괄호 안의 조건을 만족하는 Post 레코드를 가져오라는 뜻입니다.

#     return render(
#         request,
#         'blog/single_post_page.html',
#         {
#             'post': post,
#         }
#     )
