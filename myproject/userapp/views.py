from django.shortcuts import render, redirect
from .models import User
from mainapp.models import Warehouse
from .forms import UserForm, UserLoginForm, UserAuthForm, UserTelephoneForm, UserActivityForm, UserPhotoForm
from django.contrib import sessions
from django.core.files.storage import FileSystemStorage
import os


def my_information(request):
    """Информация о пользователе"""
    name_user = request.session.get('name_user', '')
    if name_user == '':
        return render(request, 'mainapp/index.html')
    else:
        user = User.objects.filter(name=name_user).first()
        return render(request, 'userapp/my_information.html', {'user': user, 'name_user': name_user})


def add_user(request):
    """Создание учётной записи"""
    if request.method == 'POST':
        form = UserForm(request.POST)
        message = 'Ошибка в данных'
        if form.is_valid() and request.POST['password'] == request.POST['repeat_password']:
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User(name=name, email=email, password=password)
            user.save()
            message = 'Пользователь сохранён, теперь можете авторизоваться и разместить объявление'
            return render(request, 'userapp/user_index.html', {'message': message})
    else:
        form = UserForm()
        message = 'Заполните форму'
    return render(request, 'userapp/user_form.html', {'form': form, 'message': message})


def login_user(request):
    """Авторизация"""
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        user = User.objects.filter(email=request.POST['email'], password=request.POST['password']).first()
        message = 'Ошибка в данных, неверно введены: адрес электронной почты или пароль'
        if user is not None and user.is_active is True:
            request.session['name_user'] = user.name
            name_user = request.session['name_user']
            message = 'Вы вошли в систему'
            return render(request, 'userapp/user_index.html', {'name_user': name_user, 'message': message})
    else:
        form = UserLoginForm()
        message = 'Введите адрес электронной почты и пароль для авторизации'
    return render(request, 'userapp/user_form.html', {'form': form, 'message': message})


def logout_user(request):
    """Выход из учётной записи"""
    del request.session['name_user']
    message = 'Вы вышли из учётной записи'
    return render(request, 'userapp/user_index.html', {'message': message})


def delete_user(request):
    """Удаление учётной записи"""
    name_user = request.session.get('name_user', '')
    if name_user == '':
        return render(request, 'mainapp/index.html')
    if request.method == 'POST':
        form = UserAuthForm(request.POST)
        message = 'Неверно введён пароль'
        user = User.objects.filter(name=name_user).first()
        if user.password == request.POST['password']:
            warehouses = Warehouse.objects.filter(user_id=user.pk).all()
            for warehouse in warehouses:
                os.remove(f'media/{warehouse.image}')
                warehouse.delete()
            os.remove(f'media/{user.my_photo}')
            user.delete()
            del request.session['name_user']
            message = 'Запись удалена'
            return render(request, 'userapp/user_index.html', {'message': message, 'name_user': name_user})
    else:
        form = UserAuthForm()
        message = 'Введите пароль для подтверждения удаления учётной записи в системе'
    return render(request, 'userapp/user_form.html', {'form': form, 'message': message, 'name_user': name_user})


def add_telephone(request):
    """Добавить номер телефона"""
    name_user = request.session.get('name_user', '')
    if name_user == '':
        return render(request, 'mainapp/index.html')
    if request.method == 'POST':
        form = UserTelephoneForm(request.POST)
        message = 'Ошибка в данных'
        if form.is_valid() and request.POST['telephone_number'] is not None:
            telephone_number = form.cleaned_data['telephone_number']
            user = User.objects.filter(name=name_user).first()
            user.telephone_number = telephone_number
            user.save()
            message = 'Контактный номер добавлен'
            return render(request, 'userapp/user_index.html', {'message': message, 'name_user': name_user})
    else:
        form = UserTelephoneForm()
        message = 'Заполните форму'
    return render(request, 'userapp/user_form.html', {'form': form, 'message': message, 'name_user': name_user})


def activity(request):
    """Описание деятельности"""
    name_user = request.session.get('name_user', '')
    if name_user == '':
        return render(request, 'mainapp/index.html')
    if request.method == 'POST':
        form = UserActivityForm(request.POST)
        message = 'Ошибка в данных'
        if form.is_valid() and request.POST['my_activity'] is not None:
            my_activity = form.cleaned_data['my_activity']
            user = User.objects.filter(name=name_user).first()
            user.my_activity = my_activity
            user.save()
            message = 'Описание деятельности добавлено'
            return render(request, 'userapp/user_index.html', {'message': message, 'name_user': name_user})
    else:
        form = UserActivityForm()
        message = 'Заполните форму'
    return render(request, 'userapp/user_form.html', {'form': form, 'message': message, 'name_user': name_user})


def photo(request):
    """Добавить фото"""
    name_user = request.session.get('name_user', '')
    if name_user == '':
        return render(request, 'mainapp/index.html')
    if request.method == 'POST':
        form = UserPhotoForm(request.POST, request.FILES)
        message = 'Ошибка в данных'
        if form.is_valid():
            my_photo = form.cleaned_data['my_photo']
            user = User.objects.filter(name=name_user).first()
            if user.my_photo is not None:
                os.remove(f'media/{user.my_photo}')
            user.my_photo = my_photo
            user.save()
            FileSystemStorage()
            message = 'Фото добавлено'
            return render(request, 'userapp/user_index.html', {'message': message, 'name_user': name_user})
    else:
        form = UserPhotoForm()
        message = 'Заполните форму'
    return render(request, 'userapp/user_form.html', {'form': form, 'message': message, 'name_user': name_user})
