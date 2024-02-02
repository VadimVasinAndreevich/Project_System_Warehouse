from django.shortcuts import render, redirect
from .models import User
from mainapp.models import Warehouse
from .forms import UserForm, UserLoginForm, UserAuthForm
from django.contrib import sessions


def add_user(request):
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
    del request.session['name_user']
    message = 'Вы вышли из учётной записи'
    return render(request, 'userapp/user_index.html', {'message': message})


def delete_user(request):
    name_user = request.session.get('name_user', '')
    if name_user == '':
        return render(request, 'mainapp/index.html')
    if request.method == 'POST':
        form = UserAuthForm(request.POST)
        message = 'Неверно введён пароль'
        user = User.objects.filter(name=name_user).first()
        if user.password == request.POST['password']:
            warehouse = Warehouse.objects.filter(user_id=user.pk).all()
            for el in warehouse:
                el.is_active = False
                el.save()
            user.is_active = False
            user.save()
            del request.session['name_user']
            message = 'Запись удалена'
            return render(request, 'userapp/user_index.html', {'message': message})
    else:
        form = UserAuthForm()
        message = 'Введите пароль для подтверждения удаления учётной записи в системе'
    return render(request, 'userapp/user_form.html', {'form': form, 'message': message, 'name_user': name_user})
