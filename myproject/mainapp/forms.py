import datetime

from django import forms
from .models import Warehouse, Regions, Cities


class WarehouseForm(forms.ModelForm):

    class Meta:
        model = Warehouse
        fields = ['region', 'city', 'name', 'square', 'type_warehouse', 'type_of_sale', 'image',
                  'description', 'price', 'address']
        widgets = {'type_warehouse': forms.Select(choices=[('Холодный', 'Холодный'), ('Отапливаемый', 'Отапливаемый')],
                                                  attrs={'placeholder': 'Выберите тип склада'}),
                   'type_of_sale': forms.Select(choices=[('Аренда', 'Аренда'), ('Продажа', 'Продажа')],
                                                  attrs={'placeholder': 'Выберите тип продажи'}),
                   'name': forms.TextInput(attrs={'placeholder': 'Введите название склада'}),
                   'address': forms.TextInput(attrs={'placeholder': 'Укажите адрес склада'}),
                   }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['city'].queryset = Cities.objects.all()

        if 'region' in self.data:
            region_id = int(self.data.get('region'))
            self.fields['city'].queryset = Cities.objects.filter(region_id=region_id).order_by('name')
        elif self.instance.pk:
            self.fields['city'].queryset = self.instance.country.city_set.order_by('name')

    """
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
    """


class WarehousePriceForm(forms.Form):
    price = forms.DecimalField(required=False, label='Цена', widget=forms.NumberInput, decimal_places=2)


class WarehouseSaleForm(forms.Form):
    type_of_sale = forms.ChoiceField(label='Тип продажи', choices=[('Продажа', 'Продажа'), ('Аренда', 'Аренда')],
                                     widget=forms.Select(attrs={'class': 'form-check-input'}))


class WarehouseDescriptionForm(forms.Form):
    description = forms.CharField(label='Описание', widget=forms.Textarea(attrs={'class': 'form-control'}))