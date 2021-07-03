from django.db import models

# 여기에 Post 모델을 정의하고, admin.py에 코드를 추가하면 된다.


class Post(models.Model):
    title = models.CharField(max_length=30)  # 이거는 문자 담는 필드
    content = models.TextField()  # 길이 제한이 없도록 TextField 만들었고,

    # 처음 레코드 생성될떄 현지 시각이 자동으로 저장되게 하는게 auto_now_add
    created_at = models.DateTimeField(auto_now_add=True)
    # auto_now 는 설정해서 다시 저장될때 그 시각 저장.
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        # 이게 지금 해당 포스트 pK값이랑, 해당 포스트의 title 값임. 원래 장고 모델 만들면 자동으로 pk값이 주어지거든?
        return f'[{self.pk}]{self.title}'
        # 처음 생성하면 pk1 주어지는거고, 그 다음은 2고 이런거임, 그래서 이렇게하면 포스트 번호랑, 포스트 제목이랑 나오게 된다.

    def get_absolute_url(self):
        # 여기서 잘 이해안가는데, 일단 이게 get_absoulte_url()함수를 만드는 과정임.
        # 이렇게 하면, 리턴 주면서 저기 blog/1/ 이나 blog/2/ 로 들어갈 수 있다.
        return f'/blog/{self.pk}/'
