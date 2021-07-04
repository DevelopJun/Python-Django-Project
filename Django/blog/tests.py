from unittest.main import main
from bs4.element import ContentMetaAttributeValue
from django.http import response
from django.test import TestCase, Client
from bs4 import BeautifulSoup
from .models import Post

# 뷰 측면에서 테스트하겠다는 의미를 TestView
# 지금 TestCase 에서 이용한 테스트 방식은 실제 데이터 베이스 안거드리고 가상의 데이터베이스에서 새로 만들어 테스트함.


class TestView(TestCase):
    def setUp(self):
        # 클라이언트를 사용하겠다는 것만 담았슴. # 장고 테스트에서는 client가 테스트를 위한 가상의 사용자라고 생각하면 된다.
        self.client = Client()

    def test_post_list(self):
        # 1.1 포스트_목록 페이지를 가지고 온다
        # 이거는 이제 8000/blog/입력했다고 가정하면 그 때 웹 페이지 정보 response에 저장
        response = self.client.get('/blog/')
        # 1.2 정상적으로 페이지가 로드 된다.
        # 웹에서느 오류 뜨면 404 돌려주고, 맞으면 200 돌려주거든 그래서 200
        self.assertEqual(response.status_code, 200)
        # 1.3 페이지 타이틀은 'blog'이다.
        # 파싱한 결과를 soup에 담고,
        soup = BeautifulSoup(response.content, 'html.parser')
        # title 요소에서 text만 들고와서 그거 'blog'인지 확인
        self.assertEqual(soup.title.text, 'Blog')
        # 1.4 내비게이션 바가 있다.
        navbar = soup.nav
        # 1.5 Blog, About Me 라는 문구가 내비게이션 바에 있다.
        # 이것도 위에 soup로 들고와서 navbar에, assertIn으로 blog 있는지 확인하는거지
        self.assertIn('Blog', navbar.text)
        self.assertIn('About_me', navbar.text)

        # 2.1 메인 영역에 게시물이 하나도 없다면
        self.assertEqual(Post.objects.count(), 0)
        # 2.2 '아직 게시물이 없습니다'라는 문가가 보인다.
        main_area = soup.find('div', id='main-area')
        self.assertIn('아직 게시물이 없습니다.', main_area.text)

        # 3.1 게시물이 2개 있다면
        post_001 = Post.objects.create(
            title='첫 번째 포스트 입니다.',
            content='Hello World. We are the world',
        )
        post_002 = Post.objects.create(
            title='두 번째 포스트 입니다.',
            content='1등이 전부는 아니잖아요',
        )

        # 3.2 포스트 목록 페이지를 새로고침 했을때
        response = self.client.get('/blog/')
        soup = BeautifulSoup(response.content, 'html.parser')
        self.assertEqual(response.status_code, 200)

        # 3.3 메인 영역에 포스트 2개의 타이틀이 존재한다.
        main_area = soup.find('div', id='main-area')
        self.assertIn(post_001.title, main_area.text)
        self.assertIn(post_002.title, main_area.text)

        # 3.4 '아직 게시물이 없습니다.' 라는 문구는 더 이상 보이지 않는다.
        self.assertNotIn('아직 게시물이 없습니다.', main_area.text)


def test_post_detail(self):  # 함수 처음 만들었으니까 데이터베이스 하나 만든거임
    # 1.1. 포스트가 하나 있따.
    post_001 = Post.objects.create(
        title='첫 번째 포스트 입니다.',
        content="hello world. we are the world",
    )
    # 1.2. 그 포스트의 url은 'blog/1/' 이다
    # 여기서 당연히 처음 post 한개 만들었으니 pk(1)이 된다.
    self.assertEqual(post_001.get_absolute_url(), 'blog/1/')

    # 2. 포스트의 상세 페이지 테스트
    # 2.1. 첫 번째 포스트의 url로 접근하면 정상적으로 작동한다(status : 200 )
    response = self.client.get(post_001.get_absolute_url())
    self.assertEqual(response.status_code, 200)
    # 이게 soup에 이제 담아서, 파싱하여 다루기 편하게 만드는거임.
    soup = BeautifulSoup(response.content, 'html.parser')

    # 2.2. 포스트 목록 페이지와 똑같은 네비게이션 바가 있다.
    navbar = soup.nav
    self.assertIn('Blog', navbar.text)
    self.assertIn('About_me', navbar.text)

    # 2.3. 첫 번째 포스트의 제목이 웹 브라우저 탬 타이틀에 들어 있다.
    self.assertIn(post_001.title, soup.title.text)

    # 2.4. 첫 번째 포스트의 제목이 포스트 영역에 있다.
    main_area = soup.find('div', id='main-area')
    post_area = main_area.find('div', id='post-area')
    self.assertIn(post_001.title, post_area.text)

    # 2.5. 첫 번째 포스트의 작성자(author)가 포스트 영역에 있다(아직 구현할 수 없음.)

    # 2.6. 첫 번째 포스트의 내용(content)이 포스트 영역에 있다.
    self.assertIn(post_001.content, post_area.text)
