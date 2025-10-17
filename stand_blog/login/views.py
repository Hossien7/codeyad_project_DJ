from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm
from django.contrib.auth.models import User


def user_login(request):
    if request.user.is_authenticated == True:
        return redirect('/')
    if request.method == "POST":
    #     username = request.POST['username']
    #     password = request.POST['password']
    #     user = authenticate(request, username=username, password=password)
        
    #     if user is not None:
    #         login(request, user)
    #         return redirect('/')
    # return render(request, 'login/index.html', {})
        form = LoginForm(request.POST)
        if form.is_valid():
            user = User.objects.get(username=form.cleaned_data.get('username'))
            login(request, user)
            return redirect('/')
        # return render(request, 'login/index.html', {'form': form})
    else:
        form = LoginForm()
    return render(request, 'login/index.html', {'form': form})
    
def user_register(request): # user.object.create()
    pass

def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('/')
    else:
        return render('home/index.html', {})
