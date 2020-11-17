from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm #유저생성 모델폼을 장고가 제공해주므로 가져와서 사용합니다.
from django.contrib.auth import authenticate, login #해당 사용자의 권한을 체크하고 로그인을 할수있는 함수입니다.

# Create your views here.


# signup은 제공해주는 view가 없기에 UserCreationForm을 사용해서 CRUD의 C와 유사하게 구현해줍니다.
def signup(request):
    context=dict()
    if request.method =="POST": #사용자의 회원가입은 request method로 POST를 사용할 것이므로
        save_form = UserCreationForm(request.POST) #장고가 제공해주는 CreationForm에 사용자가 제출한 POST Data를 넣어서
        if save_form.is_valid(): #유효성 검사를 하고 
            save_form.save() #유저를 생성해준다.

            user = authenticate(username = save_form.cleaned_data['username'],
                                password = save_form.cleaned_data['password1'])
            # 그리고 유효성 검사가 끝난 cleand_data에서 username과 pw를 들고와서 인증받은 사용자인지 검사한다.
            login(request, user) #그리고 login함수를 통해서 로그인을 시켜준다.


            return redirect('index') #성공하면 메인페이지로 다시 돌려보내주고

        else: #사용자가 입력한 정보가 유효성 검사에서 탈락한 경우

            context['userForm'] = save_form #사용자가 입력한 데이터와 실패한 이유가 담긴 form을 userForm에 덮어쓴다
            #그리고 이를 전해주면 사용자는 내용의 보존과 함께 에러의 이유를 알수 있어서 좋다.
            return render(request, 'registration/signup.html',context)

    context['userForm'] = UserCreationForm()
    #POST method로 요청되지 않는 경우인데 빈 UserCreationForm()을 만들어서 userForm으로 넘겨준다음 회원가입을 할수 있게 한다.

    return render(request, 'registration/signup.html',context)