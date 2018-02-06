from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import os


class Status(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    nome_foto = models.CharField(max_length=300)
    nome_foto_profile = models.CharField(max_length=300)
    username = models.CharField(max_length=200)
    post_date = models.DateTimeField()
    download_date = models.DateTimeField()
    print_date = models.DateTimeField()

    def __str__(self):
        return (self.nome_foto)
'''Status.objects.create(author=me,nome_foto='lala.jpg',nome_foto_profile='lala2.jpg',username='adidi',post_date='2018-01-01 10:00',download_date='2018-01-02 11:00',print_date='2018-01-03 12:00')
me = User.objects.get(username='admin')'''