from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser
from django.db import models

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email, password, **kwargs):
        email = self.normalize_email(email)
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **kwargs):
        kwargs['is_staff'], kwargs['is_admin'], kwargs['is_superuser'] = 1, 1, 1
        password = password
        return self.create_user(email, password, **kwargs)

class UserEmailVerification(models.Model):
    email = models.EmailField()
    uuid = models.UUIDField(unique=True)
    date = models.DateTimeField(auto_now_add=True)

class UserEmailChange(models.Model):
    previous_email = models.EmailField()
    new_email = models.EmailField()
    uuid = models.UUIDField(unique=True, auto_created=True)
    date = models.DateTimeField(auto_now_add=True)

class MyUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(unique=True, max_length=50)
    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=0)
    is_admin = models.BooleanField(default=0)
    is_authenticated = models.BooleanField(default=0)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()


