from django.shortcuts import render
from django.http import HttpResponse
from django.utils.datastructures import MultiValueDictKeyError


def login(request):
    user_data = {
        'username': 'python',
        'password': 'django'
    }
    if (request.method =='GET') :
        return render(request, 'pybo/login.html')

    if (request.method=='POST'):
        username= request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        if username =='':
            return HttpResponse('유저 아이디를 입력해주세요.')
        if password =='':
            return HttpResponse('유저 비밀번호를 입력해주세요.')

        if (username != user_data['username']):
            return HttpResponse('유저 아이디가 올바르지 않습니다.')

        if (password != user_data['password']):
            return HttpResponse('유저 비밀번호가 올바르지 않습니다.')

        return render(request, 'pybo/login-success.html')
    return HttpResponse()