from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager

from users.models import MyUser

'''
python manage.py makemigrations
python manage.py migrate

'''

'''class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password']

    object = BaseUserManager()'''

class Category(models.Model):
    name_category = models.CharField(max_length=255)
    slug_category = models.SlugField()

    def __str__(self):
        return  self.name_category


class Thread(models.Model):
    name_tread = models.CharField(max_length=255)
    text_thread = models.TextField()
    category_id = models.ForeignKey('Category', on_delete=models.CASCADE)
    user_id = models.ForeignKey(MyUser, on_delete=models.CASCADE)

class Answer(models.Model):
    text_area = models.TextField()
    thread_id = models.ForeignKey(Thread, on_delete=models.CASCADE)
    user_id = models.ForeignKey(MyUser, on_delete=models.CASCADE)