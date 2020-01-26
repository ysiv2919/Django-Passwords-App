from django.shortcuts import render, redirect
from .models import Info

def index(request):
    if request.user.is_authenticated:
        passwords = Info.objects.filter(user=request.user)
        return render(request, 'path/home.html', {
            'passwords': passwords
        })
    else:
        return render(request, 'path/index.html')

def new_password(request):
    if request.method == 'GET':
        return render(request, 'path/new-password.html')
    elif request.method == 'POST':
        site = request.POST['site']
        password = request.POST['password']
        user = request.user
        Info(site=site, password=password, user=user).save()
        return redirect('/')

def delete_password(request, password):
    Info.objects.filter(pk=password).delete()
    return redirect('/')