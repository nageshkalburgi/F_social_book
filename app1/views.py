# users/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser
from .forms import CustomUserCreationForm
from django.contrib.auth import login
from django.contrib.auth import logout as auth_logout
from django.contrib import messages
from .forms import UploadFileForm
from .models import UploadedFile
from django.contrib.auth.decorators import login_required



def dashboard(request):
    return render(request, 'dashboard.html')


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            print(user)
            login(request) 
            return redirect('login') 
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            print(user)
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})



def custom_logout(request):
    auth_logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('dashboard')


def password_reset(request):
    return render(request,'password_reset.html')



def authors_and_sellers(request):
    users = CustomUser.objects.filter(public_visibility=True)
    return render(request, 'authors_and_sellers.html', {'users': users})



@login_required
def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = form.save(commit=False)
            uploaded_file.user = request.user
            uploaded_file.save()
            return redirect('uploaded_files')
    else:
        form = UploadFileForm()
    return render(request, 'upload_file.html', {'form': form})

@login_required
def uploaded_files(request):
    files = UploadedFile.objects.filter(user=request.user)
    return render(request, 'uploaded_files.html', {'files': files})


