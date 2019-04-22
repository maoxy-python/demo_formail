from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=128, verbose_name='用户名')
    password = models.CharField(max_length=40, verbose_name='密码')
    email = models.EmailField(verbose_name='邮箱')
    c_time = models.DateTimeField(auto_now_add=True, verbose_name='用户的创建时间')
    has_confirm = models.BooleanField(default=False, verbose_name='邮箱是否确认')

    class Meta:
        db_table = 't_user'


class ConfirmString(models.Model):
    code = models.CharField(max_length=256, verbose_name='注册码')
    user = models.OneToOneField('User', on_delete=models.CASCADE, verbose_name='关联的用户')
    c_time = models.DateTimeField(auto_now_add=True, verbose_name='注册码的生成时间')

    class Meta:
        db_table = 't_confirmString'
