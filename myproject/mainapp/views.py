from .models import Warehouse, Regions, Cities
from userapp.models import User
from .forms import WarehouseForm, WarehousePriceForm
from userapp.forms import UserAuthForm
from django.shortcuts import render, get_object_or_404
from django.core.files.storage import FileSystemStorage


def main_index(request):
    name_user = request.session.get('name_user', '')
    return render(request, 'mainapp/index.html', {'name_user': name_user})


def warehouse_full(request):
    name_user = request.session.get('name_user', '')
    warehouses = Warehouse.objects.all()
    if name_user == '':
        return render(request, 'mainapp/warehouse_full.html', {'warehouses': warehouses, 'name_user': name_user})
    else:
        user = User.objects.filter(name=name_user).first()
        return render(request, 'mainapp/warehouse_full.html', {'warehouses': warehouses, 'name_user': name_user,
                                                               'user_pk': user.pk})


def my_warehouse(request):
    name_user = request.session.get('name_user', '')
    if name_user == '':
        return render(request, 'mainapp/index.html')
    user = User.objects.filter(name=name_user).first()
    warehouses = Warehouse.objects.filter(user_id=user.pk).all()
    return render(request, 'mainapp/warehouse_full.html', {'warehouses': warehouses, 'name_user': name_user,
                                                           'user_pk': user.pk})


def warehouse_all_information(request, warehouse_id):
    name_user = request.session.get('name_user', '')
    warehouse = get_object_or_404(Warehouse, pk=warehouse_id)
    return render(request, 'mainapp/warehouse_all_information.html', {'warehouse': warehouse, 'name_user': name_user})


def warehouse_form(request):
    name_user = request.session.get('name_user', '')
    if name_user == '':
        return render(request, 'mainapp/index.html')
    if request.method == 'POST':
        form = WarehouseForm(request.POST, request.FILES)
        message = 'Ошибка в данных'
        if form.is_valid():
            title_region = form.cleaned_data['region']
            region = Regions.objects.get(name=title_region)
            title_city = form.cleaned_data['city']
            city = Cities.objects.get(name=title_city)
            name = form.cleaned_data['name']
            square = form.cleaned_data['square']
            type_warehouse = form.cleaned_data['type_warehouse']
            type_of_sale = form.cleaned_data['type_of_sale']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            address = form.cleaned_data['address']
            user = User.objects.get(name=name_user)
            image = form.cleaned_data['image']
            fs = FileSystemStorage()
            fs.save(image.name, image)
            warehouse = Warehouse(region=region, city=city, name=name, square=square, type_warehouse=type_warehouse,
                                  type_of_sale=type_of_sale, image=image, description=description,
                                  price=price, address=address, user=user)
            warehouse.save()
            message = 'Пользователь сохранён'
    else:
        form = WarehouseForm()
        message = 'Заполните форму объявления'
    return render(request, 'mainapp/warehouse_form.html', {'form': form, 'message': message, 'name_user': name_user})


def delete_warehouse(request, warehouse_id):
    name_user = request.session.get('name_user', '')
    if name_user == '':
        return render(request, 'mainapp/index.html')
    if request.method == 'POST':
        form = WarehousePriceForm(request.POST)
        message = 'Неверно введён пароль'
        user = User.objects.filter(name=name_user).first()
        if user.password == request.POST['password']:
            warehouses = Warehouse.objects.filter(pk=warehouse_id).first()
            warehouses.is_active = False
            warehouses.save()
            warehouses = Warehouse.objects.filter(user_id=user.pk).all()
            return render(request, 'mainapp/warehouse_full.html', {'warehouses': warehouses, 'name_user': name_user})
    else:
        form = UserAuthForm()
        message = 'Введите пароль для подтверждения удаления объявления'
    return render(request, 'userapp/user_form.html', {'form': form, 'message': message, 'name_user': name_user})


def change_price(request, warehouse_id):
    name_user = request.session.get('name_user', '')
    if name_user == '':
        return render(request, 'mainapp/index.html')
    if request.method == 'POST':
        form = WarehousePriceForm(request.POST)
        message = 'Неверно введено значение поля'
        user = User.objects.filter(name=name_user).first()
        if form.is_valid():
            warehouses = Warehouse.objects.filter(pk=warehouse_id).first()
            warehouses.price = request.POST['price']
            warehouses.save()
            warehouses = Warehouse.objects.filter(user_id=user.pk).all()
            return render(request, 'mainapp/warehouse_full.html', {'warehouses': warehouses, 'name_user': name_user,
                                                                   'user_pk': user.pk})
    else:
        form = WarehousePriceForm()
        message = 'Введите новое значение'
    return render(request, 'mainapp/warehouse_form.html', {'form': form, 'message': message, 'name_user': name_user})
