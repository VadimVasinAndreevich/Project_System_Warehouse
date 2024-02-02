from django.urls import path, include
from .views import add_user, login_user, logout_user, delete_user


urlpatterns = [
    path('add_user/', add_user, name='add_user'),
    path('login_user/', login_user, name='login_user'),
    path('logout_user/', logout_user, name='logout_user'),
    path('delete_user/', delete_user, name='delete_user'),
]
