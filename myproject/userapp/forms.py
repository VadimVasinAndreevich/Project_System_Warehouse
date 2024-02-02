import datetime

from django import forms
from .models import User
from django.contrib.auth.forms import PasswordChangeForm


class UserForm(forms.Form):
    name = forms.CharField(label='Имя', min_length=8, max_length=50,
                           widget=forms.TextInput(attrs={'class': 'form-control',
                                                         'placeholder': 'Введите имя пользователя'}))
    email = forms.EmailField(label='Почта',
                             widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'user@mail.ru'}))
    password = forms.CharField(label='Пароль', min_length=8, max_length=50,
                               widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                        'placeholder': 'Введите пароль'}))
    repeat_password = forms.CharField(label='Повтор пароля', min_length=8, max_length=50, widget=forms.PasswordInput(
        attrs={'placeholder': 'Повторите ввод пароля'},))


class UserLoginForm(forms.Form):
    email = forms.EmailField(label='Почта',
                             widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'user@mail.ru'}))
    password = forms.CharField(label='Пароль', min_length=8, max_length=50,
                               widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                        'placeholder': 'Введите пароль'}))


class UserAuthForm(forms.Form):
    password = forms.CharField(label='Пароль', min_length=8, max_length=50,
                               widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                        'placeholder': 'Введите пароль для подтверждения удаления'}))
