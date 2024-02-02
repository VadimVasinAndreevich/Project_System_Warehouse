from django.db import models


class User(models.Model):
    name = models.CharField(verbose_name='имя пользователя', max_length=20, unique=True)
    email = models.EmailField(verbose_name='электронная почта', max_length=50, unique=True)
    password = models.CharField(verbose_name='пароль', max_length=20, unique=True)
    date_register = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(verbose_name='активна', default=True)

    def __repr__(self):
        return f'{self.name},{self.email},{self.password}'
