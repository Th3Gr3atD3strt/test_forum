from django import forms
#from models import *
from django.contrib.auth.forms  import UserCreationForm

from forum.models import *
from users.models import *

class UserForm(UserCreationForm):
    password1 = forms.CharField(label='Введите пароль')
    password2 = forms.CharField(label='Повторите пароль')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #self.fields['username'] = 'юзернэйм'

    class Meta:
        model = MyUser
        fields = ['username', 'email', 'password1', 'password2']

        labels = {
            'username': 'Придумайте никнэйм',
            'email': 'Введите почту',
            'password1': 'Введите пароль',
            'password2': 'Повторите пароль',
        }

class AddThread(forms.ModelForm):

    class Meta:
        model = Thread
        fields = ['name_tread','text_thread','category_id']
        labels = {
            'name_tread': 'Название Обсуждения',
            'text_thread': 'Суть',
            'category_id': 'Выберите категорию'
        }

class AddAnswer(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['text_area']

        labels = {
            'text_area': f'Введите ответ к обсуждению',
        }