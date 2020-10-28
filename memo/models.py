from django.db import models

# Create your models here.

class Memo(models.Model):
    title = models.CharField('제목',max_length=200)
    desc = models.TextField('본문',blank=True)

    created_at = models.DateTimeField('생성날짜', auto_now_add=True) #생성될때 픽스됨
    modified_at = models.DateTimeField('수정날짜', auto_now=True)#수정할때마다 바뀜

    def __str__(self):
        return self.title