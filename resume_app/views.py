
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import ResumeForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

@login_required
def upload_resume(request):
    if request.method == 'POST':
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            user_profile = form.save(commit=False)
            user_profile.user = request.user
            user_profile.save()
            return redirect('profile')
    else:
        form = ResumeForm()
    return render(request, 'upload_resume.html', {'form': form})

@login_required
def view_profile(request):
    return render(request, 'view_profile.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('upload_resume')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form=AuthenticationForm(request,data=request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request,'Successfull login')
            return redirect('upload_resume')
        else:
            messages.error(request,'Invalid credentials')
            return redirect('login')
    form=AuthenticationForm()
    return render(request, 'login.html',{'form':form})

def user_logout(request):
    logout(request)
    return redirect('login')