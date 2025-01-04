from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

def user_list(request):
    return render(request, 'account/user_list.html', {'Users': User.objects.all()})

def user_login(request):
    if request.user.is_authenticated:
        return redirect('home:index')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user= authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home:index')
        else:
            return HttpResponse('<h1>the username is not exist</h1>')
    return render(request, 'account/login.html')

def user_logout(request):
    logout(request)
    return redirect('home:index')

def user_register(request):
    if request.user.is_authenticated:
        return redirect('home:index')

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        fullname= request.POST.get('fullname')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            return HttpResponse('<h1>passwords do not match</h1>')
        if User.objects.filter(username=username).exists():
            return HttpResponse('<h1>username taken</h1>')
        user= User.objects.create_user(username= username, email= email, password= password1, )
        user.first_name = fullname
        user.save()
        login(request, user)
        return redirect('home:index')
    return render(request, 'account/register.html')
