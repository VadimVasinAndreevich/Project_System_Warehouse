from django.urls import path
from .views import (warehouse_full, warehouse_form, main_index, warehouse_all_information,
                    my_warehouse, delete_warehouse, change_price)


urlpatterns = [
    path('', main_index, name='main_index'),
    path('warehouse_full/', warehouse_full, name='warehouse_full'),
    path('warehouse_all_information/<int:warehouse_id>/', warehouse_all_information, name='warehouse_all_information'),
    path('warehouse_form/', warehouse_form, name='warehouse_form'),
    path('my_warehouse/', my_warehouse, name='my_warehouse'),
    path('delete_warehouse/<int:warehouse_id>', delete_warehouse, name='delete_warehouse'),
    path('change_price/<int:warehouse_id>', change_price, name='change_price'),
]
