from django.http import HttpResponse
from django.shortcuts import render
# render и наследование шаблона проходят от папки templates


def site_view(request):
    return render(request, 'forum/base.html', {'title':  'main page'})