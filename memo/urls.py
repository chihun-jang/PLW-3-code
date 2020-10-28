from django.urls import path
from .views import index,second
urlpatterns = [
    path('second/', second, name="second"),  #memo/라고 요청이 들어오면 여기 urls.py로 오게되고 memo/second요청이 오면 얘가 실행됩니다.
]

