from django.shortcuts import render,redirect
# render와 redirect의 차이는 render는 말그래도 해당 'template'을 가지고
# rendering 해준다는 의미인데, redirect는 해당 url요청을 다시 보내준다는 의미이다.
# 따라서 상세히 말하자면 redirect는 context를 전달해 줄수 없다.
from .models import Memo
from .forms import MemoForm,BaboForm


# Create your views here.
def index(request):
    context = dict()
    # print(request.POST.get('mydata'),"@"*50)
    request.POST.get('mydata')
    all_memo = Memo.objects.all()
    context['all_memo'] = all_memo
    return render(request, 'index.html',context)

def second(request):
    
    return render(request, 'second.html')


def create(request):
    context=dict() 
    context['memoform'] = MemoForm() #우리가 준비한 빈 modelform을 생성해서 memoform이란 이름으로 넘깁니다.
    if request.method =="POST": #사용자의 요청이 POST라는 것은 글쓰고 제출을 눌렀다는 의미
        myform = MemoForm(request.POST,request.FILES) #사용자가 제출한 POST data와 FIELS data를 받아서 modelform안에 넣어주고
        if myform.is_valid(): #유효성 검사를 거칩니다
            myform.save()     #유효성검사를 통과했으면 save해주고
            return redirect('index') #index페이지로 보내줍니다.
        else: # 만약 유효성 검사를 실패했으면
            context['memoform']= myform # 유효성 검사 실패한 modelform을 memoform에다가 덮어써서 사용자가 재작성할수있게합니다.
        
        # print(request.POST.get('title'))
        
        # create는 model 객체(여기서는 메모글) 의 생성과 저장이 동시에 이루어지고
        # Memo.objects.create(title=request.POST.get('title'),
        #                     desc=request.POST.get('desc'),
        #                     pic =request.POST.get('pic'))

        # 이경우는 해당 요소들을 받아서 생성해주고 save는 따로하는 모습을 볼수 있습니다.
        # new_memo=Memo(title=request.POST.get('title'),
        #                 desc=request.POST.get('desc'),
        #                 pic =request.POST.get('pic'))
        # new_memo.save()
        
    return render(request,'create.html',context) #얘는 사용자가 GET요청을 했을때 혹은 유효성 검사를 실패했을때 실행됩니다.


def new(request):
    context={}
    context['baboform'] = BaboForm()

    if request.method=="POST":
        tempform = BaboForm(request.POST, request.FILES)
        if tempform.is_valid():
            tempform.save()
            return redirect('index')
        else:
            context['baboform'] = tempform

    return render(request,'new.html',context)

def detail(request,detail_id):#우리가 url에서 설정한 path converter의 이름을 가져와서 사용합니다.
    context={}
    one_memo = Memo.objects.get(id=detail_id) #예를 들면 5번 id 글을 가져오겠다입니다.

    context['one_memo'] = one_memo

    return render(request, 'detail.html',context)

def update(request,update_id): #글의 수정이라는 것은 특정한 글(id값 필요)을 수정(create와 유사)하는 것입니다.
    context={}
    context['baboform'] = BaboForm(instance=Memo.objects.get(id=update_id))
                            #기존에 빈 modelform을 가져오던것을 글의 수정에서는
                            #특별한 글의 id인 update_id와 같은 글을 들고와서 modelform에 넣어서 생성해줍니다.
                            
    if request.method=="POST":
        tempform = BaboForm(request.POST, request.FILES, instance=Memo.objects.get(id=update_id))
                    #사용자가 입력한 data값을 가져와서 modelform에 넣어서 저장해줄 준비를 합니다.
                    # 그런데 이때 새로운 글을 작성하는 것이아니라, 기존에 작성해 놓았던 modelform을 들고와서 그 위에 사용자들이 보내준 Data를 덮어서 작성해줍니다.

        if tempform.is_valid(): #아래는 create와 같이 진행됩니다.
            tempform.save()
            return redirect('detail',update_id)

        else:
            context['baboform'] = tempform

    return render(request,'new.html',context)

def delete(request, delete_id):
    one_memo = Memo.objects.get(id=delete_id) #특정한 객체를 가져오고
    one_memo.delete() #해당 객체를 delete()메서드를 이용해서 삭제해줍니다.
    return redirect('index')