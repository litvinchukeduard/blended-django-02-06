from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout

from users.forms import LoginForm

def loginuser(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
        return redirect('trip_app:main')
    return render(request, 'login.html', context={"form": LoginForm()})

def logoutuser(request):
    logout(request)
    return redirect('trip_app:main')