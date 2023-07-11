from django.http import HttpResponse
from django.urls import path
from forum.views import *

urlpatterns = [
    path('threads/', forum_view, name='main_site'),
    path('register/', register_view, name='registration'),
    path('login/', login_wiew, name='login'),
    path('logout/', logout_view, name='logout'),
    path('thread/<int:thread_id>', thread_view, name='thread'),
    path('thread_create/', thread_create, name='thread_create'),
    path('thread_delete/<int:thread_id>', thread_delete, name='thread_delete'),
    path('answer_create/<int:thread_id>', answer_create ,name='answer_create'),
    path('answer_delete/<int:answer_id>', answer_delete, name='answer_delete'),

]