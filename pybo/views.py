from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils.datastructures import MultiValueDictKeyError


def login(request):
    user_data = {
        'username': 'python',
        'password': 'django'
    }

    context = {
        'method': request.method,
        'is_valid': True
    }

    if (request.method =='GET') :
        return render(request, 'pybo/login.html', context)

    if (request.method=='POST'):
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username =='':
            context['is_valid'] = False
        if password =='':
            context['is_valid'] = False

        if (username != user_data['username']):
            context['is_valid'] = False

        if (password != user_data['password']):
            context['is_valid'] = False

        if context['is_valid'] :
            response = redirect('pages:index')
            response.set_cookie('is_login', True)
            response.set_cookie('username', user_data['username'])
            response.set_cookie('password', user_data['password'])

            return response
        return render(request, 'pybo/login.html', context)

def login_detail(request, id):
    return HttpResponse('user id 는' + str(id) + '입니다.')

def index(request) :
    return render(request,'index.html')