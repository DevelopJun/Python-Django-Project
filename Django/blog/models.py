from django.db import models
from django.contrib.auth.models import User
import os

# 여기에 Post 모델을 정의하고, admin.py에 코드를 추가하면 된다.


class Category(models.Model):
    # unique=True로 만들면 동일한 name을 갖는 카테고리를 또 만들 수 없음.
    name = models.CharField(max_length=50, unique=True)
    # slug 필드를 만들때 사용한 SlugField는 사람이 읽을 수 있는 텍스트로 고유 URL을 만들고 싶을때 사용함.
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)
    # 원래 slugField 한글 지원 안하는데, allow_unicode=True로 설정해 한글로도 만들 수 있는거임.

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'


class Post(models.Model):
    title = models.CharField(max_length=30)  # 이거는 문자 담는 필드,
    content = models.TextField()  # 길이 제한이 없도록 TextField 만들었고,

    # 이거 지금 후크 텍스트로 그 워싱턴 포스트 같은 웹 사이트가 제목 아래에 드는 소제목
    hook_text = models.CharField(max_length=100, blank=True)

    # blank=True라고 하는 이유가, 이 필드가 필수 필드가 아니란거지, blank=True라고 안하면 왜 안채웠냐고 뭐라하거든,
    head_image = models.ImageField(
        upload_to='blog/images/%Y/%m/%d/', blank=True)
    # 이제 이미지를 저장할 경로를 model에서 구현 하는 부분임. 연도 폴더, 월 폴더, 일 폴더까지 내려간 위치
    # 근데 이게 빨라서 하는거지, 연도, 시간 이렇게 폴더 플로우는 비교적 빠른데, 한 폴더에 다 넣으면 찾는데 서버가 너무 힘들어 하거든,

    file_upload = models.FileField(
        upload_to='blog/files/%Y/%m/%d/', blank=True)  # 이거 이제 파일 필드임. # 파일도 올릴 수 있도록 모델 만든거지
    # 처음 레코드 생성될떄 현지 시각이 자동으로 저장되게 하는게 auto_now_add
    created_at = models.DateTimeField(auto_now_add=True)
    # auto_now 는 설정해서 다시 저장될때 그 시각 저장.
    updated_at = models.DateTimeField(auto_now=True)

    # 이 포스트의 작성자가 데이터베이스에서 삭제 되었을 떄 이 포스트도 같이 삭제한다.
    # author = models.ForeignKey(User, on_delete=models.CASCADE)
    # 이 포스트의 작성자가 데이터 베이스에서 삭제되었을때 작성자명을 빈칸으로 둔다는 말임.
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    # 여기 author은 User 라는 원래 제공되는 class 사용한거고,
    category = models.ForeignKey(
        Category, null=True, blank=True, on_delete=models.SET_NULL)
    # 여기 카테고리는 위에 우리가 class 직접 만들었잖슴.

    def __str__(self):
        # 이게 지금 해당 포스트 pK값이랑, 해당 포스트의 title 값임. 원래 장고 모델 만들면 자동으로 pk값이 주어지거든?
        return f'[{self.pk}]{self.title} :: {self.author}'
        # 처음 생성하면 pk1 주어지는거고, 그 다음은 2고 이런거임, 그래서 이렇게하면 포스트 번호랑, 포스트 제목이랑 나오게 된다.

    def get_absolute_url(self):
        # 여기서 잘 이해안가는데, 일단 이게 get_absoulte_url()함수를 만드는 과정임.
        # 이렇게 하면, 리턴 주면서 저기 blog/1/ 이나 blog/2/ 로 들어갈 수 있다.
        return f'/blog/{self.pk}/'

    # 이 부분이 파일 이름 downloat해서 보여질 수 있도록 설계하는 부분

    def get_file_name(self):
        return os.path.basename(self.file_upload.name)

    def get_file_ext(self):
        return self.get_file_name().split('.')[-1]
