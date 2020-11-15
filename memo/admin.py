from django.contrib import admin
from .models import Memo,Comment
# Register your models here.
admin.site.register([Memo,Comment]) #Comment 도 등록하기 위해서 list안에 Memo와 같이 넣어줬습니다.