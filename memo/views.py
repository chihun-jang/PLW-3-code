from django.shortcuts import render
from .models import Memo

# Create your views here.
def index(request):
    context = dict()
    # print(request.POST.get('mydata'),"@"*50)
    all_memo = Memo.objects.all()
    context['all_memo'] = all_memo
    return render(request, 'index.html',context)

def second(request):
    
    return render(request, 'second.html')