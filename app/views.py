from django.shortcuts import render, redirect
from .models import CustomUser, BoardModel, ReadMember
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.urls import reverse_lazy

def registFunc(request):

    if request.method == 'POST':
        _username = request.POST['username']
        _password = request.POST['password']
        try:
            regUser = CustomUser.objects.create_user(_username, '', _password)
            return render(request, 'list.html', {'user':regUser})
        except:
            return render(request, 'regist.html', {'error': '既に登録済みです'})

    return render(request, 'regist.html')

def loginFunc(request):
    if request.method == 'POST':
        _username = request.POST['username']
        _password = request.POST['password']
        user = authenticate(request, username=_username, password=_password)
        if user is not None:
            login(request, user)
            return redirect('list')
        else:
            return render(request, 'regist.html', {'error': 'ログインに失敗しました。ユーザーを登録してください。'})
    return render(request, 'login.html')

def logoutFunc(request):
    logout(request)
    return redirect('login')

@login_required
def listFunc(request):
    _object_list = BoardModel.objects.all()
    _user = request.user
    return render(request, 'list.html', {'object_list':_object_list, 'user':_user,})

@login_required
def mypageFunc(request):
    if request.method == 'POST':
        req = request.POST
        user_item = CustomUser.objects.get(username=req['befusername'])
        user_item.first_name = req['first_name']
        user_item.last_name = req['last_name']
        user_item.username = req['username']
        user_item.email = req['email']
        user_item.zipnumber = req['zipnumber']
        user_item.address1 = req['address1']
        user_item.address2 = req['address2']
        user_item.save()
        return redirect('list')
    return render(request, 'mypage.html')

def detailFunc(request, pk):
    board_item = BoardModel.objects.get(pk=pk)
    return render(request, 'detail.html', {'board_item':board_item})

def goodFunc(request, pk):
    board_item = BoardModel.objects.get(pk=pk)
    board_item.good = board_item.good + 1
    board_item.save()
    return redirect('list')

def readFunc(request, pk):
    board_item = BoardModel.objects.get(pk=pk)
    read_members = board_item.readmember_set.all()
    if read_members.filter(name=request.user.username).exists():
        pass
    else:
        read_item = ReadMember.objects.create(boardModel=board_item, name=request.user.username)
        read_count = board_item.readmember_set.all().count()
        board_item.read = read_count
        board_item.save()

    return redirect('list')

class BoardCeate(CreateView):
    template_name = 'create.html'
    model = BoardModel
    fields = ('title', 'content', 'author', 'images')
    success_url = reverse_lazy('list')

#    def get_template_names(self):
#        if self.request.user.is_authenticated:
#            template_name = 'create.html'
#        else:
#            template_name = 'login.html'
#        return [template_name]

