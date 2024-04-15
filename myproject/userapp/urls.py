from django.urls import path, include
from .views import add_user, login_user, logout_user, delete_user, add_telephone, my_information, activity, photo


urlpatterns = [
    path('add_user/', add_user, name='add_user'),
    path('login_user/', login_user, name='login_user'),
    path('logout_user/', logout_user, name='logout_user'),
    path('delete_user/', delete_user, name='delete_user'),
    path('my_information/', my_information, name='my_information'),
    path('add_telephone/', add_telephone, name='add_telephone'),
    path('activity/', activity, name='activity'),
    path('photo/', photo, name='photo'),
]
