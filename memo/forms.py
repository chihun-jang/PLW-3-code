from django.forms import ModelForm #Django의 modelform을 쓰기 위해서 import 해주었다.
from .models import Memo,Comment #Modelform을 만들 재료인 Model도 가져온다.



class MemoForm(ModelForm):

    class Meta:
        model = Memo  #ModelForm의 대상 Model을 지정해줍니다.
        fields = ("title","desc",'pic') # Modelform에서 보여줄 field를 명시적으로 보여주고
        # fields = "__all__" #전체인경우에는 __all__로 대체할수있지만 명시적으로 다 적어주는 것도 좋습니다.


class BaboForm(ModelForm):

    class Meta:
        model = Memo
        fields = ('title','desc','pic',)

class CommentForm(ModelForm):   #사용자로 부터 댓글 입력을 받아야 하므로 Model Form을 준비해줍니다.

    class Meta:
        model = Comment
        fields = ('desc',) #댓글은 사용자로부터 받아야할 field가 desc부분 밖에 없습니다. 