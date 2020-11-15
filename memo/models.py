from django.db import models

# Create your models here.

class Memo(models.Model):
    title = models.CharField('제목',max_length=200)
    desc = models.TextField('본문',blank=True)
    pic = models.ImageField('사진', blank=True)
    created_at = models.DateTimeField('생성날짜', auto_now_add=True) #생성될때 픽스됨
    modified_at = models.DateTimeField('수정날짜', auto_now=True)#수정할때마다 바뀜

    def __str__(self):
        return self.title

class Comment(models.Model):
    memo = models.ForeignKey('Memo',on_delete=models.CASCADE) #on_delete 옵션은 참조대상이 삭제되었을때 어떻게 처리해줄지를 결정하는 옵션
    #ForeignKey : 참조하는 대상값을 의미하는데 여기서는 글을 의미합니다
    #PrimaryKey : 우리가 어떤 대상을 식별할수있는 고유한 key값
    desc = models.CharField('댓글내용', max_length = 100)
    created_at = models.DateTimeField('생성날짜', auto_now_add=True) #생성될때 픽스됨

    def __str__(self):
        return self.desc

# 추가로 더 찾아보면 좋을 키워드
    #related_name속성을 주시면 _set을 다른이름으로 사용할수 있습니다.
    #ManyToManyField (~관련 Django 좋아요 기능 )

