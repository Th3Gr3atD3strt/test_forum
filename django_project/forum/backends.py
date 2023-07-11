import django
from django.contrib.auth.backends import BaseBackend
from django.db.models import Q

from users.models import MyUser


class MyAuthenticationBackend(BaseBackend):
    def authenticate(self, request, username, password):
        user = None
        try:
            user = MyUser.objects.get( Q(username=username) | Q(email=username) )
        except:
            return None
        return user if user.check_password(password) else None

    def get_user(self, user_id):
        try:
            return MyUser.objects.get(pk=user_id)
        except:
            return None