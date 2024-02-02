import datetime

from django import forms


class WarehouseForm(forms.Form):
    region = forms.CharField(label='Регион', max_length=50,
                             widget=forms.TextInput(attrs={'class': 'form-control',
                                                           'placeholder': 'Введите название региона'}))
    city = forms.CharField(label='Город', max_length=50,
                           widget=forms.TextInput(attrs={'class': 'form-control',
                                                         'placeholder': 'Введите название города'}))
    name = forms.CharField(label='Название склада', min_length=2, max_length=50,
                           widget=forms.TextInput(attrs={'class': 'form-control',
                                                         'placeholder': 'Введите название склада'}))
    square = forms.DecimalField(label='Площадь', widget=forms.NumberInput, decimal_places=2)
    type_warehouse = forms.ChoiceField(label='Тип склада',
                                       choices=[('Холодный', 'Холодный'), ('Отапливаемый', 'Отапливаемый')],
                                       widget=forms.Select(attrs={'class': 'form-check-input'}))
    type_of_sale = forms.ChoiceField(label='Тип продажи', choices=[('Продажа', 'Продажа'), ('Аренда', 'Аренда')],
                                     widget=forms.Select(attrs={'class': 'form-check-input'}))
    image = forms.ImageField(label='Изображение')
    description = forms.CharField(label='Описание', widget=forms.Textarea(attrs={'class': 'form-control'}))
    price = forms.DecimalField(label='Цена', widget=forms.NumberInput, decimal_places=2)
    address = forms.CharField(label='Адресс', max_length=200,
                              widget=forms.TextInput(attrs={'class': 'form-control',
                                                            'placeholder': 'Введите адрес расположения склада'}))


class WarehousePriceForm(forms.Form):
    price = forms.DecimalField(required=False, label='Цена', widget=forms.NumberInput, decimal_places=2)