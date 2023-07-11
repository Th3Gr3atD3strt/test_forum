from uuid import uuid4

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect
# Create your views here.
from django.urls import reverse

from django_project import settings
from forum.forms import *
from forum.models import *
from users.models import MyUser, UserEmailVerification


def base_view(request):
    threads = Thread.objects.all()
    return render(request, 'forum/base.html')


def forum_view(request):
    threads = Thread.objects.all()
    return render(request, 'forum/main.html', {'title': 'forum page', 'threads': threads})


def thread_view(request, thread_id):
    question = Thread.objects.get(pk=thread_id)
    answers = Answer.objects.filter(thread_id=thread_id)
    context = {
        'question': question,
        'answers': answers,
    }
    return render(request, 'forum/thread.html', context)


def thread_delete(request, thread_id):
    thread = Thread.objects.get(pk=thread_id)
    print(thread)
    thread.delete()
    return redirect(reverse("main_site"))

def answer_delete(request, answer_id):
    answer = Answer.objects.get(pk=answer_id)

    answer.delete()
    return redirect(reverse("thread", kwargs={'thread_id': answer.thread_id.id}))


def thread_create(request):
    forma = AddThread()
    if request.method == 'POST':
        forma = AddThread(request.POST)
        if forma.is_valid():
            data = forma.cleaned_data
            data['user_id'] = MyUser.objects.get(pk=request.user.id)
            thread = Thread(**data)
            thread.save()
            return redirect('thread', thread_id=thread.pk)
        else:
            forma = AddThread(**forma.cleaned_data)
    return render(request, 'forum/create_thread.html', {'form': forma})

def answer_create(request, thread_id):
    form = AddAnswer()
    if request.method == 'POST':
        form = AddAnswer(request.POST)
        if form.is_valid() and request.user.is_active:
            data = form.cleaned_data
            data['thread_id'] = Thread.objects.get(id =thread_id)
            data['user_id'] = MyUser.objects.get(id =request.user.pk)
            answer = Answer.objects.create(**data)
            return redirect(reverse('thread', kwargs={'thread_id':thread_id}))
        else:
            form = AddAnswer(request.POST)
    return render(request, 'forum/create_answer.html', {'form': form})

# РЕГИСТРАЦИЯ, АУТЕНТИФИКАЦИЯ, УДАЛЕНИЕ
def register_view(request):
    forma = UserForm()
    if request.method == 'POST':
        forma = UserForm(request.POST)
        if forma.is_valid():
            forma.save()
            user_id = uuid4()
            email, username = forma.cleaned_data['email'], forma.cleaned_data['username']
            verification_model = UserEmailVerification(uuid=user_id, email=email).save()
            msg = 'http://127.0.0.1:8000' + reverse('confirmation', kwargs={'confirmation_id': user_id,
                                                                            'username': username}
                                                    )
            send_mail(subject=
                      'Подтверждение аккаунта',
                      message=msg,
                      from_email=settings.EMAIL_HOST_USER,
                      recipient_list=[email])
            return HttpResponse('Пожалуйста, проследуйте по ссылке, которая отправлена на ваш Email')
        else:
            forma = UserForm(request.POST)

    return render(request, 'forum/registration.html', {'forma': forma})


def confirmation_view(request, confirmation_id, username):
    try:
        authenticator = UserEmailVerification.objects.get(uuid=confirmation_id)
        user_email = authenticator.email
        user = MyUser.objects.get(username=username, email=user_email)
        user.is_authenticated = True
        user.save()
        authenticator.delete()
        return HttpResponse('Всё чётко!!!')
    except:
        return HttpResponse('Произошла ошибка!Возможно, что вы уже подтвердили свой аккаунт')

##ПОКА НЕ РАБОТАЕТ!!!!!
'''
log:Vitya
Pass:Tank_1521
mail:Th3Gr3atD3str@yandex.ru
'''
def login_wiew(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = authenticate(request=request, username=request.POST['username'], password=request.POST['password'])
            if user and user.is_authenticated:
                login(request, user)
                print(request)
                return HttpResponse('Всё чётко!!!')
        else:
            print(form.errors)
            form = AuthenticationForm(request.POST)

            print('ФОРМА НЕ ВАЛИДНАЯ!!!')
    form = AuthenticationForm()
    print(request.user.is_active)
    print(request.POST)
    return render(request, 'forum/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('main_site')