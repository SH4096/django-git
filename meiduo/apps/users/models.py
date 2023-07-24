from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    phone = models.CharField(max_length=11,unique=True)

    class Meta:
        db_table = 'meiduo_user'
        verbose_name = '用户名'
        verbose_name_plural = verbose_name
