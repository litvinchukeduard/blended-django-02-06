from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout

from users.forms import LoginForm, UserCreationForm, RegisterForm

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
        print(form.error_messages)
        return redirect('trip_app:main')
    else:
        form = RegisterForm()
        return render(request, 'signup.html', context={'form': form})
    

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