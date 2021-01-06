from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'authentication/signup.html', {'form': form})

def log_in(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(request, 
                username=form.cleaned_data.get('username'),
                password=form.cleaned_data.get('password')
            )
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                return render(request, 'authentication/login.html', {'form':form})
        else:
            return render(request, 'authentication/login.html', {'form':form})
    else:
        return render(request, 'authentication/login.html', {'form':LoginForm()})

def log_out(request):
    if request.user.is_authenticated:
        goto = ''
        try:
            goto = request.META.get('HTTP_REFERER').split('/')[4]
        except:
            pass
        logout(request)
        if goto == '':
            return redirect(f'../')
        return redirect(f'../{goto}')
    else:
        return redirect('/')