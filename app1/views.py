# users/views.py
from django.shortcuts import render, redirect, HttpResponse
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
from django.core.mail import send_mail
from django.conf import settings



def dashboard(request):
    return render(request, 'dashboard.html')


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # print(user)
            login(request) 
            return redirect('login') 
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

# def login(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request, data=request.POST)

#         if form.is_valid():
#             user = form.get_user()
#             auth_login(request, user)
#             print(user)
#             return redirect('dashboard')
#     else:
#         form = AuthenticationForm()
#     return render(request, 'login.html', {'form': form})


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        # form = CustomUserCreationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            user = CustomUser.objects.get(pk=1) 
            email = user.email
            print(email)
           
            send_mail(
                'Login Notification',
                f'Hello {user.username}, you have successfully logged in.',
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=False,
            )
            

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


@login_required
def authors_and_sellers(request):
    users = CustomUser.objects.filter(public_visibility=True)
    return render(request, 'authors_and_sellers.html', {'users': users})


def user_has_uploaded_files(user):
    print('user_has_uploaded_files function executed ')
    return UploadedFile.objects.filter(user=user).exists()  

def check_uploaded_files(view_func):
    @login_required
    def _wrapped_view(request, *args, **kwargs):
        if user_has_uploaded_files(request.user):
            print(user_has_uploaded_files(request.user))
            return view_func(request, *args, **kwargs)
        else:
            return redirect('upload_file')  
    return _wrapped_view


@login_required
# @check_uploaded_files
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
@check_uploaded_files
def uploaded_files(request):
    files = UploadedFile.objects.filter(user=request.user)
    return render(request, 'uploaded_files.html', {'files': files})

def send_test_email(request):
    subject = 'Test Email'
    message = 'This is a test email from Django - [Nagesh Kalburgi].'
    from_email = 'nvsproduction143@gmail.com'  
    recipient_list = ['nageshbkalburgi111@gmail.com']  

    try:
        send_mail(subject, message, from_email, recipient_list)
        return HttpResponse('Email sent successfully!')
    except Exception as e:
        return HttpResponse(f'Error sending email: {e}')
