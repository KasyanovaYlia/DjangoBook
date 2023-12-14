from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django import forms
from users.models import User
from django.forms import TextInput, EmailInput, PasswordInput, FileInput, CharField

class UserLoginForm (AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']

        widgets = {
            "username": TextInput(attrs={
                'id': 'username',
                'placeholder': 'Введите почту'
            }), "password": TextInput(attrs={
                'id': 'password',
                'placeholder': 'Введите пароль'
            }),
        }


class UserRegistrationForm (UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

        widgets = {
            "first_name": TextInput(attrs={
                'id': 'first_name',
                'placeholder': 'Введите имя'
            }), "last_name": TextInput(attrs={
                'id': 'first_name',
                'placeholder': 'Введите фамилию'
            }), "username": TextInput(attrs={
                'id': 'username',
                'placeholder': 'Введите имя пользователя'
            }), "email": EmailInput(attrs={
                'id': 'email',
                'placeholder': 'Введите эл. почту'
            }), "password1": PasswordInput(attrs={
                'id': 'password1',
                'placeholder': 'Введите пароль'
            }), "password2": PasswordInput(attrs={
                'id': 'password2',
                'placeholder': 'Подтвердите пароль'
            }),
        }


class UserProfileForm(UserChangeForm):
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'custom-file-input'}), required=False)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'image', 'username', 'email']

        widgets = {
            "first_name": TextInput(attrs={
                'class': 'form-control py-4'
            }), "last_name": TextInput(attrs={
                'class': 'form-control py-4'
            }), "username": EmailInput(attrs={
                'class': 'form-control py-4',
                'readonly': True
            }), "email": PasswordInput(attrs={
                'class': 'form-control py-4',
                'readonly': True})
        }
