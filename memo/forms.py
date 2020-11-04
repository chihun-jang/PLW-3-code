from django.forms import ModelForm #Django의 modelform을 쓰기 위해서 import 해주었다.
from .models import Memo #Modelform을 만들 재료인 Model도 가져온다.



class MemoForm(ModelForm):

    class Meta:
        model = Memo  #ModelForm의 대상 Model을 지정해줍니다.
        fields = ("title","desc",'pic') # Modelform에서 보여줄 field를 명시적으로 보여주고
        # fields = "__all__" #전체인경우에는 __all__로 대체할수있지만 명시적으로 다 적어주는 것도 좋습니다.


class BaboForm(ModelForm):

    class Meta:
        model = Memo
        fields = ('title','desc','pic',)