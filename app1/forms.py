# users/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from .models import UploadedFile

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'public_visibility', 'birth_year', 'address', 'password1', 'password2']

# from django.contrib.auth.forms import AuthenticationForm
# from .models import CustomUser
# from django import forms

# class CustomAuthenticationForm(AuthenticationForm):
#     username = forms.CharField(max_length=254, widget=forms.TextInput(attrs={'autofocus': True}))
#     password = forms.CharField(label=("Password"), strip=False, widget=forms.PasswordInput)

#     class Meta:
#         model = CustomUser
#         fields = ['username', 'password']


class UploadFileForm(forms.ModelForm):
    class Meta:
        model = UploadedFile
        fields = ['title', 'description', 'visibility', 'cost', 'year_of_publication', 'file']


