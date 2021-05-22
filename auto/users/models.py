from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager
from django.dispatch import receiver
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token


class User(AbstractUser):
    first_name = None
    last_name = None
    username = models.CharField('이름', unique=True,max_length=50, null = True)
    email = models.EmailField('이메일', unique=True)
    password = models.CharField('비밀번호', max_length=128)
    blood = models.CharField('혈액형', max_length=50, blank=True)
    emergency = models.CharField('긴급전화번호', max_length=128, blank=True)
    disease = models.CharField('질병', max_length=128, blank=True)
    medicine = models.CharField('복용약', max_length=128, blank=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELD = []

    objects = CustomUserManager()
    isactive = models.BooleanField('인증유무',default=False)
    realname = models.CharField('이름', blank=True, max_length=50)
    phone = models.CharField('휴대폰번호', blank=True, max_length=100)
    address = models.CharField('주소', blank=True, max_length=200)
    date_of_birth = models.DateField('생년월일', blank=True, null=True)

    def __str__(self):
        return self.email

@receiver(post_save, sender=User)
def handle_user_save(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
