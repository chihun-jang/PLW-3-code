from django.urls import path
from .views import index,second,create
urlpatterns = [
    path('second/', second, name="second"),  #memo/라고 요청이 들어오면 여기 urls.py로 오게되고 memo/second요청이 오면 얘가 실행됩니다.
    path('create/', create, name="create"), #create는 Memo와 관련된 기능이므로 Memo 앱 안에서 관리해주겠습니다.
]

