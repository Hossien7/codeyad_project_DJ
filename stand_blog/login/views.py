from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(user)
            return redirect('/')
    return render(request, 'login/index.html', {})
