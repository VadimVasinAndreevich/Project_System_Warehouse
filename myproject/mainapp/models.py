from django.db import models
from userapp.models import User


class Regions(models.Model):
    name = models.CharField(verbose_name='регион', max_length=64, unique=True)
    is_active = models.BooleanField(verbose_name='активна', default=True)

    def __str__(self):
        return self.name


class Cities(models.Model):
    region = models.ForeignKey(Regions, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='город', max_length=32, unique=True)
    is_active = models.BooleanField(verbose_name='активна', default=True)

    def __str__(self):
        return self.name


class Warehouse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    region = models.ForeignKey(Regions, on_delete=models.CASCADE)
    city = models.ForeignKey(Cities, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='склад', max_length=24)
    square = models.DecimalField(verbose_name='площадь склада', max_digits=6, decimal_places=2, default=0)
    type_warehouse = models.CharField(verbose_name='тип склада', max_length=24)
    type_of_sale = models.CharField(verbose_name='тип продажи', max_length=24)
    image = models.ImageField(blank=True)
    description = models.TextField(verbose_name='описание склада', blank=True)
    price = models.DecimalField(verbose_name='цена', max_digits=12, decimal_places=2, default=0)
    address = models.CharField(verbose_name='адрес склада', max_length=200)
    date_add = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(verbose_name='активна', default=True)

    @staticmethod
    def get_items():
        return Warehouse.objects.filter(is_active=True).order_by('region', 'city', 'user')

    def __str__(self):
        return (f'{self.name}, {self.region.name}, {self.city.name}, '
                f'{self.user.name}, {self.type_warehouse}, {self.type_of_sale}')
