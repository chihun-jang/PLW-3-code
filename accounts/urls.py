from django.urls import path 
from .views import signup   #(signup은 함수기반 FBV이다.)
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
   path('signup/',signup,name="signup"),#signup URL 요청이 오면 우리가 view에서 만들어준 signup함수를 실행합니다.
   path('login/',LoginView.as_view(),name="login"), 
   # 이번에는 우리가 만들어준 signup함수가 아니라 Django에서 제공해주는 
   # LoginView와 LogoutView를 사용해보도록 합시다 이는 CBV(클래스 기반뷰의 형태)로 as_view()메서드를 통해서
   # 우리가 원하는 view의 동작을 실행합니다.
   path('logout/',LogoutView.as_view(),name="logout"),
]


# 계정 관련 App을 만들어서 urls.py를 세팅해줬습니다.
# memo앱의 기능과는 명확하게 구분이 되므로 새로운 App을 만들어 주었고
# 각 App별로 url을 따로 관리하기 위해 이처럼 분리를 해주었습니다.