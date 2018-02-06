from django.shortcuts import render
from django.utils import timezone
from .models import Status
from django.contrib.auth.models import User
import os

def status(request):
    path = 'imagem_original/'
    me = User.objects.get(username='admin')
    nomes_foto = []
    nomes_foto = os.listdir(path)
    for i in nomes_foto:
        obj, created = Status.objects.update_or_create(author=me, nome_foto=i, nome_foto_profile=(i.split('__')[0] + '.jpg'), username=i.split('__')[0], post_date='2000-01-01 00:00:00', download_date='2000-01-01 00:00:00', print_date='2000-01-01 00:00:00')


    status = Status.objects.all()
    return render(request, 'hashtag/status.html', {'status': status})
